from bpmicro import startup
from bpmicro import cmd
from bpmicro.util import add_bool_arg

led_s2i = {
            'fail': 1,
            'active': 2,
            'pass': 4,
            'red': 1,
            'orange': 2,
            'green': 4,
            }

if __name__ == "__main__":
    import argparse 
    
    parser = argparse.ArgumentParser(description='Control LED')
    add_bool_arg(parser, '--cycle', default=False, help='') 
    parser.add_argument('status', help='String value or 0-7 direct mask, 1: fail, 2: active, 4: pass')
    args = parser.parse_args()

    try:
        status = int(args.status, 0)
    except ValueError:
        try:
            status = led_s2i[args.status]
        except KeyError:
            raise Exception("Bad status value %s" % args.status)

    bp = startup.get()
    cmd.led_mask(bp.dev, status)
