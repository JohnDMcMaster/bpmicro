from bpmicro import startup
from bpmicro.util import hexdump, add_bool_arg
from bpmicro.pic16f84.read import replay

if __name__ == "__main__":
    import argparse 
    
    parser = argparse.ArgumentParser(description='Replay captured USB packets')
    add_bool_arg(parser, '--cycle', default=False, help='') 
    add_bool_arg(parser, '--cont', default=True, help='Continuity check') 
    parser.add_argument('fout', nargs='?', help='Output file') 
    args = parser.parse_args()

    if args.cycle:
        startup.cycle()

    bp = startup.get()

    (code, eeprom, config) = replay(bp.dev, cont=args.cont)
    if args.fout:
        print 'Writing to %s' % args.fout
        open(args.fout, 'w').write(code)
    else:
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

    print 'Complete'
