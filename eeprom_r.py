from bpmicro import startup
from bpmicro import cmd

import binascii

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Display EEPROM')
    args = parser.parse_args()

    bp = startup.get()
    print binascii.hexlify(cmd.sm_r(0, 32))
    print binascii.hexlify(cmd.ta_r(0, 32))
