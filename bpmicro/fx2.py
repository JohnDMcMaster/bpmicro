import time
from bpmicro.usb import usb_wraps
from bpmicro import fw


def load_fx2(dev):
    _bulkRead, _bulkWrite, _controlRead, controlWrite = usb_wraps(dev)

    # FX2_REG_W (0xA0): addr=0xE600 (CPUCS), reset: hold
    controlWrite(0x40, 0xA0, 0xE600, 0x0000, "\x01")

    # FX2_REG_W (0xA0): addr=0x0000 (FW load)
    controlWrite(0x40, 0xA0, 0x0000, 0x0000, fw.hash2bin["6cda05c6"])
    # FX2_REG_W (0xA0): addr=0x03FF (FW load)
    controlWrite(0x40, 0xA0, 0x03FF, 0x0000, fw.hash2bin["68309a90"])
    # FX2_REG_W (0xA0): addr=0x07FE (FW load)
    controlWrite(0x40, 0xA0, 0x07FE, 0x0000, fw.hash2bin["2faed3c2"])
    # FX2_REG_W (0xA0): addr=0x0BFD (FW load)
    controlWrite(0x40, 0xA0, 0x0BFD, 0x0000, fw.hash2bin["950acc1c"])

    # FX2_REG_W (0xA0): addr=0xE600 (CPUCS), reset: release
    controlWrite(0x40, 0xA0, 0xE600, 0x0000, "\x00")
