# Atomic: indicates commands must be executed in sequence
# trying to insert debugging commands likecmd.cmd_01() fail
        
import fx2
import bp1410
import bp1600
import cmd
import time
import binascii
from usb import usb_wraps, validate_read, USBAdapt

import usb1

# BP1600 POST slightly over 10 seconds
def wait_post(dev, timeout=15.0):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)

    tstart = time.time()
    printed = False
    while True:
        if time.time() - tstart > timeout:
            raise Exception("Timeout waiting for POST")
        buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
        if buff == "\x00\x00\x00":
            break
        if not printed:
            print("POST: waiting")
            printed = True
        if buff != "\x01\xFF\x00":
            print('WARNING: unexpected POST status: %s' % binascii.hexlify(buff))
        time.sleep(0.05)
    if printed:
        print('POST: ok after %0.1f sec' % (time.time() - tstart))

def init_adapter(dev):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)

    fx2.load_fx2(dev)
    wait_post(dev)

    buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
    validate_read("\x00\x00\x00", buff, "packet 641/642")

    # buff = bulkRead(0x86, 0x0200)
    _prefix, buff, _size = cmd.bulk86_next_read(dev)
    return str(buff)

def init_dev(dev, verbose=False):
    devsig = init_adapter(dev)
    init_dev = {
        "\x08\x16\x01\x00": bp1410.init_dev,
        "\x16":             bp1600.init_dev,
        }[devsig]

    init_dev = bp1410.init_dev
    init_dev(dev, verbose=verbose)

def open_dev(usbcontext=None, verbose=False):
    if usbcontext is None:
        usbcontext = usb1.USBContext()

    if verbose:
        print 'Scanning for devices...'
    for udev in usbcontext.getDeviceList(skip_on_error=True):
        vid = udev.getVendorID()
        pid = udev.getProductID()
        if (vid, pid) == (0x14b9, 0x0001):
            if verbose:
                print 'Found: Bus %03i Device %03i: ID %04x:%04x' % (
                        udev.getBusNumber(), udev.getDeviceAddress(),
                        vid, pid)
            return udev.open()
    raise Exception("Failed to find a device")

def get(init=True, verbose=False):
    '''Connect to USB device and return a BP1410 object'''
    usbcontext = usb1.USBContext()
    dev = open_dev(usbcontext, verbose=verbose)
    dev.claimInterface(0)
    if init:
        init_dev(dev, verbose=verbose)
    return USBAdapt(dev, usbcontext, verbose=verbose)
