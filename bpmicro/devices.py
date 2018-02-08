from mcs51 import i87c51
from pic import pic16f84

class_s2c = {
    'i87c51': i87c51.I87C51,
    'pic16f84': pic16f84.PIC16F84,
    }

def get(bp, device):
    try:
        c = class_s2c[device]
    except KeyError:
        raise Exception("Unsupported device %s" % device)
    return c(bp.dev)
