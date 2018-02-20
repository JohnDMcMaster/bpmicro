import time
import sys
import struct

from bpmicro.usb import usb_wraps
from bpmicro import startup
from bpmicro.cmd import bulk2
from bpmicro.usb import validate_read
from bpmicro import util
from bpmicro import cmd

def dexit():
    print 'Debug break'
    sys.exit(0)

def read_adcs(dev):
    bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)

    print 'NOTE: best guess'
    for name, (reg, sf) in cmd.adcs.iteritems():
        raw = cmd.read_adc_raw(dev, reg)
        scaled = raw * sf
        print '  %s (0x%02X): 0x%04X => %0.3f V' % (name, reg, raw, scaled)

def cleanup_adc(dev):
    _bulkRead, bulkWrite, _controlRead, _controlWrite = usb_wraps(dev)
    
    # Generated from packet 1220/1221
    bulkWrite(0x02, "\x50\x1A\x00\x00\x00")
    
    # Generated from packet 1222/1223
    buff = bulk2(dev,
            "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00\x66\xB9\x00"
            "\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00",
            target=2)
    validate_read("\x83\x00", buff, "packet 1224/1225")
    
    # Generated from packet 1226/1227
    buff = bulk2(dev, "\x02", target=6)
    validate_read("\x84\x00\x50\x01\x09\x00", buff, "packet 1228/1229")
    
    # Generated from packet 1230/1231
    buff = bulk2(dev, "\x57\x83\x00", target=2)
    validate_read("\x00\x00", buff, "packet 1232/1233")

if __name__ == "__main__":
    import argparse 
    
    parser = argparse.ArgumentParser(description='Replay captured USB packets')
    util.add_bool_arg(parser, '--loop', default=False, help='') 
    args = parser.parse_args()

    bp = startup.get()

    print
    print
    # didn't fix 17/18 issue
    #time.sleep(5)
    print
    
    if 1:
        import os

        try:
            while True:
                os.system('clear')
                read_adcs(bp.dev)
                if not args.loop:
                    break
                time.sleep(0.2)
        finally:
            print 'Cleaning up on exit'
            cleanup_adc(bp.dev)

    if 0:
        import curses
        import atexit
        
        @atexit.register
        def goodbye():
            """ Reset terminal from curses mode on exit """
            curses.nocbreak()
            if stdscr:
                stdscr.keypad(0)
            curses.echo()
            curses.endwin()        

        stdscr = curses.initscr()
        while True:
            stdscr.clear()
            read_adcs(bp.dev)
            time.sleep(0.2)
        
    print 'Complete'
