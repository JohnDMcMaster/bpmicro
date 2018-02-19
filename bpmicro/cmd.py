'''
Functionality based on bulk 0x02 write + optional bulk 0x86 read 
'''

from bpmicro.usb import usb_wraps
from bpmicro.usb import validate_read, validate_readv
from bpmicro.util import hexdump, where
from bpmicro import util

import binascii
import struct
import libusb1
import time
from collections import namedtuple

bulk86_dbg = 0
splits = [0]

def atomic_probe(dev):
    where(2)
    cmd_01(dev)

class BadPrefix(Exception):
    pass

class ContFail(Exception):
    pass

class Overcurrent(Exception):
    pass

# Abnormal device communication
class BusError(Exception):
    pass

class Unsupported(Exception):
    pass

# prefix: leave to external logic to packetize
def bulk86(dev, target=None, donef=None, prefix=None):
    bulkRead, _bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    
    dbg = bulk86_dbg
    
    if dbg:
        print
        print 'bulk86'
        where(2)
        try:
            where(3)
        except IndexError:
            pass
    
    # AFAIK certain packets have no way of knowing done
    # other than knowing in advance how many bytes you should expect
    # Strange since there are continue markers
    if donef is None and target is not None:
        def donef(buff):
            return len(buff) == target
    
    '''
    Ex: need to read 4096 bytes
    Max buffer packet size is 512 bytes
    but for some reason only uses up to 256 bytes of real data
    + 3 framing bytes and 0 fills the rest to form 512 byte transfer
    So to transfer the data 
    '''
    def nxt_buff():
        if dbg:
            print '  nxt_buff: reading'
        p = bytearray(bulkRead(0x86, 0x0200))
        if dbg:
            hexdump(p, label='  nxt_buff', indent='    ')
        #print str2hex(p)
        prefix_this = p[0]
        size = (p[-1] << 8) | p[-2]
        '''
        if size != len(p) - 3:
            if truncate and size < len(p) - 3:
                return prefix_this, p[1:1 + size], suffix_this
            else:
                print 'Truncate: %s' % truncate
                print size, len(p) - 3, len(p)
                hexdump(p)
                raise Exception("Bad length (enable truncation?)")
        return prefix_this, p[1:-2], suffix_this
        '''
        # No harm seen in always truncating
        return prefix_this, p[1:1 + size]

    buff = ''
    while True:
        if donef and donef(buff):
            break
            
        # Test on "packet 152/153" (0x64 byte response)
        # gave 19/1010 splits => 1.9% of split
        # Ran some torture tests looping on this to verify this logic is okay
        if dbg and buff:
            print '  NOTE: split packet.  Have %d / %s bytes' % (len(buff), target)
            hexdump(buff, indent='    ')
            splits[0] += 1
        try:
            # Ignore suffix continue until we have a reason to care
            if dbg:
                tstart = time.time()
            prefix_this, buff_this = nxt_buff()
            if dbg:
                tend = time.time()
                print '  time: %0.3f' % (tend - tstart,)
            buff += buff_this
            
            if prefix is not None:
                if prefix != prefix_this:
                    hexdump(buff_this)
                    raise BadPrefix('Wanted prefix 0x%02X, got 0x%02X' % (prefix, prefix_this))
            elif prefix_this == 0x08:
                pass
            else:
                raise BadPrefix('Unknown prefix 0x%02X' % prefix_this)
            
            if donef and not donef(buff):
                if dbg:
                    print '  continue: not done'
                continue
            if dbg:
                print '  break: no special markers'
            break
        
        # FIXME: temp
        except libusb1.USBError:
            #if prefix is None:
            #    return buff
            raise
    #print 'Done w/ buff len %d' % len(buff)
    if target is not None and len(buff) != target:
        hexdump(buff, label='Wrong size', indent='  ')
        prefix_this, buff_this = nxt_buff()
        raise Exception('Target len: buff %d != target %d' % (len(buff), target))
    if dbg:
        hexdump(buff, label='  ret', indent='    ')
        print
    return buff

# FIXME: with target set small but not truncate will happily truncate
# FIXME: suffix 1 means continue read.  Make higher level func
def bulk2(dev, cmd, target=None, donef=None, prefix=None):
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    
    bulkWrite(0x02, cmd)
    return bulk86(dev, target=target, donef=donef, prefix=prefix)

def bulk86_next_read(dev):
    bulkRead, _bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    '''
    Ex: need to read 4096 bytes
    Max buffer packet size is 512 bytes
    but for some reason only uses up to 256 bytes of real data
    + 3 framing bytes and 0 fills the rest to form 512 byte transfer
    So to transfer the data 
    '''
    p = bytearray(bulkRead(0x86, 0x0200))
    #print str2hex(p)
    prefix_this = p[0]
    size = (p[-1] << 8) | p[-2]
    # No harm seen in always truncating
    return prefix_this, p[1:1 + size], size

def bulk2b(dev, cmd):
    '''
    Issue bulk 0x02 command and collate / return bulk 0x86 responses
    prefix is always 0x08?
    '''
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)

    bulkWrite(0x02, cmd)
    ret = ''
    while True:
        # When is prefix not 0x08?
        _prefix, this, size = bulk86_next_read(dev)
        ret += this
        # FIXME: hack
        # Originally I thought this was end of stream flag, but its actually size upper bit
        # What is the proper check?
        # Possibly this...next would return 0 bytes?
        if size < 0x1fd:
            break
    return ret

# 0x40 words
SM_FMT, SM =  util.mkstruct('SM', (
        # namei is referenced by the diagnostics, printed in hex (but as LE)
        'unk00', 'H', 'name', '12s', 'namei', 'I',
        'unk12', 'H', 'unk14', 'H', 'unk16', 'H', 'unk18', 'H', 'unk1A', 'H', 'unk1C', 'H', 'unk1E', 'H',
        'ins_all', 'H', 'pad22', 'H', 'ins_last', 'H', 'unk26', 'H', 'pad28', '28s',
        'unk44', 'H', 'unk46', 'H', 'unk48', 'H', 'pad4A', 'H', 'pad4C', '4s',
        'unk50', 'H', 'unk52', 'H', 'pad54', '44s'
        ), 0x80)

SM2_FMT = '<HHHHHH'

def sm_decode(buff):
    up = list(struct.unpack(SM_FMT, buff))
    # Remove string padding
    up[1] = up[1].replace('\x00', '')
    return SM(*up)

# Read data structure containing serial number
# Other than that bit, meaning is unknown
def sn_r(dev):
    return bulk2(dev, "\x0E\x00", target=0x20)

# Possibly I2C traffic
# Addresses are inclusive
# Addresses in 16 bit words
def periph_r(dev, periph, start, end):
    if not (0 <= start <= 0x40):
        raise Exception("Bad start")
    if not (0 <= end <= 0x40):
        raise Exception("Bad end")
    if start > end:
        raise Exception("Bad start/end")
    words = end - start + 1
    if words < 0:
        raise Exception("Bad start-end")
    '''
    Example commands
    bulk2(dev, "\x22\x02\x22\x00\x23\x00\x06
        read SM 22:23
    
    I fuzzed to find periph 1, no real example commands but this seems to work
        bulk2(dev, "\x22\x01\x00\x00\x7F\x00\x06
    '''
    return bulk2(dev, "\x22" + chr(periph) + chr(start) + "\x00" + chr(end) + "\x00\x06",
                target=(words*2))

# Teach adapter (ex: TA84VLV_FX4) EEPROM
def ta_r(dev, start=0, end=0x3F):
    # bulk2(dev, "\x22\x01" + chr(start) + "\x00" + chr(end) + "\x00\x06"
    return periph_r(dev, 0x01, start, end)

# Read socket module (ex: SM84) EEPROM
def sm_r(dev, start=0, end=0x3F):
    # bulk2(dev, "\x22\x02" + chr(start) + "\x00" + chr(end) + "\x00\x06"
    return periph_r(dev, 0x02, start, end)

# 0x40 words
TA_FMT, TA =  util.mkstruct('TA', (
        # namei is referenced by the diagnostics, printed in hex (but as LE)
        'unk00', 'H', 'name', '12s', 'pad', '16s',
        'unk1E', 'H', 'unk20', 'H', 'pad22', '94s'
        ), 0x80)
def ta_decode(buff):
    up = list(struct.unpack(TA_FMT, buff))
    # Remove string padding
    up[1] = up[1].replace('\x00', '')
    return TA(*up)

'''
********************************************************************************
Higher level functions
********************************************************************************
'''
def sn_read(dev, verbose=False):
    # Generated from packet 118/119
    buff = sn_r(dev)
    if 0:
        validate_read(
                "\x3A\x00\x90\x32\xA7\x02\x2A\x86\x01\x95\x3C\x36\x90\x00\x1F"
                "\x00\x01\x00\xD6\x05\x01\x00\x72\x24\x22\x39\x00\x00\x00\x00\x27"
                "\x1F",
                buff, "packet 120/121")
    sn = buff[6:8]
    #sn = binascii.hexlify(sn)
    sn = struct.unpack('<H', sn)[0]
    if verbose:
        print 'S/N: %s' % sn
    return sn

SM1_FMT = '<H12s18s'
SM1 = namedtuple('sm', ('unk0', 'name', 'unk12'))

def sm_decode3(buff):
    up = list(struct.unpack(SM1_FMT, buff))
    # Remove string padding
    up[1] = up[1].replace('\x00', '')
    return SM1(*up)

# Socket module read command
# Maybe a higher level command instead of the lower level read?
# Only returns the first 32 bytes
def cmd_sm_0e02(dev):
    return bulk2(dev, "\x0E\x02", target=0x20)

def sm_info3(dev):
    buff = cmd_sm_0e02(dev)
    if 0:
        validate_readv((
                  "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
                  "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
                  "\xFF",
                  
                  # Socket module
                  # 00000000  11 00 53 4D 34 38 44 00  00 00 00 00 00 00 5D F4  |..SM48D.......].|
                  # 00000010  39 FF 00 00 00 00 00 00  00 00 00 00 00 00 62 6C  |9.............bl|
                  "\x11\x00\x53\x4D\x34\x38\x44\x00\x00\x00\x00\x00\x00\x00\x5D\xF4" \
                  "\x39\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x62\x6C",
                  ),
                  buff, "packet 136/137")
    # Don't throw exception on no SM for now?)
    # since it will break other code
    if buff == '\xFF' * 32:
        return None
    return sm_decode3(buff)

def sm_info1(dev):
    sm_info0(dev)
    
    # Generated from packet 23/24
    cmd_49(dev)
    
    # Generated from packet 27/28
    sm = sm_info3(dev)
    print 'Name: %s' % sm.name
    return sm

def sm_info0(dev):
    # Original code is likely check if SM is inserted before reading
    gpio_readi(dev)
    gpio_readi(dev)

    sm_info22(dev)
    sm_info24(dev)
    sm_info3(dev)

def sm_is_inserted(gpio):
    return not bool(gpio & gpio_i2s['smn'])

def sm_insert(dev, verbose=True):
    buff = sm_r(dev, 0x10, 0x1F)
    #hexdump(buff, label="sm_insert", indent='  ')
    SM2_FMT = '<HHHH24s'
    SM2 = namedtuple('sm', ('ins_all', 'unk1', 'ins_last', 'unk2', 'res'))
    sm2 = SM2(*struct.unpack(SM2_FMT, buff))
    if verbose:
        # Auto increments during some operation
        print 'SM insertions (all): %d' % sm2.ins_all
        print 'SM insertions (since last): %d' % sm2.ins_last

    return sm2

def sm_info10(dev, verbose=True):
    # Generated from packet 35/36
    buff = sm_r(dev, 0x10, 0x13)
    '''
    something caused fields to update
      Expected; 8
        "\x32\x01\x00\x00\x93\x00\x00\x00"
        00000000  32 01 00 00 93 00 00 00                           |2.......        |
      Actual; 8
        "\x3A\x01\x00\x00\x9B\x00\x00\x00"
        00000000  3A 01 00 00 9B 00 00 00                           |:.......        |
    '''
    hexdump(buff, label="sm_info10", indent='  ')
    SM3_FMT = '<HHHH'
    SM3 = namedtuple('sm3', ('ins_all', 'unk1', 'ins_last', 'unk2'))
    sm3 = SM3(*struct.unpack(SM3_FMT, buff))
    if verbose:
        print '  Insertions (all): %d' % sm3.ins_all
        print '  Insertions (since last): %d' % sm3.ins_last
    return sm3

def sm_info22(dev):
    # Generated from packet 11/12
    buff = sm_r(dev, 0x22, 0x23)
    if 0:
        validate_read("\xAA\x55\x33\xA2", buff, "packet 13/14")

def sm_info24(dev):
    # Generated from packet 15/16
    buff = sm_r(dev, 0x24, 0x25)
    if 0:
        validate_read("\x01\x00\x00\x00", buff, "packet 17/18")

'''
Some sort of large status structure
It seems to always report the same value but changes state quickly as things happen

immediately before and after firmware load (packets 78 - 91)
    /home/mcmaster/lib/python/uvscada/bpm/startup.py.replay():139
    cmd_01 len: 129
      00000010  00 30 00 80 00 00 00 00  00 C0 00 00 00 09 00 08  |.0..............|
    /home/mcmaster/lib/python/uvscada/bpm/startup.py.boot_cold():60
    cmd_01 len: 129
      00000010  00 30 00 81 00 00 00 00  00 C0 00 00 00 09 00 08  |.0..............|
'''
def cmd_01r(dev, validate=True):
    def donef(buff):
        return len(buff) == 129 or len(buff) == 133

    buff = bulk2(dev, '\x01',
            #target=133)
            donef=donef)
    #print 'cmd_01 len: %d' % len(buff)
    return buff

def cmd_01(dev):
    return cmd_01r(dev)

# cmd_01: some sort of big status read
# happens once during startup and a few times during programming write/read cycles

def cmd_02(dev, exp, msg='cmd_2'):
    # Generated from packet 188/189
    buff = bulk2(dev, "\x02", target=6)
    validate_read(exp, buff, msg)

gpio_i2s = {
    # Observed bits
    'u400': 0x0400,
    'u40':  0x0040,
    'u20':  0x0020,
    'u10':  0x0010,
    # clear => present
    'smn':   0x0001,
}
# Not sure if this actually is GPIO
# but seems like a good guess given that it detects socket module insertion
def gpio_readi(dev):
    buff = bulk2(dev, "\x03", target=2)
    validate_readv((
            "\x31\x00",
            "\x71\x04",
            "\x71\x00",
            
            # SM
            "\x30\x00",
            "\x30\x04",
            ),
            buff, "packet 128/129")
    return struct.unpack('<H', buff)[0]
    

def cmd_08(dev, cmd):
    cmdf = "\x08\x01\x57" + cmd + "\x00"
    if len(cmdf) != 5:
        raise Exception("Malfored command")

    buff = bulk2(dev, cmdf, target=0x02)
    validate_read("\x00\x00", buff, "packet W: 359/360, R: 361/362")

def cmd_09(dev):
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    bulkWrite(0x02, "\x09\x10\x57\x81\x00")

# cmd_04

# cmd_08

'''
1 => LED on

LEDs:
-1: fail
-2: active
-4: pass
'''
led_s2i = {
            'fail': 1,
            'active': 2,
            'pass': 4,
            #'green': 1,
            #'orange': 2,
            #'red': 4,
            }
led_i2s = dict((v, k) for k, v in led_s2i.iteritems())

def cmd_0C_mk():
    return "\x0C\x04"

def led_mask(dev, mask):
    mask = led_s2i.get(mask, mask)
    if mask < 0 or mask > 7:
        raise ValueError("Bad mask")
    #dev.bulkWrite(endpoint, data, timeout=timeout)
    dev.bulkWrite(0x02, "\x0C" + chr(mask), timeout=1000)

def led_mask_30(dev, mask):
    mask = led_s2i.get(mask, mask)
    if mask < 0 or mask > 7:
        raise ValueError("Bad mask")
    buff = bulk2(dev, "\x0C" + chr(mask) + "\x30", target=2)
    validate_read(chr(mask) + "\x00", buff, "packet 9/10")    

# cmd_10
def cmd_10(dev):
    buff = bulk2(dev, "\x10\x80\x02", target=0x06)
    # Discarded 3 / 9 bytes => 6 bytes
    validate_read("\x80\x00\x00\x00\x09\x00", buff, "packet W: 65/66, R: 67/68")

def cmd_11_mk():
    return "\x11\xF0\xFF"

# cmd_14 repeat

# cmd_1D

def cmd_20_mk():
    '''
    Examples:
    bulkWrite(0x02, "\x20\x01\x00 \x0C\x04")
    bulkWrite(0x02, "\x20\x01\x00 \x50\x7D\x02\x00\x00")
    '''
    return "\x20\x01\x00"

def cmd_20(dev):
    _bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)
    # No reply
    bulkWrite(0x02, cmd_20_mk())


# cmd_22 peripheral (I2C?) read

# Reset socket module insertion counter
def sm_rst(dev):
    buff = bulk2(dev,
            "\x23\x02\x12\x00\x13\x00\x06\x00\x00\x00\x00\x00\x00\x12\xAA",
            target=0x01)
    validate_read("\xAB", buff, "packet W: 5/6, R: 7/8")

# cmd_30: see LED functions

# cmd_3B
def cmd_3B(dev):
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    
    bulkWrite(0x02, 
        "\x3B\x0C\x22\x00\xC0\x40\x00\x3B\x0E\x22\x00\xC0\x00\x00\x3B\x1A" \
        "\x22\x00\xC0\x18\x00"
        )

def cmd_41(dev):
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    bulkWrite(0x02, "\x41\x00\x00")

def cmd_43_mk(cmd):
    ret = "\x43\x19" + cmd + "\x00\x00"
    if len(ret) != 5:
        raise Exception("Bad length")
    return ret

def cmd_43(dev, cmd):
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    
    # "\x43\x19\x00\x00\x00"
    # "\x43\x19\x10\x00\x00"
    bulkWrite(0x02, cmd_43_mk(cmd))

# cmd_45
def cmd_45(dev):
    buff = bulk2(dev, "\x45\x01\x00\x00\x31\x00\x06", target=0x64)
    # Discarded 3 / 103 bytes => 100 bytes
    validate_read(
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF"
        , buff, "packet W: 77/78, R: 79/80")

# Common (GPIO/status?)
# Oddly sometimes this requires truncation and sometimes doesn't
def cmd_49(dev):
    # Generated from packet 156/157
    buff = bulk2(dev, "\x49", target=2)
    validate_read("\x0F\x00", buff, "packet 158/159")
    return buff

# cmd_4A
def cmd_4A(dev):
    # Generated from packet 123/124
    buff = bulk2(dev, "\x4A\x03\x00\x00\x00", target=0x02)
    # Discarded 3 / 5 bytes => 2 bytes
    validate_read("\x03\x00", buff, "packet W: 123/124, R: 125/126")

def cmd_4C(dev):
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    bulkWrite(0x02, "\x4C\x00\x02")
'''

Always
-begin with 0x57
-end with 0x00

Payload size varies
-1
-4

Often returns 0000 but not always
Return size can vary

think these are literlaly a 57 command followed by a 50 command
this hints that I can string (some?) commands together
but it may not be obvious to know where the boundary is
'''

def cmd_50_mk(cmd):
    '''
    Example:
    "\x50\x9F\x09\x00\x00"
    As part of a larger command:
    "\x57\x82\x00 \x50\x1D\x00\x00\x00"
    '''
    ret = "\x50" + cmd + "\x00\x00"
    if len(ret) != 5:
        raise Exception("Malfored command")
    return ret

def cmd_50(dev, cmd):
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    # No reply
    bulkWrite(0x02, cmd_50_mk(cmd))

def cmd_57_mk(cmd):
    return "\x57" + cmd + "\x00"

def cmd_57s(dev, cmds, exp, msg="cmd_57"):
    out = ''.join([cmd_57_mk(c) for c in cmds])
    buff = bulk2b(dev, out)
    validate_read(exp, buff, msg)
    return buff

def cmd_57_94(dev):
    cmd_57s(dev, '\x94', "\x62",  "cmd_57_94")
    # Seems to get paired with this
    buff = bulk86(dev, target=0x01, prefix=0x18)
    validate_read("\x0B", buff, "packet 545/546")

def cmd_57_50(dev, c57, c50):
    # ex: bulkWrite(0x02, "\x57\x82\x00 \x50\x1D\x00\x00\x00")
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    bulkWrite(0x02, cmd_57_mk(c57) + cmd_50_mk(c50))

# cmd_5A: encountered once

# cmd_66

# cmd_80

# cmd_82

# cmd_A6

# cmd_DB

# cmd_E9

def readB0(dev):
    _bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)

    # Atomic
    # Generated from packet 11/12
    buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
    # Req: 4096, got: 3
    validate_read("\x00\x00\x00", buff, "packet 11/12")
    # Generated from packet 13/14
    buff = bulk86(dev, target=0x01)
    validate_read("\x16", buff, "packet 13/14")

def cmd_1438(dev):
    # Generated from packet 253/254
    buff = bulk2(dev, 
        "\x14\x38\x25\x00\x00\x04\x00\x90\x32\x90\x00\xA7\x02\x1F\x00\x14" \
        "\x40\x25\x00\x00\x01\x00\x3C\x36\x0E\x01", target=0x20)
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C",
        buff, "packet W: 253/254, R: 255/256")

def check_cont(dev, verbose=False, removed_ref=None):
        # Generated from packet 241/242
        # Takes about 0.05 sec on pass but 0.52 sec on fail
        tstart = time.time()
        buff = cmd_57s(dev, "\x85", None,  "check_cont")
        tend = time.time()
        if verbose:
            print 'Continuity test took %0.3f sec' % (tend - tstart,)
            #util.hexdump(buff, label='Continuity', indent='  ')
        # Chip inserted
        if buff == "\x01":
            if verbose:
                print 'Continuity OK'
        # Chip removed
        elif removed_ref and buff == removed_ref:
            raise ContFail('Continuity complete failure (part not inserted?)')
        # Inserting chip while running
        # I'm guessing its telling me which pins failed
        # Lets bend a pin and verify
        else:
            raise ContFail('Continuity partial failure (dirty contacts?  Inserted wrong?)')
