from bpmicro.usb import usb_wraps
from bpmicro.util import hexdump

from bpmicro.cmd import bulk2, bulk86
from bpmicro.cmd import sm_info3, led_mask_30
from bpmicro.cmd import cmd_20_mk, cmd_49, cmd_02, cmd_50, cmd_50_mk, cmd_0C_mk, cmd_57s, cmd_57_50, cmd_41, cmd_43, cmd_10, cmd_45
from bpmicro.cmd import cmd_4C, cmd_09, cmd_08, cmd_3B, cmd_4A
from bpmicro.cmd import sm_info0, sm_info1, sm_insert, sn_read, sm_info10
from bpmicro.usb import validate_read
from bpmicro.cmd import cmd_01
from bpmicro import cmd
import bpmicro.device
from . import i87c51_fw

import usb1
import sys
import inspect
import time


def dexit():
    print('Debug break')
    sys.exit(0)


def fw_read(dev, target=4096):
    print('Verifying firmware readback')
    # Generated from packet 381/382
    # WARNING: unexpected suffix: 0x01
    #buff = bulk2(dev, "\x08\x00\x57\x8F\x00", target=len(fw))
    buff = bulk2(dev, "\x08\x00\x57\x8F\x00", target=target)
    return buff


def dev_read(dev, cont, verbose=False):
    read_replay1(dev, cont)
    return read_replay2(dev, cont)


def read_replay1(dev, cont=True):
    _bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)

    cmd.readB0(dev)

    # Generated from packet 15/16
    cmd_01(dev)

    # NOTE:: req max 512 but got 136
    # Generated from packet 19/20
    buff = cmd.bulk2(dev,
        "\x43\x19\x10\x00\x00\x3B\x7E\x25\x00\x00\xFE\xFF\x3B\x7C\x25\x00" \
        "\x00\xFE\xFF\x00", target=0x02)
    validate_read("\xA4\x06", buff, "packet W: 19/20, R: 21/22")

    # Generated from packet 23/24
    cmd_01(dev)

    # Generated from packet 27/28
    sn_read(dev)

    # Generated from packet 31/32
    cmd.cmd_1438(dev)

    sm_info1(dev)

    # Generated from packet 55/56
    cmd_01(dev)

    # NOTE:: req max 512 but got 136
    # Generated from packet 59/60
    cmd_43(dev, "\x10")

    # Generated from packet 61/62
    bulkWrite(0x02, cmd_20_mk() + cmd_0C_mk())

    # Generated from packet 63/64
    cmd_41(dev)

    # Generated from packet 65/66
    cmd_10(dev)

    sm_info3(dev)
    '''
    validate_read(
        "\x11\x00\x53\x4D\x34\x38\x44\x00\x00\x00\x00\x00\x00\x00\x5D\xF4" \
        "\x39\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x62\x6C"
        , buff, "packet W: 69/70, R: 71/72")
    '''

    sm_insert(dev)

    # Generated from packet 77/78
    cmd_45(dev)

    # Generated from packet 81/82
    cmd_49(dev)

    sm_info1(dev)

    sm_insert(dev)

    # Generated from packet 117/118
    sm_info10(dev)

    # Generated from packet 121/122
    cmd_3B(dev)

    cmd_4A(dev)

    # NOTE:: req max 512 but got 5
    # Generated from packet 127/128
    cmd_4C(dev)
    # Generated from packet 129/130
    # None (0xB2)
    buff = controlWrite(0x40, 0xB2, 0x0000, 0x0000, "")

    # Atomic
    # Generated from packet 131/132
    cmd_50(dev, "\x5D\x00")
    # Generated from packet 133/134
    buff = bulk2(dev,
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x10" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x80" \
        "\xE9\x02\x00\x00\x00\x90\x00\xE9\x04\x00\x00\x00\x00\x00\x00\x00" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x00\x00" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x80\x00", buff, "packet W: 133/134, R: 135/136")

    # Generated from packet 137/138
    cmd_02(dev, "\x81\x00\x60\x00\x09\x00", "packet W: 137/138, R: 139/140")

    # Atomic
    # Generated from packet 141/142
    cmd_50(dev, "\xC0\x00")
    # Generated from packet 143/144
    buff = bulk2(dev,
        "\x66\xB8\x01\x2D\x81\xE3\xFF\xFF\x00\x00\x66\xBB\x18\x00\x66\xC7" \
        "\x05\x30\x40\x00\xC0\xF0\xFF\x89\xD9\xC1\xE1\x02\x66\xC7\x81\x02" \
        "\x00\x00\x00\xF0\xFF\x66\x03\x05\xE4\x46\x00\x00\x66\x89\x05\x90" \
        "\x40\x00\xC0\x89\xDA\x81\xCA\x00\x80\x00\x00\x66\x89\x15\x50\x40" \
        "\x00\xC0\xC6\x05\x14\x22\x00\xC0\x7B\x81\xCA\x00\x40\x00\x00\x66" \
        "\x89\x15\x50\x40\x00\xC0\x89\xD9\x66\xC1\xE1\x02\x66\x89\x81\x00" \
        "\x00\x00\x00\x66\x2B\x05\xE4\x46\x00\x00\xC6\x05\x14\x22\x00\xC0" \
        "\xBB\x81\xCB\x00\x80\x00\x00\x66\x89\x1D\x50\x40\x00\xC0\x89\xC2" \
        "\x81\xE2\x07\x00\x00\x00\x03\xD2\x81\xCA\x01\x00\x00\x00\x89\xD9" \
        "\x81\xE1\x03\x00\x00\x00\xD3\xE2\xD3\xE2\xD3\xE2\xD3\xE2\xD3\xE2" \
        "\xC1\xE2\x0A\x89\xD9\x81\xE1\xFC\x03\x00\x00\x09\xCA\x88\x82\x00" \
        "\x00\x00\x40\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x81\x00", buff, "packet W: 143/144, R: 145/146")

    # Generated from packet 147/148
    cmd_02(dev, "\x82\x00\x20\x01\x09\x00", "packet W: 147/148, R: 149/150")

    # Generated from packet 151/152
    cmd_09(dev)

    # Generated from packet 153/154
    cmd_02(dev, "\x82\x00\x20\x01\x09\x00", "packet W: 153/154, R: 155/156")

    # added
    sm_insert(dev)

    print('Going active')
    led_mask_30(dev, 'active')

    # Atomic
    # Generated from packet 161/162
    cmd_50(dev, "\x18\x00")
    # Generated from packet 163/164
    buff = bulk2(dev,
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x82\x00", buff, "packet W: 163/164, R: 165/166")

    # Generated from packet 167/168
    cmd_02(dev, "\x83\x00\x40\x01\x09\x00", "packet W: 167/168, R: 169/170")

    # Generated from packet 171/172
    buff = bulk2(dev,
        "\x57\x82\x00\x20\x01\x00\x2B\x3B\x0C\x22\x00\xC0\x40\x00\x3B\x0E" \
        "\x22\x00\xC0\x00\x00\x3B\x1A\x22\x00\xC0\x18\x00\x0E\x01"
        , target=0x20)

    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 171/172, R: 173/174")

    sm_info0(dev)

    # Generated from packet 195/196
    buff = bulk2(dev, "\x48\x00\x10\x82\x02", target=0x06)

    validate_read("\x82\x00\x20\x01\x09\x00", buff,
                  "packet W: 195/196, R: 197/198")

    # Generated from packet 199/200
    bulkWrite(0x02, cmd_20_mk() + cmd_50_mk("\x7D\x02"))

    # Generated from packet 201/202
    buff = bulk2(dev, i87c51_fw.p201, target=0x02)

    validate_read("\x82\x00", buff, "packet W: 201/202, R: 203/204")

    # Generated from packet 205/206
    cmd_02(dev, "\x83\x00\xA0\x03\x09\x00", "packet W: 205/206, R: 207/208")

    # Atomic
    # Generated from packet 209/210
    cmd_57_50(dev, "\x82", "\x1D\x00")
    # Generated from packet 211/212
    buff = bulk2(dev,
        "\xC7\x05\x74\x46\x00\x00\x0B\x00\x00\x00\xFF\x15\x38\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x83\x00", buff, "packet W: 211/212, R: 213/214")

    # Generated from packet 215/216
    cmd_02(dev, "\x84\x00\xC0\x03\x09\x00", "packet W: 215/216, R: 217/218")

    # Atomic
    '''
    Seems these must be done together
    Increments socket insertion count
    '''
    # Generated from packet 219/220
    cmd_57_50(dev, "\x83", "\x18\x3A")
    # p221.bin: DOS executable (COM)
    # Generated from packet 221/222
    buff = bulk2(dev, i87c51_fw.p221, target=0x02)

    validate_read("\x84\x00", buff, "packet W: 221/222, R: 223/224")

    # Generated from packet 225/226
    cmd_02(dev, "\x85\x00\xE0\x3D\x09\x00", "packet W: 225/226, R: 227/228")

    # Generated from packet 229/230
    bulkWrite(0x02,
        "\x57\x84\x00\xF0\xFF\xFF\x0F\xF0\xFF\xFF\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\xF0\x0F\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        )

    # Atomic
    # Generated from packet 231/232
    cmd_50(dev, "\xDE\x03")
    # Generated from packet 233/234
    buff = bulk2(dev, i87c51_fw.p233, target=0x02)

    validate_read("\x85\x00", buff, "packet W: 233/234, R: 235/236")

    # Generated from packet 237/238
    cmd_02(dev, "\x86\x00\xC0\x41\x09\x00", "packet W: 237/238, R: 239/240")

    # The actual continuity check
    if cont:
        # Generated from packet 241/242
        # Takes about 0.05 sec on pass but 0.52 sec on fail
        tstart = time.time()
        buff = cmd_57s(dev, "\x85", None, "cmd_57")
        tend = time.time()
        print(('Continuity test took %0.3f sec' % (tend - tstart, )))
        hexdump(buff, label='Continuity', indent='  ')
        # Chip inserted
        if buff == "\x01":
            print('Continuity OK')
        # Chip removed
        elif buff == ("\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
                    "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"):
            raise cmd.ContFail(
                'Continuity complete failure (part not inserted?)')
        # Inserting chip while running
        # I'm guessing its telling me which pins failed
        # Lets bend a pin and verify
        else:
            raise cmd.ContFail(
                'Continuity partial failure (dirty contacts?  Inserted wrong?)'
            )

    # Atomic with following operation
    # Generated from packet 245/246
    cmd_50(dev, "\x62\x00")

    # Generated from packet 247/248
    buff = bulk2(dev,
        "\x00\x00\x3C\x00\x38\x00\x34\x00\x30\x00\x3D\x00\x39\x00\x35\x00" \
        "\x31\x00\x3E\x00\x3A\x00\x36\x00\x32\x00\x3F\x00\x3B\x00\x37\x00" \
        "\x33\x00\x1E\x00\x1A\x00\x16\x00\x00\x00\x02\x00\x06\x00\x0A\x00" \
        "\x0E\x00\x23\x00\x27\x00\x2B\x00\x2F\x00\x22\x00\x26\x00\x2A\x00" \
        "\x2E\x00\x21\x00\x25\x00\x29\x00\x2D\x00\x20\x00\x24\x00\x28\x00" \
        "\x1C\x00\x00\x00\x04\x00\x08\x00\x0C\x00\x10\x00\x14\x00\x18\x00" \
        "\x1C\x00"
        , target=0x02)

    validate_read("\x86\x00", buff, "packet W: 247/248, R: 249/250")

    # Generated from packet 251/252
    cmd_02(dev, "\x87\x00\x30\x42\x09\x00", "packet W: 251/252, R: 253/254")

    # Atomic with next
    # Generated from packet 255/256
    bulkWrite(0x02,
        "\x1D\xC0\x41\x09\x00\x28\x00\x15\x60\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x01\x00\x00\x00\x1C\x30\x00\x00\x00\x08\x00\x00\x00\x48" \
        "\x00\x50\x71\x09\x00\x00")

    # Generated from packet 257/258
    buff = bulk2(dev, i87c51_fw.p257, target=0x02)

    validate_read("\x87\x00", buff, "packet W: 257/258, R: 259/260")

    # Generated from packet 261/262
    cmd_02(dev, "\x88\x00\xB0\x4B\x09\x00", "packet W: 261/262, R: 263/264")

    # Generated from packet 265/266
    cmd_57s(dev, "\x87", "\x00\x00", "cmd_57")

    # Atomic
    # Generated from packet 269/270
    cmd_50(dev, "\x17\x00")
    # Generated from packet 271/272
    buff = bulk2(dev,
        "\xC7\x05\x2C\x00\x09\x00\x24\x04\x00\x00\x66\xB9\x00\x00\xB2\x00" \
        "\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x88\x00", buff, "packet W: 271/272, R: 273/274")

    # Generated from packet 275/276
    cmd_02(dev, "\x89\x00\xD0\x4B\x09\x00", "packet W: 275/276, R: 277/278")

    # Atomic
    # Generated from packet 279/280
    cmd_57_50(dev, "\x88", "\x32\x07")
    # Generated from packet 281/282
    buff = bulk2(dev, i87c51_fw.p281, target=0x02)

    validate_read("\x89\x00", buff, "packet W: 281/282, R: 283/284")

    # Generated from packet 285/286
    cmd_02(dev, "\x8A\x00\x10\x53\x09\x00", "packet W: 285/286, R: 287/288")

    # Generated from packet 289/290
    cmd_57s(dev, '\x89', "\x00\x00")

    # Atomic
    # Generated from packet 293/294
    cmd_50(dev, "\x3D\x03")
    # Generated from packet 295/296
    buff = bulk2(dev, i87c51_fw.p295, target=0x02)

    validate_read("\x8A\x00", buff, "packet W: 295/296, R: 297/298")

    # Generated from packet 299/300
    cmd_02(dev, "\x8B\x00\x50\x56\x09\x00", "packet W: 299/300, R: 301/302")

    # Generated from packet 303/304
    cmd_57s(dev, "\x8A", "\x89\x00")

    # Atomic
    # Generated from packet 307/308
    cmd_50(dev, "\x1D\x00")
    # Generated from packet 309/310
    buff = bulk2(dev,
        "\x66\x8B\x0D\x1A\x24\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x8B\x00", buff, "packet W: 309/310, R: 311/312")
    # Generated from packet 313/314
    cmd_02(dev, "\x8C\x00\x70\x56\x09\x00", "packet W: 313/314, R: 315/316")

    # Generated from packet 317/318
    # Bad part returns \x59\x00 but otherwise can be read
    # (with partially corrupt bit pattern)
    if cont:
        buff = cmd_57s(dev, "\x8B", None)
        if buff == "\x59\x00":
            raise Exception("Failed 0x8B health check")
        else:
            validate_read("\x58\x00", buff, "")

    # Atomic
    # Generated from packet 321/322
    cmd_50(dev, "\xF8\x04")
    # Generated from packet 323/324
    buff = bulk2(dev, i87c51_fw.p323, target=0x02)

    validate_read("\x8C\x00", buff, "packet W: 323/324, R: 325/326")

    # Generated from packet 327/328
    cmd_02(dev, "\x8D\x00\x70\x5B\x09\x00", "packet W: 327/328, R: 329/330")

    # Generated from packet 331/332
    cmd_57s(dev, '\x8C', "\x00\x00")

    # Atomic
    # Generated from packet 335/336
    cmd_50(dev, "\x18\x00")
    # Generated from packet 337/338
    buff = bulk2(dev,
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x8D\x00", buff, "packet W: 337/338, R: 339/340")

    # Generated from packet 341/342
    cmd_02(dev, "\x8E\x00\x90\x5B\x09\x00", "packet W: 341/342, R: 343/344")

    # Generated from packet 345/346
    cmd_57s(dev, "\x8D\x89", "\x00\x00")

    # Atomic
    # Generated from packet 349/350
    cmd_50(dev, "\xFA\x01")
    # Generated from packet 351/352
    buff = bulk2(dev, i87c51_fw.p351, target=0x02)
    validate_read("\x8E\x00", buff, "packet W: 351/352, R: 353/354")

    # Generated from packet 355/356
    cmd_02(dev, "\x8F\x00\x90\x5D\x09\x00", "packet W: 355/356, R: 357/358")

    # Generated from packet 323/324
    cmd_08(dev, "\x8E")

    # Generated from packet 363/364
    cmd_57s(dev, '\x8C', "\x00\x00")


def read_replay2(dev, cont):
    # Generated from packet 367/368
    cmd_57s(dev, "\x8D\x89", "\x00\x00")

    # Atomic
    # Generated from packet 371/372
    cmd_50(dev, "\xDD\x05")
    # Generated from packet 373/374
    buff = bulk2(dev, i87c51_fw.p373, target=0x02)

    validate_read("\x8F\x00", buff, "packet W: 373/374, R: 375/376")

    # Generated from packet 377/378
    cmd_02(dev, "\x90\x00\x70\x63\x09\x00", "packet W: 377/378, R: 379/380")

    fw_in = fw_read(dev)
    print('Readback ok')

    # Generated from packet 401/402
    cmd_57s(dev, '\x8C', "\x00\x00")

    # Atomic
    # Generated from packet 405/406
    cmd_50(dev, "\x0D\x00")
    # Generated from packet 407/408
    buff = bulk2(dev,
                 "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00",
                 target=0x02)
    validate_read("\x90\x00", buff, "packet W: 407/408, R: 409/410")

    # Generated from packet 411/412
    cmd_02(dev, "\x91\x00\x80\x63\x09\x00", "packet W: 411/412, R: 413/414")

    # Atomic
    # Generated from packet 415/416
    cmd_57_50(dev, "\x90", "\x1A\x00")
    # Generated from packet 417/418
    buff = bulk2(dev,
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00\x66\xB9\x00" \
        "\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x91\x00", buff, "packet W: 417/418, R: 419/420")

    cmd_02(dev, "\x92\x00\xA0\x63\x09\x00", "packet W: 421/422, R: 423/424")

    cmd_57s(dev, "\x91", "\x00\x00", "packet W: 425/426, R: 427/428")

    led_mask_30(dev, 'pass')

    sm_info1(dev)
    sm_insert(dev)
    sm_info10(dev)

    return fw_in


class NotBlank(Exception):
    pass


# sm scan for large values
# Exception: prefix: wanted 0x08, got 0x2C
'''
TODO: handle better
If you try to program something you can't
(ie a non-erased part)
you'll get
BadPrefix: Wanted prefix 0x18, got 0x08
with reply  \x63\x01
'''


def fw_w(dev, fw, verbose=False):
    pos = 0
    print('FW load: begin')
    tstart = time.time()
    while pos < len(fw):
        remain = len(fw) - pos
        chunk = fw[pos:pos + min(remain, 0xCC)]
        if len(chunk) == remain:
            prefix = 0x08
            reply = "\x00"
        else:
            prefix = 0x18
            reply = "\x0B"
        if verbose:
            print(('  pos 0X%04X, len 0x%02X, prefix 0x%02X' %
                   (pos, len(chunk), prefix)))
        buff = bulk2(dev,
                     chr(len(chunk)) + '\x00' + chunk,
                     target=0x01,
                     prefix=prefix)
        validate_read(reply, buff, "packet W: 429/430, R: 431/432")
        pos += len(chunk)
    tend = time.time()
    print(('FW load : end.  Took %0.1f sec' % (tend - tstart, )))


'''
First one is a program cycle, others are simply 
FW load: begin
FW load : end.  Took 2.7 sec
FW load: begin
FW load : end.  Took 0.1 sec
FW load: begin
FW load : end.  Took 0.1 sec
'''


#def replay(dev, fw, cont=True, blank=True):
def dev_write(dev, devcfg, cont=True, verbose=False, blank=True):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)
    fw = devcfg['code']

    # Generated by uvusbreplay 0.1
    # uvusbreplay copyright 2011 John McMaster <JohnDMcMaster@gmail.com>
    # cmd: /home/mcmaster/bin/usbrply --packet-numbers --no-setup --comment --fx2 --packet-numbers -j cap/2015-10-11/i87c51_13_write_cont_id_blank_v2_ff.cap

    # FIXME: size?
    read_replay1(dev, cont)

    # Generated from packet 363/364
    cmd_57s(dev, '\x8C', "\x00\x00")

    # Generated from packet 367/368
    cmd_50(dev, "\x18\x00")

    # Generated from packet 369/370
    buff = bulk2(dev,
        "\x66\xB8\x01\x2D\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x8F\x00", buff, "packet W: 369/370, R: 371/372")
    # Generated from packet 373/374
    buff = bulk2(dev, "\x02", target=0x06)

    validate_read("\x90\x00\xB0\x5D\x09\x00", buff,
                  "packet W: 373/374, R: 375/376")
    # Generated from packet 377/378
    buff = bulk2(dev, "\x57\x8F\x00\x57\x89\x00", target=0x02)

    validate_read("\x00\x00", buff, "packet W: 377/378, R: 379/380")

    # Generated from packet 381/382
    cmd_50(dev, "\x0A\x06")

    # Generated from packet 383/384
    buff = bulk2(dev, i87c51_fw.p383, target=0x02)

    validate_read("\x90\x00", buff, "packet W: 383/384, R: 385/386")
    # Generated from packet 387/388
    buff = bulk2(dev, "\x02", target=0x06)

    validate_read("\x91\x00\xC0\x63\x09\x00", buff,
                  "packet W: 387/388, R: 389/390")

    # Generated from packet 391/392
    if blank:
        print('Blank checking')
        tstart = time.time()
        buff = bulk2(dev, "\x08\x00\x57\x90\x00", target=0x02)
        tend = time.time()
        print(('Blank test took %0.3f sec' % (tend - tstart, )))
        if buff == "\x00\x00":
            print('Blank: pass')
        elif buff == "\x01\x00":
            raise NotBlank('Blank: fail')
        else:
            hexdump(buff)
            raise Exception("Unknown blank status")

    # Generated from packet 395/396
    cmd_57s(dev, '\x8C', "\x00\x00")

    # Generated from packet 399/400
    cmd_50(dev, "\x18\x00")

    # Generated from packet 401/402
    buff = bulk2(dev,
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x91\x00", buff, "packet W: 401/402, R: 403/404")
    # Generated from packet 405/406
    buff = bulk2(dev, "\x02", target=0x06)

    validate_read("\x92\x00\xE0\x63\x09\x00", buff,
                  "packet W: 405/406, R: 407/408")
    # Generated from packet 409/410
    buff = bulk2(dev, "\x57\x91\x00\x57\x89\x00", target=0x02)

    validate_read("\x00\x00", buff, "packet W: 409/410, R: 411/412")

    # Generated from packet 413/414
    cmd_50(dev, "\x9F\x09")

    # Generated from packet 415/416
    buff = bulk2(dev, i87c51_fw.p415, target=0x02)

    validate_read("\x92\x00", buff, "packet W: 415/416, R: 417/418")
    # Generated from packet 419/420
    buff = bulk2(dev, "\x02", target=0x06)

    validate_read("\x93\x00\x80\x6D\x09\x00", buff,
                  "packet W: 419/420, R: 421/422")
    # Generated from packet 423/424
    buff = bulk2(dev, "\x57\x92\x00", target=0x01)

    validate_read("\x62", buff, "packet W: 423/424, R: 425/426")
    # Generated from packet 427/428

    # NOTE: prefix 0x18
    buff = bulk86(dev, target=0x01, prefix=0x18)
    validate_read("\x0B", buff, "packet 427/428")

    # Generated from packet 429/430
    fw_w(dev, fw, verbose=True)

    # Generated from packet 513/514
    cmd_57s(dev, '\x8C', "\x00\x00")

    # Generated from packet 517/518
    cmd_50(dev, "\x18\x00")

    # Generated from packet 519/520
    buff = bulk2(dev,
        "\x66\xB8\x01\x2D\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x93\x00", buff, "packet W: 519/520, R: 521/522")
    # Generated from packet 523/524
    buff = bulk2(dev, "\x02", target=0x06)

    validate_read("\x94\x00\xA0\x6D\x09\x00", buff,
                  "packet W: 523/524, R: 525/526")
    # Generated from packet 527/528
    buff = bulk2(dev, "\x57\x93\x00\x57\x89\x00", target=0x02)

    validate_read("\x00\x00", buff, "packet W: 527/528, R: 529/530")

    # Generated from packet 531/532
    cmd_50(dev, "\xE0\x08")

    # Generated from packet 533/534
    buff = bulk2(dev, i87c51_fw.p533, target=0x02)

    validate_read("\x94\x00", buff, "packet W: 533/534, R: 535/536")
    # Generated from packet 537/538
    buff = bulk2(dev, "\x02", target=0x06)

    validate_read("\x95\x00\x80\x76\x09\x00", buff,
                  "packet W: 537/538, R: 539/540")

    # Generated from packet 541/542
    cmd.cmd_57_94(dev)

    # Generated from packet 547/548
    fw_w(dev, fw)

    # Generated from packet 631/632
    cmd_57s(dev, '\x8C', "\x00\x00")

    # Generated from packet 635/636
    cmd_50(dev, "\x18\x00")

    # Generated from packet 637/638
    buff = bulk2(dev,
        "\x66\xB8\x01\x37\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x95\x00", buff, "packet W: 637/638, R: 639/640")
    # Generated from packet 641/642
    buff = bulk2(dev, "\x02", target=0x06)

    validate_read("\x96\x00\xA0\x76\x09\x00", buff,
                  "packet W: 641/642, R: 643/644")
    # Generated from packet 645/646
    buff = bulk2(dev, "\x57\x95\x00\x57\x89\x00", target=0x02)

    validate_read("\x00\x00", buff, "packet W: 645/646, R: 647/648")

    # Generated from packet 649/650
    cmd.cmd_57_94(dev)

    # Generated from packet 655/656
    fw_w(dev, fw)

    # Generated from packet 739/740
    cmd_57s(dev, '\x8C', "\x00\x00")

    # Generated from packet 743/744
    cmd_50(dev, "\x0D\x00")

    # Generated from packet 745/746
    buff = bulk2(dev,
                 "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00",
                 target=0x02)

    validate_read("\x96\x00", buff, "packet W: 745/746, R: 747/748")
    # Generated from packet 749/750
    buff = bulk2(dev, "\x02", target=0x06)

    validate_read("\x97\x00\xB0\x76\x09\x00", buff,
                  "packet W: 749/750, R: 751/752")

    # Generated from packet 753/754
    cmd_57_50(dev, "\x96", "\x1A\x00")

    # Generated from packet 755/756
    buff = bulk2(dev,
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00\x66\xB9\x00" \
        "\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        , target=0x02)

    validate_read("\x97\x00", buff, "packet W: 755/756, R: 757/758")

    # Generated from packet 759/760
    buff = bulk2(dev, "\x02", target=0x06)

    validate_read("\x98\x00\xD0\x76\x09\x00", buff,
                  "packet W: 759/760, R: 761/762")

    # Generated from packet 763/764
    buff = bulk2(dev, "\x57\x97\x00", target=0x02)

    validate_read("\x00\x00", buff, "packet W: 763/764, R: 765/766")

    # Generated from packet 767/768
    led_mask_30(dev, "pass")

    # Generated from packet 771/772
    cmd.gpio_readi(dev)

    # Generated from packet 775/776
    cmd.gpio_readi(dev)

    # Generated from packet 779/780
    #cmd.sm_info22(dev)
    # Generated from packet 783/784
    #cmd.sm_info24(dev)
    # Generated from packet 787/788
    #sm_info3(dev)
    # Generated from packet 791/792
    cmd_49(dev)
    # Generated from packet 795/796
    #sm_info3(dev)
    # Generated from packet 799/800
    sm_insert(dev)

    # Generated from packet 803/804
    sm_info10(dev)


class I87C51(bpmicro.device.Device):
    def __init__(self, dev, verbose=False):
        self.verbose = verbose
        self.dev = dev

    def read(self, opts):
        return dev_read(dev=self.dev,
                        cont=opts.get('cont', True),
                        verbose=opts.get('verbose', False))

    def program(self, devcfg, opts):
        dev_write(dev=self.dev,
                  devcfg=devcfg,
                  cont=opts.get('cont', True),
                  verbose=opts.get('verbose', False))
