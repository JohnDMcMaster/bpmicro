from mcs51 import i87c51
from pic import pic16c554, pic17c43
from pic import pic16f84
from mcs51 import at89c51

class_s2c = {
    'i87c51': i87c51.I87C51,
    'pic16c554': pic16c554.PIC16C554,
    'pic17c43': pic17c43.PIC17C43,
    'pic16f84': pic16f84.PIC16F84,
    'at89c51': at89c51.AT89C51,
    }

def get(bp, device, verbose=False):
    try:
        c = class_s2c[device]
    except KeyError:
        raise Exception("Unsupported device %s" % device)
    return c(bp.dev, verbose=verbose)
