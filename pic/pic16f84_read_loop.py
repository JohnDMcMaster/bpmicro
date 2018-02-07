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
            fw_in = replay(bp.dev, cont=args.cont)
        except cmd.BusError:
            print 'WARNING: bus error'
            continue
        except cmd.Overcurrent:
            print 'WARNING: overcurrent'
            continue
        hexdump(fw_in, indent='  ', label='Read data')
        print 'Bytes: %d 0x%04X' % (len(fw_in), len(fw_in))
