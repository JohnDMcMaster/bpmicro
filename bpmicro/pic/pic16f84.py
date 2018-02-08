# Based off of 17_read-cont-y_cold.cap
# md5 0fdb988186be94a062adc9d1c0019463

from bpmicro import cmd
from bpmicro import util
from bpmicro.usb import validate_read
from bpmicro.usb import usb_wraps
from bpmicro.bp1410_fw import load_fx2
import pic16f84_fw
import bpmicro.device

import binascii
import struct
import time

def my_cmd_57s(dev):
    ret = bytearray()
    for dati in xrange(0x40):
        if dati == 0:
            # Generated from packet 2075/2076
            this = cmd.cmd_57s(dev, "\x94", None)
        else:
            # Generated from packet 2079/2080
            # ...
            # Generated from packet 2327/2328
            this = cmd.cmd_57s(dev, "\x92\x94", None)
        # Convert little to big endian?
        # no the data buff will be anyway
        #ret += this[1] + this[0]
        ret += this

    # Generated from packet 2331/2332
    cmd.cmd_57s(dev, "\x92\x8D", "\x00\x00")

    return ret

def dev_read(dev, cont=False, verbose=False):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)
    config = {}

    # Generated from packet 1273/1274
    # Unexpected SM read
    buff = cmd.bulk2b(dev, "\x22\x02\x25\x00\x25\x00\x06")
    validate_read("\x00\x00", buff, "packet W: 1273/1274, R 1 to 1275/1276")

    # Generated from packet 1643/1644
    # NOTE:: req max 4096 but got 3
    buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
    # Req: 4096, got: 3
    validate_read("\x00\x00\x00", buff, "packet 1643/1644")
    # Generated from packet 1645/1646
    _prefix, buff, _size = cmd.bulk86_next_read(dev)
    validate_read("\x16", buff, "packet 1645/1646")
    # NOTE:: req max 512 but got 4
    # Generated from packet 1647/1648
    #cmd.cmd_01(dev)
    # NOTE:: req max 512 but got 136
    # Generated from packet 1651/1652
    buff = cmd.bulk2b(dev, 
        "\x43\x19\x08\x00\x00\x3B\x7E\x25\x00\x00\xFE\xFF\x3B\x7C\x25\x00" \
        "\x00\xFE\xFF\x00"
        )
    validate_read("\xA4\x06", buff, "packet W: 1651/1652, R 1 to 1653/1654")
    # NOTE:: req max 512 but got 5
    # Generated from packet 1655/1656
    #cmd.cmd_01(dev)
    # NOTE:: req max 512 but got 136
    # Generated from packet 1659/1660
    #cmd.sn_read(dev)

    # Technology adapter info
    if 0:
        # NOTE:: req max 512 but got 35
        # Generated from packet 1663/1664
        buff = cmd.bulk2b(dev, 
            "\x14\x38\x25\x00\x00\x04\x00\x90\x32\x90\x00\xA7\x02\x1F\x00\x14" \
            "\x40\x25\x00\x00\x01\x00\x3C\x36\x0E\x01"
            )
        validate_read(
            "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
            "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
            , buff, "packet W: 1663/1664, R 1 to 1665/1666")
    
    # NOTE:: req max 512 but got 35
    # Generated from packet 1667/1668
    #cmd.gpio_readi(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 1671/1672
    #cmd.gpio_readi(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 1675/1676
    #cmd.sm_info22(dev)
    # NOTE:: req max 512 but got 7
    # Generated from packet 1679/1680
    #cmd.sm_info24(dev)
    # NOTE:: req max 512 but got 7
    # Generated from packet 1683/1684
    #cmd.sm_read(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 1687/1688
    #cmd.cmd_01(dev)
    # NOTE:: req max 512 but got 136
    # Generated from packet 1691/1692
    bulkWrite(0x02, "\x43\x19\x08\x00\x00")
    # Generated from packet 1693/1694
    bulkWrite(0x02, "\x20\x01\x00\x0C\x04")
    # Generated from packet 1695/1696
    cmd.cmd_41(dev)
    # Generated from packet 1697/1698
    cmd.cmd_10(dev)
    # NOTE:: req max 512 but got 9
    # Generated from packet 1701/1702
    #cmd.sm_read(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 1705/1706
    #cmd.sm_insert(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 1709/1710
    cmd.cmd_45(dev)
    # NOTE:: req max 512 but got 103
    # Generated from packet 1713/1714
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 1717/1718
    #cmd.gpio_readi(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 1721/1722
    #cmd.gpio_readi(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 1725/1726
    #cmd.sm_info22(dev)
    # NOTE:: req max 512 but got 7
    # Generated from packet 1729/1730
    #cmd.sm_info24(dev)
    # NOTE:: req max 512 but got 7
    # Generated from packet 1733/1734
    #cmd.sm_read(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 1737/1738
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 1741/1742
    #cmd.sm_read(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 1745/1746
    #cmd.sm_insert(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 1749/1750
    #cmd.sm_info10(dev)
    # NOTE:: req max 512 but got 11
    # Generated from packet 1753/1754
    cmd.cmd_3B(dev)
    # Generated from packet 1755/1756
    cmd.cmd_4A(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 1759/1760
    cmd.cmd_4C(dev)
    # Generated from packet 1761/1762
    buff = controlWrite(0x40, 0xB2, 0x0000, 0x0000, "")
    # Generated from packet 1763/1764
    cmd.cmd_50(dev, "\x4D\x00")
    # Generated from packet 1765/1766
    buff = cmd.bulk2b(dev, 
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x10" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x80" \
        "\xE9\x02\x00\x00\x00\x90\x00\xE9\x04\x00\x00\x00\x00\x00\x00\x00" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x80\x00", buff, "packet W: 1765/1766, R 1 to 1767/1768")
    # Generated from packet 1769/1770
    cmd.cmd_02(dev, "\x81\x00\x50\x00\x09\x00")
    # Generated from packet 1773/1774
    cmd.cmd_50(dev, "\xC0\x00")
    # Generated from packet 1775/1776
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x2D\x81\xE3\xFF\xFF\x00\x00\x66\xBB\x18\x00\x66\xC7" \
        "\x05\x30\x40\x00\xC0\xF0\xFF\x89\xD9\xC1\xE1\x02\x66\xC7\x81\x02" \
        "\x00\x00\x00\xF0\xFF\x66\x03\x05\xE4\x46\x00\x00\x66\x89\x05\x90" \
        "\x40\x00\xC0\x89\xDA\x81\xCA\x00\x80\x00\x00\x66\x89\x15\x50\x40" \
        "\x00\xC0\xC6\x05\x14\x22\x00\xC0\x7B\x81\xCA\x00\x40\x00\x00\x66" \
        "\x89\x15\x50\x40\x00\xC0\x89\xD9\x66\xC1\xE1\x02\x66\x89\x81\x00" \
        "\x00\x00\x00\x66\x2B\x05\xE4\x46\x00\x00\xC6\x05\x14\x22\x00\xC0" \
        "\xBB\x81\xCB\x00\x80\x00\x00\x66\x89\x1D\x50\x40\x00\xC0\x89\xC2" \
        "\x81\xE2\x07\x00\x00\x00\x03\xD2\x81\xCA\x01\x00\x00\x00\x89\xD9" \
        "\x81\xE1\x03\x00\x00\x00\xD3\xE2\xD3\xE2\xD3\xE2\xD3\xE2\xD3\xE2" \
        "\xC1\xE2\x0A\x89\xD9\x81\xE1\xFC\x03\x00\x00\x09\xCA\x88\x82\x00" \
        "\x00\x00\x40\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x81\x00", buff, "packet W: 1775/1776, R 1 to 1777/1778")
    # Generated from packet 1779/1780
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 1783/1784
    bulkWrite(0x02, 
        "\x04\x20\x05\x3D\x06\x20\x07\x64\x08\x6F\x09\x63\x0A\x75\x0B\x6D" \
        "\x57\x81\x00"
        )
    # Generated from packet 1785/1786
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 1789/1790
    cmd.led_mask(dev, "active")
    # Generated from packet 1793/1794
    cmd.cmd_50(dev, "\x18\x00")
    # Generated from packet 1795/1796
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x82\x00", buff, "packet W: 1795/1796, R 1 to 1797/1798")
    # Generated from packet 1799/1800
    cmd.cmd_02(dev, "\x83\x00\x30\x01\x09\x00")
    # Generated from packet 1803/1804
    buff = cmd.bulk2b(dev, 
        "\x57\x82\x00\x20\x01\x00\x2B\x3B\x0C\x22\x00\xC0\x40\x00\x3B\x0E" \
        "\x22\x00\xC0\x00\x00\x3B\x1A\x22\x00\xC0\x18\x00\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 1803/1804, R 1 to 1805/1806")
    # Generated from packet 1807/1808
    #cmd.gpio_readi(dev)
    # Generated from packet 1811/1812
    #cmd.gpio_readi(dev)
    # Generated from packet 1815/1816
    #cmd.sm_info22(dev)
    # Generated from packet 1819/1820
    #cmd.sm_info24(dev)
    # Generated from packet 1823/1824
    #cmd.sm_read(dev)
    # Generated from packet 1827/1828
    buff = cmd.bulk2b(dev, "\x48\x00\x10\x82\x02")
    validate_read("\x82\x00\x10\x01\x09\x00", buff, "packet W: 1827/1828, R 1 to 1829/1830")
    # Generated from packet 1831/1832
    bulkWrite(0x02, "\x20\x01\x00\x50\x7D\x02\x00\x00")
    # Generated from packet 1833/1834
    buff = cmd.bulk2b(dev, pic16f84_fw.p651)
    validate_read("\x82\x00", buff, "packet W: 1833/1834, R 1 to 1835/1836")
    # Generated from packet 1837/1838
    cmd.cmd_02(dev, "\x83\x00\x90\x03\x09\x00")
    # Generated from packet 1841/1842
    bulkWrite(0x02, "\x57\x82\x00\x50\x1D\x00\x00\x00")
    # Generated from packet 1843/1844
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x74\x46\x00\x00\x0B\x00\x00\x00\xFF\x15\x38\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x83\x00", buff, "packet W: 1843/1844, R 1 to 1845/1846")
    # Generated from packet 1847/1848
    cmd.cmd_02(dev, "\x84\x00\xB0\x03\x09\x00")
    # Generated from packet 1851/1852
    bulkWrite(0x02, "\x57\x83\x00\x50\x18\x3A\x00\x00")
    # Generated from packet 1853/1854
    buff = cmd.bulk2b(dev, pic16f84_fw.p533)
    validate_read("\x84\x00", buff, "packet W: 1853/1854, R 1 to 1855/1856")
    # Generated from packet 1857/1858
    cmd.cmd_02(dev, "\x85\x00\xD0\x3D\x09\x00")
    # Generated from packet 1861/1862
    bulkWrite(0x02, 
        "\x57\x84\x00\xF0\xFF\x01\x00\x00\x80\xFF\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\xFE\xFF\xFF\x7F\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        )
    # Generated from packet 1863/1864
    cmd.cmd_50(dev, "\xDE\x03")
    # Generated from packet 1865/1866
    buff = cmd.bulk2b(dev, pic16f84_fw.p555)
    validate_read("\x85\x00", buff, "packet W: 1865/1866, R 1 to 1867/1868")
    # Generated from packet 1869/1870
    cmd.cmd_02(dev, "\x86\x00\xB0\x41\x09\x00")

    # Generated from packet 1873/1874
    # Times out if chip not inserted
    #cmd.cmd_57s(dev, "\x85", "\x01")
    if cont:
        # Generated from packet 241/242
        # Takes about 0.05 sec on pass but 0.52 sec on fail
        tstart = time.time()
        buff = cmd.cmd_57s(dev, "\x85", None,  "cmd_57")
        tend = time.time()
        if verbose:
            print 'Continuity test took %0.3f sec' % (tend - tstart,)
            util.hexdump(buff, label='Continuity', indent='  ')
        # Chip inserted
        if buff == "\x01":
            if verbose:
                print 'Continuity OK'
        # Chip removed
        elif buff == ("\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
                    "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"):
            raise cmd.ContFail('Continuity complete failure (part not inserted?)')
        # Inserting chip while running
        # I'm guessing its telling me which pins failed
        # Lets bend a pin and verify
        else:
            raise cmd.ContFail('Continuity partial failure (dirty contacts?  Inserted wrong?)')

    # Generated from packet 1877/1878
    cmd.cmd_50(dev, "\x71\x1B")
    # Generated from packet 1879/1880
    buff = cmd.bulk2b(dev, pic16f84_fw.p591)
    validate_read("\x86\x00", buff, "packet W: 1879/1880, R 1 to 1881/1882")
    # Generated from packet 1883/1884
    cmd.cmd_02(dev, "\x87\x00\x30\x5D\x09\x00")
    # Generated from packet 1887/1888
    buff = cmd.bulk2b(dev, 
        "\x57\x86\x00\x2C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x06" \
        "\x07\x08\x09\x28\x29\x2A\x2B\x2D\x2E\x2F\x30\x00\x00"
        )
    validate_read("\x01", buff, "packet W: 1887/1888, R 1 to 1889/1890")
    # Generated from packet 1891/1892
    bulkWrite(0x02, "\x20\x01\x00\x50\x36\x00\x00\x00")
    # Generated from packet 1893/1894
    buff = cmd.bulk2b(dev, 
        "\x00\x00\x3C\x00\x38\x00\x34\x00\x30\x00\x00\x00\x39\x00\x35\x00" \
        "\x31\x00\x3E\x00\x2E\x00\x21\x00\x25\x00\x29\x00\x1C\x00\x20\x00" \
        "\x24\x00\x28\x00\x2C\x00\x00\x00\x04\x00\x08\x00\x0C\x00\x10\x00" \
        "\x14\x00\x18\x00\x1C\x00"
        )
    validate_read("\x87\x00", buff, "packet W: 1893/1894, R 1 to 1895/1896")
    # Generated from packet 1897/1898
    cmd.cmd_02(dev, "\x88\x00\x70\x5D\x09\x00")
    # Generated from packet 1901/1902
    bulkWrite(0x02, 
        "\x1D\x30\x5D\x09\x00\x12\x00\x15\x60\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x10\x00\x00\x00\x00\x1C\x30\x00\x10\x00\x00\x00\x00\x00\x48" \
        "\x00\x50\x71\x09\x00\x00"
        )
    # Generated from packet 1903/1904
    buff = cmd.bulk2b(dev, pic16f84_fw.p615)
    validate_read("\x88\x00", buff, "packet W: 1903/1904, R 1 to 1905/1906")
    # Generated from packet 1907/1908
    cmd.cmd_02(dev, "\x89\x00\xF0\x66\x09\x00")
    # Generated from packet 1911/1912
    cmd.cmd_57s(dev, "\x88", "\x00\x00")
    # Generated from packet 1915/1916
    cmd.cmd_50(dev, "\x17\x00")
    # Generated from packet 1917/1918
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x2C\x00\x09\x00\x24\x00\x00\x00\x66\xB9\x00\x00\xB2\x00" \
        "\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x89\x00", buff, "packet W: 1917/1918, R 1 to 1919/1920")
    # Generated from packet 1921/1922
    cmd.cmd_02(dev, "\x8A\x00\x10\x67\x09\x00")
    # Generated from packet 1925/1926
    bulkWrite(0x02, "\x57\x89\x00\x50\x18\x00\x00\x00")
    # Generated from packet 1927/1928
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x8A\x00", buff, "packet W: 1927/1928, R 1 to 1929/1930")
    # Generated from packet 1931/1932
    cmd.cmd_02(dev, "\x8B\x00\x30\x67\x09\x00")
    # Generated from packet 1935/1936
    bulkWrite(0x02, "\x57\x8A\x00\x50\xD1\x06\x00\x00")
    # Generated from packet 1937/1938
    buff = cmd.bulk2b(dev, pic16f84_fw.p891)
    validate_read("\x8B\x00", buff, "packet W: 1937/1938, R 1 to 1939/1940")
    # Generated from packet 1941/1942
    cmd.cmd_02(dev, "\x8C\x00\x10\x6E\x09\x00")
    # Generated from packet 1945/1946
    cmd.cmd_57s(dev, "\x8B", "\x00\x00")
    # Generated from packet 1949/1950
    cmd.cmd_50(dev, "\xF2\x02")
    # Generated from packet 1951/1952
    buff = cmd.bulk2b(dev, pic16f84_fw.p663)
    validate_read("\x8C\x00", buff, "packet W: 1951/1952, R 1 to 1953/1954")
    # Generated from packet 1955/1956
    cmd.cmd_02(dev, "\x8D\x00\x10\x71\x09\x00")

    # XXX
    # unprotected: \x00\x00
    # protected: \x01\x00
    # Generated from packet 1959/1960
    buff = cmd.bulk2b(dev, "\x08\x01\x57\x8C\x00")
    #validate_read("\x00\x00", buff, "packet W: 1959/1960, R 1 to 1961/1962")
    util.hexdump(buff, label='packet 1959/1960', indent='  ')
    #print binascii.hexlify(buff)
    config['secure'] = buff != '\x00\x00'

    # Generated from packet 1963/1964
    cmd.cmd_50(dev, "\xCE\x03")
    # Generated from packet 1965/1966
    buff = cmd.bulk2b(dev, pic16f84_fw.p919)
    validate_read("\x8D\x00", buff, "packet W: 1965/1966, R 1 to 1967/1968")
    # Generated from packet 1969/1970
    cmd.cmd_02(dev, "\x8E\x00\xE0\x74\x09\x00")
    # Generated from packet 1973/1974
    cmd.cmd_57s(dev, "\x8D", "\x00\x00")
    # Generated from packet 1977/1978
    buff = cmd.bulk2b(dev, "\x57\x8A\x00\x57\x8B\x00")
    validate_read("\x00\x00", buff, "packet W: 1977/1978, R 1 to 1979/1980")
    # Generated from packet 1981/1982
    cmd.cmd_50(dev, "\x45\x03")
    # Generated from packet 1983/1984
    buff = cmd.bulk2b(dev, pic16f84_fw.p697)
    validate_read("\x8E\x00", buff, "packet W: 1983/1984, R 1 to 1985/1986")
    # Generated from packet 1987/1988
    cmd.cmd_02(dev, "\x8F\x00\x30\x78\x09\x00")

    # Generated from packet 1991/1992
    buff = cmd.bulk2b(dev, 
        "\x04\x00\x05\x00\x06\x00\x07\x00\x08\x00\x09\x04\x0A\x00\x0B\x00" \
        "\x57\x8E\x00"
        )
    code = buff
    #validate_read(pic16f84_fw.p2001, buff, "packet W: 1991/1992, R 5 to 2001/2002")

    # Generated from packet 2003/2004
    cmd.cmd_50(dev, "\x5E\x00")
    # Generated from packet 2005/2006
    buff = cmd.bulk2b(dev, 
        "\x66\xC7\x05\x1C\x24\x00\x00\x00\x00\x66\x8B\x1D\x1C\x24\x00\x00" \
        "\x81\xE3\xFF\xFF\x00\x00\xC1\xE3\x01\x53\x5B\x66\xC7\x83\x38\x24" \
        "\x00\x00\xAD\x0B\x66\xFF\x05\x1C\x24\x00\x00\x66\x8B\x05\x1C\x24" \
        "\x00\x00\x81\xE0\xFF\xFF\x00\x00\xFF\xF0\xB8\x07\x00\x00\x00\x59" \
        "\x39\xC8\x77\xC5\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00" \
        "\x00\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x8F\x00", buff, "packet W: 2005/2006, R 1 to 2007/2008")
    # Generated from packet 2009/2010
    cmd.cmd_02(dev, "\x90\x00\x90\x78\x09\x00")
    # Generated from packet 2013/2014
    cmd.cmd_57s(dev, "\x8F", "\x00\x00")
    # Generated from packet 2017/2018
    cmd.cmd_50(dev, "\x58\x06")
    # Generated from packet 2019/2020
    buff = cmd.bulk2b(dev, pic16f84_fw.p759)
    validate_read("\x90\x00", buff, "packet W: 2019/2020, R 1 to 2021/2022")
    # Generated from packet 2023/2024
    cmd.cmd_02(dev, "\x91\x00\xF0\x7E\x09\x00")
    # Generated from packet 2027/2028
    cmd.cmd_57s(dev, "\x90", "\x00\x00")
    # Generated from packet 2031/2032
    cmd.cmd_50(dev, "\x92\x00")
    # Generated from packet 2033/2034
    buff = cmd.bulk2b(dev, 
        "\xE9\x03\x00\x00\x00\x90\x00\x00\x66\xC7\x05\xF6\x7E\x09\x00\x00" \
        "\x00\x66\x8B\x05\xF6\x7E\x09\x00\x81\xE0\xFF\xFF\x00\x00\xFF\xF0" \
        "\xB8\x07\x00\x00\x00\x59\x39\xC8\x0F\x86\x57\x00\x00\x00\x66\x8B" \
        "\x1D\xF6\x7E\x09\x00\x81\xE3\xFF\xFF\x00\x00\xC1\xE3\x01\x66\x50" \
        "\x66\x8B\x83\x38\x24\x00\x00\xFB\x66\x50\x66\x53\x66\x51\x8A\xC8" \
        "\xFF\x15\x3C\x11\x00\x00\x66\x59\x66\x5B\xFA\x66\x58\x66\xC1\xE8" \
        "\x08\xFB\x66\x53\x66\x51\x8A\xC8\xFF\x15\x3C\x11\x00\x00\x66\x59" \
        "\x66\x5B\xFA\x66\x58\x66\x8B\x05\xF6\x7E\x09\x00\x66\xFF\x05\xF6" \
        "\x7E\x09\x00\xEB\x8C\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11" \
        "\x00\x00"
        )
    validate_read("\x91\x00", buff, "packet W: 2033/2034, R 1 to 2035/2036")
    # Generated from packet 2037/2038
    cmd.cmd_02(dev, "\x92\x00\x90\x7F\x09\x00")

    # FIXME: which is this?
    # Names from minipro
    #fuses = {'conf_word': None}
    # 4 ID words?
    # Generated from packet 2041/2042
    # "\xFF\x3F \xFF\x3F \xFF\x3F \xFF\x3F \x03\x00 \x01\x00 \x01\x00"
    buff = cmd.cmd_57s(dev, "\x91", None)
    def fusepack(buff, i):
        return struct.unpack('<H', buff[2*i:2*i+2])[0]
    for i in xrange(0, 4):
        config['user_id%d' % i] = fusepack(buff, i)
    # FIXME: confirm
    config['conf_word'] = fusepack(buff, 4)
    #print binascii.hexlify(buff)


    # Generated from packet 2045/2046
    cmd.cmd_50(dev, "\x89\x00")
    # Generated from packet 2047/2048
    buff = cmd.bulk2b(dev, 
        "\x66\xC7\x05\x28\x24\x00\x00\x00\x00\x66\x8B\x05\x28\x24\x00\x00" \
        "\x81\xE0\xFF\xFF\x00\x00\xFF\xF0\xB8\x06\x00\x00\x00\x59\x39\xC8" \
        "\x0F\x87\x15\x00\x00\x00\xE9\x51\x00\x00\x00\x66\x8B\x05\x28\x24" \
        "\x00\x00\x66\xFF\x05\x28\x24\x00\x00\xEB\xCE\xE9\x04\x00\x00\x00" \
        "\x00\x00\x00\x00\x66\xC7\x05\xD0\x7F\x09\x00\x06\x00\x66\x8B\x0D" \
        "\x28\x24\x00\x00\x66\xD3\x2D\xD0\x7F\x09\x00\x66\x8B\x05\xD0\x7F" \
        "\x09\x00\x81\xE0\xFF\xFF\x00\x00\x88\x05\x28\x80\x00\x80\x88\x05" \
        "\x24\x80\x06\x40\x88\x05\x24\x80\x04\x40\xEB\xAF\x66\xB9\x00\x00" \
        "\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x92\x00", buff, "packet W: 2047/2048, R 1 to 2049/2050")
    # Generated from packet 2051/2052
    cmd.cmd_02(dev, "\x93\x00\x20\x80\x09\x00")
    # Generated from packet 2055/2056
    bulkWrite(0x02, pic16f84_fw.p795)
    # Generated from packet 2057/2058
    buff = cmd.bulk2b(dev, pic16f84_fw.p797)
    validate_read("\x93\x00", buff, "packet W: 2057/2058, R 1 to 2059/2060")
    # Generated from packet 2061/2062
    cmd.cmd_02(dev, "\x94\x00\xA0\x81\x09\x00")
    # Generated from packet 2065/2066
    bulkWrite(0x02, "\x57\x93\x00\x50\x07\x01\x00\x00")
    # Generated from packet 2067/2068
    buff = cmd.bulk2b(dev, pic16f84_fw.p807)
    validate_read("\x94\x00", buff, "packet W: 2067/2068, R 1 to 2069/2070")
    # Generated from packet 2071/2072
    cmd.cmd_02(dev, "\x95\x00\xB0\x82\x09\x00")

    eeprom = my_cmd_57s(dev)

    # Generated from packet 2335/2336
    cmd.cmd_50(dev, "\x0D\x00")
    # Generated from packet 2337/2338
    buff = cmd.bulk2b(dev, "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00")
    validate_read("\x95\x00", buff, "packet W: 2337/2338, R 1 to 2339/2340")
    # Generated from packet 2341/2342
    cmd.cmd_02(dev, "\x96\x00\xC0\x82\x09\x00")
    # Generated from packet 2345/2346
    bulkWrite(0x02, "\x57\x95\x00\x50\x1A\x00\x00\x00")
    # Generated from packet 2347/2348
    buff = cmd.bulk2b(dev, 
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00\x66\xB9\x00" \
        "\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x96\x00", buff, "packet W: 2347/2348, R 1 to 2349/2350")
    # Generated from packet 2351/2352
    cmd.cmd_02(dev, "\x97\x00\xE0\x82\x09\x00")
    # Generated from packet 2355/2356
    cmd.cmd_57s(dev, "\x96", "\x00\x00")
    # Generated from packet 2359/2360
    cmd.led_mask(dev, "pass")
    # Generated from packet 2363/2364
    #cmd.gpio_readi(dev)
    # Generated from packet 2367/2368
    #cmd.gpio_readi(dev)
    # Generated from packet 2371/2372
    #cmd.sm_info22(dev)
    # Generated from packet 2375/2376
    #cmd.sm_info24(dev)
    # Generated from packet 2379/2380
    #cmd.sm_read(dev)
    # Generated from packet 2383/2384
    cmd.cmd_49(dev)
    # Generated from packet 2387/2388
    #cmd.sm_read(dev)
    # Generated from packet 2391/2392
    #cmd.sm_insert(dev)
    # Generated from packet 2395/2396
    #cmd.sm_info10(dev)

    return {'code': code, 'data': eeprom, 'config': config}

class PIC16F84(bpmicro.device.Device):
    def __init__(self, dev, verbose=False):
        self.verbose = verbose
        self.dev = dev

    def read(self, opts):
        return dev_read(dev=self.dev, cont=opts.get('cont', True), verbose=opts.get('verbose', False))

    @staticmethod
    def print_config(config):
        for i in xrange(0, 4):
            print '  user_id%d:  0x%04X' % (i, config['user_id%d' % i])
        #print '  conf_word: 0x%04X' % (config['conf_word'])
        print '  secure: %s' % (config['secure'])
