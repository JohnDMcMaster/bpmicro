from bpmicro import startup
from bpmicro import cmd
from bpmicro.util import hexdump, add_bool_arg
from bpmicro import devices

def main():
    import argparse 
    
    parser = argparse.ArgumentParser(description='Replay captured USB packets')
    add_bool_arg(parser, '--cycle', default=False, help='') 
    add_bool_arg(parser, '--cont', default=True, help='Continuity check') 
    parser.add_argument('device') 
    args = parser.parse_args()

    if args.cycle:
        startup.cycle()

    verbose = True
    bp = startup.get()
    device = devices.get(bp, args.device, verbose=verbose)

    while True:
        print
        print
        print
        try:
            devcfg = device.read({'cont': args.cont})
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
        hexdump(devcfg['code'], indent='  ', label='Code')

        if 'data' in devcfg:
            print
            hexdump(devcfg['data'], indent='  ', label='EEPROM')

        if 'config' in devcfg:
            print
            print 'Fuses'
            config = devcfg['config']
            for i in xrange(0, 4):
                print '  user_id%d:  0x%04X' % (i, config['user_id%d' % i])
            #print '  conf_word: 0x%04X' % (config['conf_word'])
            print '  secure: %s' % (config['secure'])

if __name__ == "__main__":
    main()
