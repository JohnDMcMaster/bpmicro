from bpmicro import startup
from bpmicro import cmd
from bpmicro.util import add_bool_arg, hexdump

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Control LED')
    args = parser.parse_args()

    bp = startup.get()
    print('Ready')
    #cmd.sn_read(bp.dev)

    print()
    print('Status structure')
    buff = cmd.cmd_01r(bp.dev, validate=False)
    hexdump(buff, indent='  ')

    # mask doesn't effect
    #cmd.led_mask(bp.dev, 7)
    print()
    gpio = cmd.gpio_readi(bp.dev)
    print('GPIO: 0x%02X' % gpio)
    print('  SM inserted: %d' % (cmd.sm_is_inserted(gpio)))

    print()
    print('Socket module')
    if cmd.sm_is_inserted(gpio):
        cmd.sm_insert(bp.dev)
        cmd.sm_info1(bp.dev)
        hexdump(cmd.sm_r(bp.dev, 0x00, 0x3F), label="SM", indent='  ')
    else:
        print('SM not inserted')

    print()
    print('Peripheral memory')
    hexdump(cmd.ta_r(bp.dev, 0x00, 0x3F), label="TA", indent='  ')
