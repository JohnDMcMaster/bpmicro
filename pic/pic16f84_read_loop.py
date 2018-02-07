from bpmicro import startup
from bpmicro import cmd
from bpmicro.util import hexdump, add_bool_arg
from bpmicro.pic16f84.read import replay

if __name__ == "__main__":
    import argparse 
    
    parser = argparse.ArgumentParser(description='Replay captured USB packets')
    add_bool_arg(parser, '--cycle', default=False, help='') 
    add_bool_arg(parser, '--cont', default=True, help='Continuity check') 
    args = parser.parse_args()

    if args.cycle:
        startup.cycle()

    bp = startup.get()

    while True:
        print
        print
        print
        try:
            (code, eeprom, config) = replay(bp.dev, cont=args.cont)
        except cmd.BusError:
            print 'WARNING: bus error'
            continue
        except cmd.Overcurrent:
            print 'WARNING: overcurrent'
            continue
        except cmd.ContFail:
            print 'WARNING: continuity fail'
            continue

        print
        hexdump(code, indent='  ', label='Code')

        print
        hexdump(eeprom, indent='  ', label='EEPROM')

        print
        print 'Fuses'
        for i in xrange(0, 4):
            print '  user_id%d:  0x%04X' % (i, config['user_id%d' % i])
        #print '  conf_word: 0x%04X' % (config['conf_word'])
        print '  secure: %s' % (config['secure'])
