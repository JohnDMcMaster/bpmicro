BP Microsystems open source driver
Developed against BP 1410


********************************************************************************
Why does this project exist?
********************************************************************************
I actually find BPWin to be pretty decent for simple tasks
However, I need to run some special analysis on a Linux system and need API level access
BPWin charges even for their Windows API, and I don't want to deal with GUI scripting
For most people you are probably better off using the vendor software
There are also some other Linux friendlier options today such as Linux minipro tools
However, BPM offers much better continuity, overcurrent, and other protections


********************************************************************************
Still reading? Okay!
********************************************************************************
It is unknown as of this writing how applicable the current code is to other models
It is suspected that part of the code could be refactored for parallel port support
(if someone generated equivilent traces)


********************************************************************************
Adding a new device
********************************************************************************
What you'll need:
-Linux host w/
    Virtualization software (I use VMWare player)
    Wireshark
-Windows guest w/
    BPWin software (I use 5.33.0)
-Device you want to support
-A pattern handy, such as what to write, or a known pattern on the device

Do the following to capture the packets:
-Host: start usbmon
-Host: start wireshark (root and/or usb permissions may be needed)
-Host: use lsusb to see which devices are present
-Turn on BP and plug into computer
-Host: use lsusb again and see which device is new. Note the USB bus number
-Host: start guest using your virtualization software
-Connect the USB device to the VM
-Host: run lsusb again. You should see that the device number has bumped by 1 (per fxload). Record this number
-Guest: start BPWin
-Guest: select a device you want to support and ensure device is in socket. Do a test read in BPWin if you like
-Host: start capture on the usb bus noted earlier
-Guest: run the operation you want to support (ie read)
-Host: stop capture
-Host: save capture. I name mine like "pic17c43_20187-02-10_02_read_cont-y-id-y.cap"
    That is: <device>_<date>_<capture#>_<operation>_<options>.cap

Decoding the capture
I use a script that looks something like this:
    function process() {
        base=$1
        id=$2
        usbrply --fx2 --device $id -j $base.cap >$base.json
        python ../../scrape.py $base.json >$base.py
        python ../../scrape.py --dumb $base.json >${base}_dumb.py
    }

    process pic17c43_20187-02-10_02_read_cont-y-id-y 6
Where 6 is the device number noted earlier
    If you didn't record this, open up the capture in Wireshark and look for relevant traffic
    If its the only device on the bus, this should be obvious
    If you have other devices (such as keyboard/mouse), look for the one with bulk traffic
Now:
-Run the script
    Note: some flags are set to drop various packets (such as read only commands)
    See scrape help for details
-Open the main .py (ie non-dumb) file
-Note: device support is typically composed of a functionality and firmware (fw) file
-Use an existing support file pair as a template for your device to support, renaming and copying into relevant architecture directory
    Ex: 8052, 8751, and at89c51 all go into mcs51 directory
    Create a new directory if needed (and make sure to add __init__.py file)
-Replace the firmware provided by your template with the generated firmware
-Rename the class to match your new device
-Replace the code provided with your remplate with the generated code
-Tweak import at top to have something like "import bpmicro.pic.pic17c43_fw as my_fw"
-Look at the firmware blobs for the one that is actually your firmware. Make this a code read like done in your template file
-Consider adding this firmware definition to scrape.py so its in its firwmare database
-Edit devs.py to add your device by adding import and adding to list
-Test by running a command like: python main.py read pic17c43
    Disconnect from vmware if you haven't already

