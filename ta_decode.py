from bpmicro import cmd
from bpmicro import util

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Dump device data')
    util.add_bool_arg(parser, '--verbose', default=True, help='Print hex dumps')
    parser.add_argument('fin', default=None, help='File in')
    args = parser.parse_args()

    sm = cmd.ta_decode(open(args.fin).read())
    if args.verbose:
        util.print_mkstruct(sm)
    else:
        util.print_mkstruct(sm, filter=lambda k, v: 'pad' not in k and 'unk' not in k)
