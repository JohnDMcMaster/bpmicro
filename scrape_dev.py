from bpmicro.util import str2hex

import json
import binascii
import subprocess
import os
import sys

from bpmicro.cmd import led_i2s
from bpmicro.util import hexdump
from bpmicro.util import add_bool_arg
from bpmicro import fw

import scrape
from scrape import line, inc_indent, dec_indent

import usbrply.parsers


# hack: new firmwares disabled due to args stuff
class Scraper(scrape.Scraper):
    def __init__(self):
        scrape.Scraper.__init__(self)
        self.found_ret = False

    def file_prefix(self):
        line('# Generated from scrape_dev.py')
        line('from bpmicro.cmd import bulk2, bulk86')
        line('from bpmicro import cmd')
        line('from bpmicro.usb import usb_wraps')
        line('from bpmicro.usb import validate_read')
        line('from bpmicro import fw')
        line('import bpmicro.device')
        line('import usb1')
        line('')
        line('def dev_read(dev, cont, verbose=False):')
        inc_indent()
        line("bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)")
        line('')

    def file_postfix(self):
        print('''
class Device(bpmicro.device.Device):
    def __init__(self, dev, verbose=False):
        self.verbose = verbose
        self.dev = dev

    def read(self, opts):
        return dev_read(dev=self.dev, cont=opts.get('cont', True), verbose=opts.get('verbose', False))
        ''')

    def loop_postfix(self):
        assert self.found_ret
        line("return {\"code\": fw_in}")

    def check_bulk2(self, cmd):
        # FIXME: hook buffer read
        # self.found_ret = True
        if cmd == "\x08\x00\x57\x8A\x00":
            line("fw_in = buff")
            self.found_ret = True
        else:
            return True

if __name__ == "__main__":
    import argparse 
    
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--dumb', action='store_true')
    add_bool_arg(parser, '--omit-ro', default=True, help='Omit read only requests (ex: get SM info)')
    parser.add_argument('--big-thresh', type=int, default=255)
    parser.add_argument('--usbrply', default='')
    parser.add_argument('--save', action='store_true', help='Save firmware')
    parser.add_argument('-w', action='store_true', help='Write python file')
    parser.add_argument('fin')
    args = parser.parse_args()

    j, json_fn = scrape.load_json(args.fin)
    # j = usbrply.parsers.pcap2json(args)

    if args.w:
        filename, file_extension = os.path.splitext(args.fin)
        fnout = filename + '.py'
        print('Selected output file %s' % fnout)
        assert fnout != args.fin and fnout != json_fn
        scrape.fout = open(fnout, 'w')

    dumb = args.dumb
    omit_ro = args.omit_ro
    scraper = Scraper()
    scraper.dump(j, save=args.save)
