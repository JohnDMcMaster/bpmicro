from bpmicro.usb import usb_wraps, validate_read
from bpmicro import cmd
from bpmicro import fw


def boot_cold(dev):
    bulkRead, bulkWrite, controlRead, _controlWrite = usb_wraps(dev)

    buff = cmd.bulk2(
        dev, "\x43\x19\x00\x00\x00\x3B\x66\x1B\x00\x00\xFE\xFF\x3B\x64\x1B\x00"
        "\x00\xFE\xFF\x00",
        target=2)
    validate_read("\xA4\x06", buff, "packet 72/73")

    # Atomic
    #cmd.cmd_01 state: 0x80 => 0x81
    bulkWrite(0x02, cmd.cmd_43_mk("\x00") + cmd.cmd_11_mk())
    bulkWrite(0x02, fw.hash2bin["0232b379"])
    bulkWrite(0x02, fw.hash2bin["a7292c41"])
    bulkWrite(0x02, fw.hash2bin["ce6f13bd"])
    bulkWrite(0x02, fw.hash2bin["4398af9b"])
    bulkWrite(0x02, fw.hash2bin["250c94c4"])
    buff = cmd.bulk2(dev, "\x5A", target=1)
    validate_read("\x80", buff, "packet 92/93")

    # Atomic
    #cmd.cmd_01 state: 0x81 => 0x82
    bulkWrite(0x02, "\x11\x10\x00")
    bulkWrite(
        0x02,
        "\xEA\xCC\x64\x01\x00\x08\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x3F")
    buff = cmd.bulk2(dev, "\xA6", target=1)
    validate_read("\x81", buff, "packet 100/101")

    # Atomic
    #cmd.cmd_01 state: 0x82 => 0x83
    bulkWrite(0x02, "\x11\x4E\x00")
    bulkWrite(
        0x02,
        "\xE8\x00\x00\x00\x00\xFA\x5A\x83\xEA\x05\x81\xEA\x00\x00\x01\x00"
        "\x81\xFA\x00\x00\x01\x00\x74\x1F\xBB\x00\x00\x00\x00\xB9\x00\x00"
        "\x01\x00\x66\x8B\x02\x66\x89\x83\x00\x00\x01\x00\x83\xC2\x02\x83"
        "\xC3\x02\x83\xE9\x02\x75\xEB\x8C\xC8\x50\xB8\xF0\xFF\x01\x00\x50"
        "\x0F\x20\xC0\x0D\x00\x00\x00\x60\x0F\x22\xC0\x0F\x09\xC3")
    buff = cmd.bulk2(dev, "\xDB", target=1)
    validate_read("\x82", buff, "packet 108/109")

    #cmd.cmd_01 state: 0x83 => 0x80.  Length 129 => 133
    # Generated from packet 110/111
    buff = cmd.bulk2(dev, "\x82", target=1)
    validate_read("\x16", buff, "packet 112/113")


def boot_warm(dev):
    # Generated from packet 70/71
    buff = cmd.bulk2(
        dev, "\x43\x19\x00\x00\x00\x3B\x7E\x25\x00\x00\xFE\xFF\x3B\x7C\x25\x00"
        "\x00\xFE\xFF\x00",
        target=2)
    validate_read("\xA4\x06", buff, "packet 72/73")

    # Generated from packet 74/75
    #cmd.cmd_01(dev)


def init_dev(dev, verbose=False):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)

    # bp1410 init signature
    #validate_read("\x08\x16\x01\x00", devsig, "packet 57/58")

    buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
    validate_read("\x00\x00\x00", buff, "packet 62/63")

    buff = bulkRead(0x86, 0x0200)
    validate_read("\x08\x16\x01\x00", buff, "packet 64/65")

    buff = bytearray(cmd.cmd_01(dev))
    # Seems to be okay if we always do this although its only sometimes needed
    glitch_154 = True
    # All of these are the same except for the state byte
    # maybe varies depending if SM installed
    if len(buff) == 129:
        if verbose:
            print('Boot: cold')
        state = buff[0x13]
        if state != 0x80 and verbose:
            print(('  WARNING: state: 0x%02X.  Interrupted load?' % state))
        # 70-117
        boot_cold(dev)
    elif len(buff) == 133:
        if verbose:
            print('Boot: warm')
        # 70-76
        boot_warm(dev)
    # elif buff == r01_glitch_154:
    #     print 'Warm boot (glitch)'
    #     glitch_154 = True
    #     # 70-76
    #     boot_warm(dev)
    else:
        raise Exception("Bad warm/cold response")

    # Packets going forward are from cold boot since its more canonical / clean
    # warm -40 packet (ie 120 cold => 80 warm)

    buff = cmd.bulk2(
        dev, "\x14\x38\x25\x00\x00\x04\x00\x90\x32\x90\x00\xA7\x02\x1F\x00\x14"
        "\x40\x25\x00\x00\x01\x00\x3C\x36\x0E\x01",
        target=0x20)
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00"
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E"
        "\x2C", buff, "packet 124/125")

    bulkWrite(0x02, "\x43\x19\x00\x00\x00")
    bulkWrite(0x02, "\x20\x01\x00\x0C\x04")
    bulkWrite(0x02, "\x41\x00\x00")

    # Generated from packet 148/149
    #cmd.cmd_01[0x17]: 0x00 => 0x09
    # warm: als state 0x83 => 0x80, 0x15: 0x30 => 0x00, 016: 0x01 => 0x00
    buff = cmd.bulk2(dev, "\x10\x80\x02", target=6)
    validate_read("\x80\x00\x00\x00\x09\x00", buff, "packet 150/151")

    buff = cmd.bulk2(dev, "\x45\x01\x00\x00\x31\x00\x06", target=0x64)
    validate_read(
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        "\xFF\xFF\xFF\xFF\xFF", buff, "packet 154/155")

    cmd.cmd_49(dev)
    bulkWrite(
        0x02,
        "\x3B\x0C\x22\x00\xC0\x30\x00\x3B\x0E\x22\x00\xC0\x00\x00\x3B\x1A"
        "\x22\x00\xC0\x18\x00")
    buff = cmd.bulk2(dev, "\x4A\x03\x00\x00\x00", target=2)
    validate_read("\x03\x00", buff, "packet 176/177")

    # Atomic
    # Generated from packet 178/179
    bulkWrite(0x02, "\x4C\x00\x02")
    # Generated from packet 180/181
    # None (0xB2)
    controlWrite(0x40, 0xB2, 0x0000, 0x0000, "")

    # Atomic
    cmd.cmd_50(dev, "\x45\x00")
    # FIXME: size field unexpected
    buff = cmd.bulk2(
        dev, "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x10"
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x80"
        "\xE9\x02\x00\x00\x00\x90\x00\xE9\x04\x00\x00\x00\x00\x00\x00\x00"
        "\xE9\x03\x00\x00\x00\x90\x00\x00\x66\xB9\x00\x00\xB2\x00\xFB\xFF"
        "\x25\x44\x11\x00\x00",
        target=2)
    validate_read("\x80\x00", buff, "packet 186/187")

    #cmd.cmd_01[0x15]: 0x00 => 0x50
    cmd.cmd_02(dev, "\x81\x00\x50\x00\x09\x00", "packet 190/191")

    # Atomic
    #cmd.cmd_01 state: 0x81 => 0x82
    cmd.cmd_50(dev, "\xC0\x00")
    buff = cmd.bulk2(
        dev, "\x66\xB8\x01\x2D\x81\xE3\xFF\xFF\x00\x00\x66\xBB\x18\x00\x66\xC7"
        "\x05\x30\x40\x00\xC0\xF0\xFF\x89\xD9\xC1\xE1\x02\x66\xC7\x81\x02"
        "\x00\x00\x00\xF0\xFF\x66\x03\x05\xE4\x46\x00\x00\x66\x89\x05\x90"
        "\x40\x00\xC0\x89\xDA\x81\xCA\x00\x80\x00\x00\x66\x89\x15\x50\x40"
        "\x00\xC0\xC6\x05\x14\x22\x00\xC0\x7B\x81\xCA\x00\x40\x00\x00\x66"
        "\x89\x15\x50\x40\x00\xC0\x89\xD9\x66\xC1\xE1\x02\x66\x89\x81\x00"
        "\x00\x00\x00\x66\x2B\x05\xE4\x46\x00\x00\xC6\x05\x14\x22\x00\xC0"
        "\xBB\x81\xCB\x00\x80\x00\x00\x66\x89\x1D\x50\x40\x00\xC0\x89\xC2"
        "\x81\xE2\x07\x00\x00\x00\x03\xD2\x81\xCA\x01\x00\x00\x00\x89\xD9"
        "\x81\xE1\x03\x00\x00\x00\xD3\xE2\xD3\xE2\xD3\xE2\xD3\xE2\xD3\xE2"
        "\xC1\xE2\x0A\x89\xD9\x81\xE1\xFC\x03\x00\x00\x09\xCA\x88\x82\x00"
        "\x00\x00\x40\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00",
        target=2)
    validate_read("\x81\x00", buff, "packet 196/197")

    #cmd.cmd_01: 0x15: 0x50 => 0x01.  0x16: 0x00 => 0x01
    # Generated from packet 198/199
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00", "packet 200/201")

    if glitch_154:
        buff = cmd.bulk2(
            dev,
            "\x08\x20\x09\x20\x0A\x20\x0B\x20\x57\x81\x00\x0C\x04\x30",
            target=2)
        validate_read("\x04\x00", buff, "packet 204/205")
    else:
        # Think this clears the red light
        # Generated from packet 202/203
        buff = cmd.bulk2(
            dev,
            "\x04\x72\x05\x73\x06\x2E\x07\x70\x08\x75\x09\x73\x0A\x68\x0B\x28"
            "\x57\x81\x00\x0C\x04\x30",
            target=2)
        validate_read("\x04\x00", buff, "packet 204/205")

    buff = cmd.bulk2(
        dev, "\x3B\x0C\x22\x00\xC0\x30\x00\x3B\x0E\x22\x00\xC0\x00\x00\x3B\x1A"
        "\x22\x00\xC0\x18\x00\x0E\x01",
        target=0x20)
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00"
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E"
        "\x2C", buff, "packet 208/209")

    # Atomic
    #cmd.cmd_01 state: 0x82 => 0x83
    bulkWrite(0x02, "\x48\x00\x20\x00\x00\x50\x12\x00\x00\x00")
    buff = cmd.bulk2(
        dev, "\x00\x00\x00\x00\x04\x00\x08\x00\x0C\x00\x10\x00\x14\x00\x18\x00"
        "\x1C\x00",
        target=2)
    validate_read("\x82\x00", buff, "packet 226/227")

    cmd.cmd_02(dev, "\x83\x00\x30\x01\x09\x00", "packet 230/231")

    #cmd.cmd_01: 0x15: 0x10 => 0x30
    buff = cmd.bulk2(
        dev, "\x1D\x10\x01\x09\x00\x00\x00\x15\x60\x00\x00\x00\x00\x00\x00\x00"
        "\x00\x00\x00\x00\x00\x00\x1C\x00\x00\x48\x00\x12\xAA",
        target=1)
    validate_read("\xAB", buff, "packet 234/235")
