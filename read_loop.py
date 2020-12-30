#!/usr/bin/env python
from bpmicro import startup
from bpmicro import cmd
from bpmicro.util import hexdump, add_bool_arg
from bpmicro import devices
import os
import json
import binascii
import hashlib


def buff2hash8(buff):
    return binascii.hexlify(hashlib.md5(buff).digest())[0:8]


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Replay captured USB packets')
    add_bool_arg(parser, '--cycle', default=False, help='')
    add_bool_arg(parser, '--cont', default=True, help='Continuity check')
    parser.add_argument('device')
    parser.add_argument('out_dir', nargs='?')
    args = parser.parse_args()

    verbose = True
    bp = startup.get()
    device = devices.get(bp, args.device, verbose=verbose)

    if args.out_dir and not os.path.exists(args.out_dir):
        os.mkdir(args.out_dir)

    itern = 0
    while True:
        itern += 1
        prefix = os.path.join(args.out_dir, "%03u" % itern)
        print("")
        print("")
        print("")
        try:
            devcfg = device.read({'cont': args.cont})
        except cmd.BusError:
            print('WARNING: bus error')
            continue
        except cmd.Overcurrent:
            print('WARNING: overcurrent')
            continue
        except cmd.ContFail:
            print('WARNING: continuity fail')
            continue

        print("")
        hexdump(devcfg['code'], indent='  ', label='Code')
        hexdump(devcfg['code'][0:0x40], indent='  ', label='Code start')
        print((buff2hash8(devcfg['code'])))
        if args.out_dir:
            open(prefix + "_code.bin", "wb").write(devcfg['code'])

        if 'data' in devcfg:
            print("")
            hexdump(devcfg['data'], indent='  ', label='EEPROM')
            if args.out_dir:
                open(prefix + "_data.bin", "wb").write(devcfg['data'])

        if 'config' in devcfg:
            print("")
            print('Fuses')
            config = devcfg['config']
            for i in range(0, 4):
                print(('  user_id%d:  0x%04X' % (i, config['user_id%d' % i])))
            #print '  conf_word: 0x%04X' % (config['conf_word'])
            print(('  secure: %s' % (config['secure'])))
            if args.out_dir:
                open(prefix + "_config.json", "w").write(
                    json.dumps(devcfg['config'],
                               sort_keys=True,
                               indent=4,
                               separators=(',', ': ')))


if __name__ == "__main__":
    main()
