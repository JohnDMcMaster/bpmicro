from bpmicro import startup
from bpmicro import cmd
from bpmicro import util

import argparse
import binascii
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dump device data')
    util.add_bool_arg(parser, '--verbose', default=True, help='Print hex dumps')
    util.add_bool_arg(parser, '--save', default=True, help='Save dump')
    parser.add_argument('dout', nargs='?', default=None, help='File out')
    args = parser.parse_args()

    bp = startup.get()
    sn = cmd.sn_read(bp.dev)

    dout = None
    if args.save:
        if args.dout:
            dout = args.dout
        else:
            if not os.path.exists('dump'):
                os.mkdir('dump')
            i = 0
            while True:
                dout = 'dump/' + str(sn)
                if i:
                    dout += '.' + str(i)
                if not os.path.exists(dout):
                    break
                i += 1
        print 'Writing to %s' % dout
        if not os.path.exists(dout):
            os.mkdir(dout)
        _t = util.IOLog(out_fn=os.path.join(dout, 'out.txt'))

    print
    print 'S/N: %s' % sn
    sn_buff = cmd.sn_r(bp.dev)
    if args.verbose:
        util.hexdump(sn_buff)
    if args.save:
        open(os.path.join(dout, 'sn.bin'), 'w').write(sn_buff)

    print
    print 'Status structure'
    status_struct = cmd.cmd_01r(bp.dev, validate=False)
    if args.verbose:
        util.hexdump(status_struct, indent='')
    if args.save:
        open(os.path.join(dout, 'status.bin'), 'w').write(status_struct)

    print
    print 'cmd_49: %s' % binascii.hexlify(cmd.cmd_49(bp.dev))

    # mask doesn't effect
    #cmd.led_mask(bp.dev, 7)
    print
    gpio = cmd.gpio_readi(bp.dev)
    print 'GPIO: 0x%02X' % gpio
    print '  SM inserted: %d' % (cmd.sm_is_inserted(gpio))

    print
    print 'Socket module (SM)'
    if cmd.sm_is_inserted(gpio):
        #cmd.sm_insert(bp.dev)
        #info1 = cmd.sm_info1(bp.dev)

        sm_eeprom = cmd.sm_r(bp.dev, 0x00, 0x3F)
        sm = cmd.sm_decode(sm_eeprom)
        cmd.print_mkstruct(sm, filter=lambda k, v: 'pad' not in k and 'unk' not in k)

        if args.verbose:
            util.hexdump(sm_eeprom)
        if args.save:
            open(os.path.join(dout, 'sm_eeprom_%s.bin' % sm.name), 'w').write(sm_eeprom)
    
        print 'Alternate command'
        sm2_eeprom = cmd.cmd_sm_0e02(bp.dev)
        if args.verbose:
            util.hexdump(sm2_eeprom)
        if args.save:
            open(os.path.join(dout, 'sm_eeprom2_%s.bin' % sm.name), 'w').write(sm2_eeprom)
    else:
        print 'SM not inserted'


    print
    print 'Technology adapter (TA)'
    ta_eeprom = cmd.ta_r(bp.dev, 0x00, 0x3F)
    if args.verbose:
        util.hexdump(ta_eeprom)
    if args.save:
        open(os.path.join(dout, 'ta_eeprom.bin'), 'w').write(ta_eeprom)