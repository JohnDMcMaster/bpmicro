from bpmicro import cmd
from bpmicro import util
from bpmicro import sockets

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Dump device data')
    util.add_bool_arg(parser,
                      '--verbose',
                      default=True,
                      help='Print hex dumps')
    parser.add_argument('fin', default=None, help='File in')
    args = parser.parse_args()

    sm = cmd.sm_decode(open(args.fin).read())
    if args.verbose:
        util.print_mkstruct(sm)
    else:
        util.print_mkstruct(
            sm, filter=lambda k, v: 'pad' not in k and 'unk' not in k)

    name_expect = sockets.name_i2s.get(sm.sockid, None)
    if name_expect is None:
        print('Note: unknown socket type %s' % sm.sockid)
    elif name_expect != sm.name:
        print('WARNING: expected name %s but got %s' % (name_expect, sm.name))
