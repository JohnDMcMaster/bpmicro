from bpmicro.usb import usb_wraps
from bpmicro.util import hexdump

from bpmicro.cmd import bulk2, bulk86
from bpmicro.cmd import sm_info3, led_mask_30
from bpmicro.cmd import cmd_20_mk, cmd_49, cmd_02, cmd_50, cmd_50_mk, cmd_0C_mk, cmd_57s, cmd_57_50, cmd_41, cmd_43, cmd_10, cmd_45
from bpmicro.cmd import cmd_4C, cmd_09, cmd_08, cmd_3B, cmd_4A
from bpmicro.cmd import sm_info0, sm_info1, sm_insert, sn_read, sm_info10
from bpmicro.usb import validate_read
from bpmicro.cmd import cmd_01
from bpmicro import cmd
import bpmicro.device
import at89c51_fw
import bpmicro.mcs51.at89c51_fw

import usb1
import sys
import inspect
import time

def dev_read(dev, cont=False, verbose=False):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)
    
    # None (0xB0)
    # NOTE:: req max 4096 but got 3
    buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
    # Req: 4096, got: 3
    validate_read("\x00\x00\x00", buff, "packet 1877/1882")
    # Generated from packet 1883/1884
    _prefix, buff, _size = cmd.bulk86_next_read(dev)
    validate_read("\x16", buff, "packet 1883/1884")
    # NOTE:: req max 512 but got 136
    # Generated from packet 1899/1900
    # bulk2 aggregate: packet W: 1899/1900, 1 to R 1901/1902
    buff = cmd.bulk2b(dev, 
        "\x43\x19\x10\x00\x00\x3B\x7E\x25\x00\x00\xFE\xFF\x3B\x7C\x25\x00" \
        "\x00\xFE\xFF\x00"
        )
    validate_read("\xA4\x06", buff, "packet W: 1899/1900, R 1 to 1901/1902")
    # NOTE:: req max 512 but got 35
    # Generated from packet 1913/1914
    # bulk2 aggregate: packet W: 1913/1914, 1 to R 1915/1916
    buff = cmd.bulk2b(dev, 
        "\x14\x38\x25\x00\x00\x04\x00\x90\x32\x90\x00\xA7\x02\x1F\x00\x14" \
        "\x40\x25\x00\x00\x01\x00\x3C\x36\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 1913/1914, R 1 to 1915/1916")
    # NOTE:: req max 512 but got 136
    # Generated from packet 1941/1942
    cmd.cmd_43(dev, "\x10")
    # Generated from packet 1943/1944
    bulkWrite(0x02, "\x20\x01\x00\x0C\x04")
    # Generated from packet 1945/1946
    cmd.cmd_41(dev)
    # Generated from packet 1947/1948
    # bulk2 aggregate: packet W: 1947/1948, 1 to R 1949/1950
    cmd.cmd_10(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 1983/1984
    # bulk2 aggregate: packet W: 1983/1984, 1 to R 1987/1994
    cmd.cmd_45(dev)
    # NOTE:: req max 512 but got 103
    # Generated from packet 1995/1996
    # bulk2 aggregate: packet W: 1995/1996, 1 to R 1997/1998
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2027/2028
    # bulk2 aggregate: packet W: 2027/2028, 1 to R 2029/2030
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 11
    # Generated from packet 2049/2050
    bulkWrite(0x02, 
        "\x3B\x0C\x22\x00\xC0\x30\x00\x3B\x0E\x22\x00\xC0\x00\x00\x3B\x1A" \
        "\x22\x00\xC0\x18\x00"
        )
    # Generated from packet 2051/2052
    # bulk2 aggregate: packet W: 2051/2052, 1 to R 2053/2054
    cmd.cmd_4A(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2055/2058
    cmd.cmd_4C(dev)
    # Generated from packet 2059/2060
    # None (0xB2)
    buff = controlWrite(0x40, 0xB2, 0x0000, 0x0000, "")
    # Generated from packet 2061/2062
    cmd.cmd_50(dev, "\x4D\x00")
    # Generated from packet 2063/2064
    # bulk2 aggregate: packet W: 2063/2064, 1 to R 2067/2068
    buff = cmd.bulk2b(dev, 
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x10" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x80" \
        "\xE9\x02\x00\x00\x00\x90\x00\xE9\x04\x00\x00\x00\x00\x00\x00\x00" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x80\x00", buff, "packet W: 2063/2064, R 1 to 2067/2068")
    # Generated from packet 2069/2070
    # bulk2 aggregate: packet W: 2069/2070, 1 to R 2071/2072
    cmd.cmd_02(dev, "\x81\x00\x50\x00\x09\x00")
    # Generated from packet 2075/2076
    cmd.cmd_50(dev, "\xC0\x00")
    # Generated from packet 2077/2078
    # bulk2 aggregate: packet W: 2077/2078, 1 to R 2079/2080
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
    validate_read("\x81\x00", buff, "packet W: 2077/2078, R 1 to 2079/2080")
    # Generated from packet 2081/2082
    # bulk2 aggregate: packet W: 2081/2082, 1 to R 2085/2086
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2087/2088
    cmd.cmd_09(dev)
    # Generated from packet 2093/2094
    # bulk2 aggregate: packet W: 2093/2094, 1 to R 2095/2096
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2099/2100
    # bulk2 aggregate: packet W: 2099/2100, 1 to R 2101/2102
    cmd.led_mask(dev, "active")
    # Generated from packet 2103/2104
    cmd.cmd_50(dev, "\x18\x00")
    # Generated from packet 2107/2108
    # bulk2 aggregate: packet W: 2107/2108, 1 to R 2109/2110
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x82\x00", buff, "packet W: 2107/2108, R 1 to 2109/2110")
    # Generated from packet 2111/2112
    # bulk2 aggregate: packet W: 2111/2112, 1 to R 2113/2114
    cmd.cmd_02(dev, "\x83\x00\x30\x01\x09\x00")
    # Generated from packet 2115/2116
    # bulk2 aggregate: packet W: 2115/2116, 1 to R 2119/2132
    buff = cmd.bulk2b(dev, 
        "\x57\x82\x00\x20\x01\x00\x2B\x3B\x0C\x22\x00\xC0\x30\x00\x3B\x0E" \
        "\x22\x00\xC0\x00\x00\x3B\x1A\x22\x00\xC0\x18\x00\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 2115/2116, R 1 to 2119/2132")
    # Generated from packet 2161/2162
    # bulk2 aggregate: packet W: 2161/2162, 1 to R 2163/2164
    buff = cmd.bulk2b(dev, "\x48\x00\x10\x82\x02")
    validate_read("\x82\x00\x10\x01\x09\x00", buff, "packet W: 2161/2162, R 1 to 2163/2164")
    # Generated from packet 2167/2168
    bulkWrite(0x02, "\x20\x01\x00\x50\x7D\x02\x00\x00")
    # Generated from packet 2171/2172
    # bulk2 aggregate: packet W: 2171/2172, 1 to R 2173/2174
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p7497e05e)
    validate_read("\x82\x00", buff, "packet W: 2171/2172, R 1 to 2173/2174")
    # Generated from packet 2175/2176
    # bulk2 aggregate: packet W: 2175/2176, 1 to R 2177/2178
    cmd.cmd_02(dev, "\x83\x00\x90\x03\x09\x00")
    # Generated from packet 2179/2180
    bulkWrite(0x02, "\x57\x82\x00\x50\x1D\x00\x00\x00")
    # Generated from packet 2181/2182
    # bulk2 aggregate: packet W: 2181/2182, 1 to R 2183/2186
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x74\x46\x00\x00\x0B\x00\x00\x00\xFF\x15\x38\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x83\x00", buff, "packet W: 2181/2182, R 1 to 2183/2186")
    # Generated from packet 2187/2188
    # bulk2 aggregate: packet W: 2187/2188, 1 to R 2189/2190
    cmd.cmd_02(dev, "\x84\x00\xB0\x03\x09\x00")
    # Generated from packet 2191/2192
    bulkWrite(0x02, "\x57\x83\x00\x50\x62\x00\x00\x00")
    # Generated from packet 2193/2194
    # bulk2 aggregate: packet W: 2193/2194, 1 to R 2195/2196
    buff = cmd.bulk2b(dev, 
        "\x00\x00\x3C\x00\x38\x00\x34\x00\x30\x00\x3D\x00\x39\x00\x35\x00" \
        "\x31\x00\x3E\x00\x3A\x00\x36\x00\x32\x00\x3F\x00\x3B\x00\x37\x00" \
        "\x33\x00\x1E\x00\x1A\x00\x16\x00\x00\x00\x02\x00\x06\x00\x0A\x00" \
        "\x0E\x00\x23\x00\x27\x00\x2B\x00\x2F\x00\x22\x00\x26\x00\x2A\x00" \
        "\x2E\x00\x21\x00\x25\x00\x29\x00\x2D\x00\x20\x00\x24\x00\x28\x00" \
        "\x1C\x00\x00\x00\x04\x00\x08\x00\x0C\x00\x10\x00\x14\x00\x18\x00" \
        "\x1C\x00"
        )
    validate_read("\x84\x00", buff, "packet W: 2193/2194, R 1 to 2195/2196")
    # Generated from packet 2197/2198
    # bulk2 aggregate: packet W: 2197/2198, 1 to R 2199/2200
    cmd.cmd_02(dev, "\x85\x00\x20\x04\x09\x00")
    # Generated from packet 2201/2202
    bulkWrite(0x02, 
        "\x1D\xB0\x03\x09\x00\x28\x00\x15\x60\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x01\x00\x00\x00\x1C\x30\x00\x00\x00\x08\x00\x00\x00\x48" \
        "\x00"
        )
    # Generated from packet 2203/2204
    cmd.cmd_50(dev, "\x17\x00")
    # Generated from packet 2205/2206
    # bulk2 aggregate: packet W: 2205/2206, 1 to R 2207/2208
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x2C\x00\x09\x00\x04\x04\x00\x00\x66\xB9\x00\x00\xB2\x00" \
        "\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x85\x00", buff, "packet W: 2205/2206, R 1 to 2207/2208")
    # Generated from packet 2209/2210
    # bulk2 aggregate: packet W: 2209/2210, 1 to R 2211/2212
    cmd.cmd_02(dev, "\x86\x00\x40\x04\x09\x00")
    # Generated from packet 2213/2214
    bulkWrite(0x02, "\x57\x85\x00\x50\x18\x00\x00\x00")
    # Generated from packet 2215/2216
    # bulk2 aggregate: packet W: 2215/2216, 1 to R 2217/2218
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x86\x00", buff, "packet W: 2215/2216, R 1 to 2217/2218")
    # Generated from packet 2219/2220
    # bulk2 aggregate: packet W: 2219/2220, 1 to R 2221/2222
    cmd.cmd_02(dev, "\x87\x00\x60\x04\x09\x00")
    # Generated from packet 2223/2224
    bulkWrite(0x02, "\x57\x86\x00\x50\x4F\x08\x00\x00")
    # Generated from packet 2225/2226
    # bulk2 aggregate: packet W: 2225/2226, 1 to R 2227/2228
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pb765d18a)
    validate_read("\x87\x00", buff, "packet W: 2225/2226, R 1 to 2227/2228")
    # Generated from packet 2229/2230
    # bulk2 aggregate: packet W: 2229/2230, 1 to R 2231/2232
    cmd.cmd_02(dev, "\x88\x00\xB0\x0C\x09\x00")
    # Generated from packet 2233/2234
    # bulk2 aggregate: packet W: 2233/2234, 1 to R 2235/2242
    cmd.cmd_57s(dev, "\x87", "\x00\x00")
    # Generated from packet 2243/2244
    cmd.cmd_50(dev, "\xCB\x02")
    # Generated from packet 2245/2246
    # bulk2 aggregate: packet W: 2245/2246, 1 to R 2249/2250
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pe1244dd0)
    validate_read("\x88\x00", buff, "packet W: 2245/2246, R 1 to 2249/2250")
    # Generated from packet 2251/2252
    # bulk2 aggregate: packet W: 2251/2252, 1 to R 2253/2254
    cmd.cmd_02(dev, "\x89\x00\x80\x0F\x09\x00")
    # Generated from packet 2257/2258
    # bulk2 aggregate: packet W: 2257/2258, 9 to R 2325/2326
    code = cmd.cmd_57s(dev, "\x88", None)
    # Generated from packet 2331/2332
    cmd.cmd_50(dev, "\x8E\x04")
    # Generated from packet 2333/2334
    # bulk2 aggregate: packet W: 2333/2334, 1 to R 2335/2336
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p99f93b18)
    validate_read("\x89\x00", buff, "packet W: 2333/2334, R 1 to 2335/2336")
    # Generated from packet 2337/2338
    # bulk2 aggregate: packet W: 2337/2338, 1 to R 2339/2340
    cmd.cmd_02(dev, "\x8A\x00\x10\x14\x09\x00")
    # Generated from packet 2341/2342
    # bulk2 aggregate: packet W: 2341/2342, 1 to R 2343/2346
    cmd.cmd_57s(dev, "\x89", "\x00\x00")
    # Generated from packet 2347/2348
    cmd.cmd_50(dev, "\x0D\x00")
    # Generated from packet 2349/2350
    # bulk2 aggregate: packet W: 2349/2350, 1 to R 2351/2352
    buff = cmd.bulk2b(dev, "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00")
    validate_read("\x8A\x00", buff, "packet W: 2349/2350, R 1 to 2351/2352")
    # Generated from packet 2353/2354
    # bulk2 aggregate: packet W: 2353/2354, 1 to R 2355/2356
    cmd.cmd_02(dev, "\x8B\x00\x20\x14\x09\x00")
    # Generated from packet 2357/2358
    bulkWrite(0x02, "\x57\x8A\x00\x50\x1A\x00\x00\x00")
    # Generated from packet 2359/2360
    # bulk2 aggregate: packet W: 2359/2360, 1 to R 2361/2362
    buff = cmd.bulk2b(dev, 
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00\x66\xB9\x00" \
        "\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x8B\x00", buff, "packet W: 2359/2360, R 1 to 2361/2362")
    # Generated from packet 2363/2364
    # bulk2 aggregate: packet W: 2363/2364, 1 to R 2365/2366
    cmd.cmd_02(dev, "\x8C\x00\x40\x14\x09\x00")
    # Generated from packet 2367/2368
    # bulk2 aggregate: packet W: 2367/2368, 1 to R 2369/2370
    cmd.cmd_57s(dev, "\x8B", "\x00\x00")
    # Generated from packet 2371/2372
    # bulk2 aggregate: packet W: 2371/2372, 1 to R 2373/2374
    cmd.led_mask(dev, "pass")
    # Generated from packet 2399/2400
    # bulk2 aggregate: packet W: 2399/2400, 1 to R 2401/2402
    cmd.cmd_49(dev)

    return {'code': code}

def dev_read_id_cont(dev, cont=False, verbose=False):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)
    
    # Selected device 17
    # Generated by uvusbreplay 0.1
    # uvusbreplay copyright 2011 John McMaster <JohnDMcMaster@gmail.com>
    # cmd: /usr/local/bin/usbrply --packet-numbers --no-setup --comment --fx2 --device-hi -j ./01_read_cont-y_id-y.cap.pcapng
    # Generated from packet 2013/2014
    # None (0xB0)
    # NOTE:: req max 4096 but got 3
    buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
    # Req: 4096, got: 3
    validate_read("\x00\x00\x00", buff, "packet 2013/2014")
    # Generated from packet 2015/2016
    _prefix, buff, _size = cmd.bulk86_next_read(dev)
    validate_read("\x16", buff, "packet 2015/2016")
    # NOTE:: req max 512 but got 136
    # Generated from packet 2055/2056
    # bulk2 aggregate: packet W: 2055/2056, 1 to R 2057/2058
    buff = cmd.bulk2b(dev, 
        "\x43\x19\x10\x00\x00\x3B\x7E\x25\x00\x00\xFE\xFF\x3B\x7C\x25\x00" \
        "\x00\xFE\xFF\x00"
        )
    validate_read("\xA4\x06", buff, "packet W: 2055/2056, R 1 to 2057/2058")
    # NOTE:: req max 512 but got 35
    # Generated from packet 2071/2072
    # bulk2 aggregate: packet W: 2071/2072, 1 to R 2075/2076
    buff = cmd.bulk2b(dev, 
        "\x14\x38\x25\x00\x00\x04\x00\x90\x32\x90\x00\xA7\x02\x1F\x00\x14" \
        "\x40\x25\x00\x00\x01\x00\x3C\x36\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 2071/2072, R 1 to 2075/2076")
    # NOTE:: req max 512 but got 136
    # Generated from packet 2109/2110
    cmd.cmd_43(dev, "\x10")
    # Generated from packet 2113/2114
    bulkWrite(0x02, "\x20\x01\x00\x0C\x04")
    # Generated from packet 2115/2116
    cmd.cmd_41(dev)
    # Generated from packet 2117/2118
    # bulk2 aggregate: packet W: 2117/2118, 1 to R 2121/2122
    cmd.cmd_10(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2155/2156
    # bulk2 aggregate: packet W: 2155/2156, 1 to R 2157/2164
    cmd.cmd_45(dev)
    # NOTE:: req max 512 but got 103
    # Generated from packet 2165/2166
    # bulk2 aggregate: packet W: 2165/2166, 1 to R 2167/2168
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2189/2190
    # bulk2 aggregate: packet W: 2189/2190, 1 to R 2191/2192
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 11
    # Generated from packet 2207/2208
    bulkWrite(0x02, 
        "\x3B\x0C\x22\x00\xC0\x30\x00\x3B\x0E\x22\x00\xC0\x00\x00\x3B\x1A" \
        "\x22\x00\xC0\x18\x00"
        )
    # Generated from packet 2209/2210
    # bulk2 aggregate: packet W: 2209/2210, 1 to R 2211/2212
    cmd.cmd_4A(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2213/2214
    cmd.cmd_4C(dev)
    # Generated from packet 2215/2216
    # None (0xB2)
    buff = controlWrite(0x40, 0xB2, 0x0000, 0x0000, "")
    # Generated from packet 2217/2218
    cmd.cmd_50(dev, "\x4D\x00")
    # Generated from packet 2219/2220
    # bulk2 aggregate: packet W: 2219/2220, 1 to R 2221/2222
    buff = cmd.bulk2b(dev, 
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x10" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x80" \
        "\xE9\x02\x00\x00\x00\x90\x00\xE9\x04\x00\x00\x00\x00\x00\x00\x00" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x80\x00", buff, "packet W: 2219/2220, R 1 to 2221/2222")
    # Generated from packet 2223/2224
    # bulk2 aggregate: packet W: 2223/2224, 1 to R 2225/2226
    cmd.cmd_02(dev, "\x81\x00\x50\x00\x09\x00")
    # Generated from packet 2227/2228
    cmd.cmd_50(dev, "\xC0\x00")
    # Generated from packet 2229/2230
    # bulk2 aggregate: packet W: 2229/2230, 1 to R 2231/2232
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
    validate_read("\x81\x00", buff, "packet W: 2229/2230, R 1 to 2231/2232")
    # Generated from packet 2233/2234
    # bulk2 aggregate: packet W: 2233/2234, 1 to R 2235/2236
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2237/2238
    cmd.cmd_09(dev)
    # Generated from packet 2239/2240
    # bulk2 aggregate: packet W: 2239/2240, 1 to R 2241/2242
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2243/2244
    # bulk2 aggregate: packet W: 2243/2244, 1 to R 2245/2246
    cmd.led_mask(dev, "active")
    # Generated from packet 2247/2248
    cmd.cmd_50(dev, "\x18\x00")
    # Generated from packet 2249/2250
    # bulk2 aggregate: packet W: 2249/2250, 1 to R 2251/2252
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x82\x00", buff, "packet W: 2249/2250, R 1 to 2251/2252")
    # Generated from packet 2253/2254
    # bulk2 aggregate: packet W: 2253/2254, 1 to R 2255/2256
    cmd.cmd_02(dev, "\x83\x00\x30\x01\x09\x00")
    # Generated from packet 2257/2258
    # bulk2 aggregate: packet W: 2257/2258, 1 to R 2259/2260
    buff = cmd.bulk2b(dev, 
        "\x57\x82\x00\x20\x01\x00\x2B\x3B\x0C\x22\x00\xC0\x30\x00\x3B\x0E" \
        "\x22\x00\xC0\x00\x00\x3B\x1A\x22\x00\xC0\x18\x00\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 2257/2258, R 1 to 2259/2260")
    # Generated from packet 2281/2282
    # bulk2 aggregate: packet W: 2281/2282, 1 to R 2283/2284
    buff = cmd.bulk2b(dev, "\x48\x00\x10\x82\x02")
    validate_read("\x82\x00\x10\x01\x09\x00", buff, "packet W: 2281/2282, R 1 to 2283/2284")
    # Generated from packet 2285/2286
    bulkWrite(0x02, "\x20\x01\x00\x50\x7D\x02\x00\x00")
    # Generated from packet 2287/2288
    # bulk2 aggregate: packet W: 2287/2288, 1 to R 2289/2290
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p7497e05e)
    validate_read("\x82\x00", buff, "packet W: 2287/2288, R 1 to 2289/2290")
    # Generated from packet 2291/2292
    # bulk2 aggregate: packet W: 2291/2292, 1 to R 2293/2294
    cmd.cmd_02(dev, "\x83\x00\x90\x03\x09\x00")
    # Generated from packet 2295/2296
    bulkWrite(0x02, "\x57\x82\x00\x50\x1D\x00\x00\x00")
    # Generated from packet 2297/2298
    # bulk2 aggregate: packet W: 2297/2298, 1 to R 2299/2300
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x74\x46\x00\x00\x0B\x00\x00\x00\xFF\x15\x38\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x83\x00", buff, "packet W: 2297/2298, R 1 to 2299/2300")
    # Generated from packet 2301/2302
    # bulk2 aggregate: packet W: 2301/2302, 1 to R 2303/2304
    cmd.cmd_02(dev, "\x84\x00\xB0\x03\x09\x00")
    # Generated from packet 2305/2306
    bulkWrite(0x02, "\x57\x83\x00\x50\x18\x3A\x00\x00")
    # Generated from packet 2307/2308
    # bulk2 aggregate: packet W: 2307/2308, 1 to R 2309/2310
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p06a7b55f)
    validate_read("\x84\x00", buff, "packet W: 2307/2308, R 1 to 2309/2310")
    # Generated from packet 2311/2312
    # bulk2 aggregate: packet W: 2311/2312, 1 to R 2313/2314
    cmd.cmd_02(dev, "\x85\x00\xD0\x3D\x09\x00")
    # Generated from packet 2315/2316
    bulkWrite(0x02, 
        "\x57\x84\x00\xF0\xFF\xFF\x0F\xF0\xFF\xFF\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\xF0\x0F\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        )
    # Generated from packet 2317/2318
    cmd.cmd_50(dev, "\xDE\x03")
    # Generated from packet 2319/2320
    # bulk2 aggregate: packet W: 2319/2320, 1 to R 2321/2322
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pf127b9be)
    validate_read("\x85\x00", buff, "packet W: 2319/2320, R 1 to 2321/2322")
    # Generated from packet 2323/2324
    # bulk2 aggregate: packet W: 2323/2324, 1 to R 2325/2326
    cmd.cmd_02(dev, "\x86\x00\xB0\x41\x09\x00")
    # Generated from packet 2327/2328
    # bulk2 aggregate: packet W: 2327/2328, 1 to R 2329/2330
    cmd.check_cont(dev)
    # Generated from packet 2331/2332
    cmd.cmd_50(dev, "\x71\x1B")
    # Generated from packet 2333/2334
    # bulk2 aggregate: packet W: 2333/2334, 1 to R 2335/2336
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pccc4c386)
    validate_read("\x86\x00", buff, "packet W: 2333/2334, R 1 to 2335/2336")
    # Generated from packet 2337/2338
    # bulk2 aggregate: packet W: 2337/2338, 1 to R 2339/2340
    cmd.cmd_02(dev, "\x87\x00\x30\x5D\x09\x00")
    # Generated from packet 2341/2342
    # bulk2 aggregate: packet W: 2341/2342, 1 to R 2343/2344
    buff = cmd.bulk2b(dev, 
        "\x57\x86\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05" \
        "\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12\x13\x1D\x1E" \
        "\x1F\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2A\x2B\x2C\x2D\x2E" \
        "\x2F\x00\x00"
        )
    validate_read("\x01", buff, "packet W: 2341/2342, R 1 to 2343/2344")
    # Generated from packet 2349/2350
    bulkWrite(0x02, "\x20\x01\x00\x50\x62\x00\x00\x00")
    # Generated from packet 2351/2352
    # bulk2 aggregate: packet W: 2351/2352, 1 to R 2353/2354
    buff = cmd.bulk2b(dev, 
        "\x00\x00\x3C\x00\x38\x00\x34\x00\x30\x00\x3D\x00\x39\x00\x35\x00" \
        "\x31\x00\x3E\x00\x3A\x00\x36\x00\x32\x00\x3F\x00\x3B\x00\x37\x00" \
        "\x33\x00\x1E\x00\x1A\x00\x16\x00\x00\x00\x02\x00\x06\x00\x0A\x00" \
        "\x0E\x00\x23\x00\x27\x00\x2B\x00\x2F\x00\x22\x00\x26\x00\x2A\x00" \
        "\x2E\x00\x21\x00\x25\x00\x29\x00\x2D\x00\x20\x00\x24\x00\x28\x00" \
        "\x1C\x00\x00\x00\x04\x00\x08\x00\x0C\x00\x10\x00\x14\x00\x18\x00" \
        "\x1C\x00"
        )
    validate_read("\x87\x00", buff, "packet W: 2351/2352, R 1 to 2353/2354")
    # Generated from packet 2355/2356
    # bulk2 aggregate: packet W: 2355/2356, 1 to R 2357/2358
    cmd.cmd_02(dev, "\x88\x00\xA0\x5D\x09\x00")
    # Generated from packet 2361/2362
    bulkWrite(0x02, 
        "\x1D\x30\x5D\x09\x00\x28\x00\x15\x60\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x01\x00\x00\x00\x1C\x30\x00\x00\x00\x08\x00\x00\x00\x48" \
        "\x00\x50\x71\x09\x00\x00"
        )
    # Generated from packet 2363/2364
    # bulk2 aggregate: packet W: 2363/2364, 1 to R 2367/2368
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p41a6e1af)
    validate_read("\x88\x00", buff, "packet W: 2363/2364, R 1 to 2367/2368")
    # Generated from packet 2369/2370
    # bulk2 aggregate: packet W: 2369/2370, 1 to R 2371/2372
    cmd.cmd_02(dev, "\x89\x00\x20\x67\x09\x00")
    # Generated from packet 2373/2374
    # bulk2 aggregate: packet W: 2373/2374, 1 to R 2375/2376
    cmd.cmd_57s(dev, "\x88", "\x00\x00")
    # Generated from packet 2377/2378
    cmd.cmd_50(dev, "\x17\x00")
    # Generated from packet 2379/2380
    # bulk2 aggregate: packet W: 2379/2380, 1 to R 2381/2382
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x2C\x00\x09\x00\x04\x04\x00\x00\x66\xB9\x00\x00\xB2\x00" \
        "\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x89\x00", buff, "packet W: 2379/2380, R 1 to 2381/2382")
    # Generated from packet 2383/2384
    # bulk2 aggregate: packet W: 2383/2384, 1 to R 2385/2386
    cmd.cmd_02(dev, "\x8A\x00\x40\x67\x09\x00")
    # Generated from packet 2389/2390
    bulkWrite(0x02, "\x57\x89\x00\x50\x4F\x08\x00\x00")
    # Generated from packet 2391/2392
    # bulk2 aggregate: packet W: 2391/2392, 1 to R 2393/2394
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pb765d18a)
    validate_read("\x8A\x00", buff, "packet W: 2391/2392, R 1 to 2393/2394")
    # Generated from packet 2395/2396
    # bulk2 aggregate: packet W: 2395/2396, 1 to R 2397/2398
    cmd.cmd_02(dev, "\x8B\x00\x90\x6F\x09\x00")
    # Generated from packet 2399/2400
    # bulk2 aggregate: packet W: 2399/2400, 1 to R 2401/2404
    cmd.cmd_57s(dev, "\x8A", "\x00\x00")
    # Generated from packet 2405/2406
    cmd.cmd_50(dev, "\x96\x04")
    # Generated from packet 2407/2408
    # bulk2 aggregate: packet W: 2407/2408, 1 to R 2409/2410
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p040c7668)
    validate_read("\x8B\x00", buff, "packet W: 2407/2408, R 1 to 2409/2410")
    # Generated from packet 2411/2412
    # bulk2 aggregate: packet W: 2411/2412, 1 to R 2413/2414
    cmd.cmd_02(dev, "\x8C\x00\x30\x74\x09\x00")
    # Generated from packet 2415/2416
    # bulk2 aggregate: packet W: 2415/2416, 1 to R 2417/2418
    cmd.cmd_57s(dev, "\x8B", "\x1E\x00")
    # Generated from packet 2419/2420
    cmd.cmd_50(dev, "\x1D\x00")
    # Generated from packet 2421/2422
    # bulk2 aggregate: packet W: 2421/2422, 1 to R 2423/2424
    buff = cmd.bulk2b(dev, 
        "\x66\x8B\x0D\x1A\x24\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x8C\x00", buff, "packet W: 2421/2422, R 1 to 2423/2424")
    # Generated from packet 2425/2426
    # bulk2 aggregate: packet W: 2425/2426, 1 to R 2427/2428
    cmd.cmd_02(dev, "\x8D\x00\x50\x74\x09\x00")
    # Generated from packet 2429/2430
    # bulk2 aggregate: packet W: 2429/2430, 1 to R 2431/2432
    cmd.cmd_57s(dev, "\x8C", "\xFF\x51")
    # Generated from packet 2433/2434
    cmd.cmd_50(dev, "\x8E\x04")
    # Generated from packet 2435/2436
    # bulk2 aggregate: packet W: 2435/2436, 1 to R 2437/2438
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p99f93b18)
    validate_read("\x8D\x00", buff, "packet W: 2435/2436, R 1 to 2437/2438")
    # Generated from packet 2439/2440
    # bulk2 aggregate: packet W: 2439/2440, 1 to R 2441/2442
    cmd.cmd_02(dev, "\x8E\x00\xE0\x78\x09\x00")
    # Generated from packet 2443/2444
    # bulk2 aggregate: packet W: 2443/2444, 1 to R 2445/2446
    cmd.cmd_57s(dev, "\x8D", "\x00\x00")
    # Generated from packet 2447/2448
    cmd.cmd_50(dev, "\x18\x00")
    # Generated from packet 2449/2450
    # bulk2 aggregate: packet W: 2449/2450, 1 to R 2451/2452
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x8E\x00", buff, "packet W: 2449/2450, R 1 to 2451/2452")
    # Generated from packet 2453/2454
    # bulk2 aggregate: packet W: 2453/2454, 1 to R 2455/2456
    cmd.cmd_02(dev, "\x8F\x00\x00\x79\x09\x00")
    # Generated from packet 2457/2458
    # bulk2 aggregate: packet W: 2457/2458, 1 to R 2459/2464
    cmd.cmd_57s(dev, "\x8E\x8A", "\x00\x00")
    # Generated from packet 2465/2466
    cmd.cmd_50(dev, "\xCB\x02")
    # Generated from packet 2467/2468
    # bulk2 aggregate: packet W: 2467/2468, 1 to R 2469/2470
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pe1244dd0)
    validate_read("\x8F\x00", buff, "packet W: 2467/2468, R 1 to 2469/2470")
    # Generated from packet 2471/2472
    # bulk2 aggregate: packet W: 2471/2472, 1 to R 2473/2474
    cmd.cmd_02(dev, "\x90\x00\xD0\x7B\x09\x00")
    # Generated from packet 2475/2476
    # bulk2 aggregate: packet W: 2475/2476, 9 to R 2497/2498
    code = cmd.cmd_57s(dev, "\x8F", None)
    # Generated from packet 2499/2500
    # bulk2 aggregate: packet W: 2499/2500, 1 to R 2501/2502
    cmd.cmd_57s(dev, "\x8D", "\x00\x00")
    # Generated from packet 2503/2504
    cmd.cmd_50(dev, "\x0D\x00")
    # Generated from packet 2505/2506
    # bulk2 aggregate: packet W: 2505/2506, 1 to R 2507/2508
    buff = cmd.bulk2b(dev, "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00")
    validate_read("\x90\x00", buff, "packet W: 2505/2506, R 1 to 2507/2508")
    # Generated from packet 2509/2510
    # bulk2 aggregate: packet W: 2509/2510, 1 to R 2511/2512
    cmd.cmd_02(dev, "\x91\x00\xE0\x7B\x09\x00")
    # Generated from packet 2513/2514
    bulkWrite(0x02, "\x57\x90\x00\x50\x1A\x00\x00\x00")
    # Generated from packet 2515/2516
    # bulk2 aggregate: packet W: 2515/2516, 1 to R 2517/2518
    buff = cmd.bulk2b(dev, 
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00\x66\xB9\x00" \
        "\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x91\x00", buff, "packet W: 2515/2516, R 1 to 2517/2518")
    # Generated from packet 2519/2520
    # bulk2 aggregate: packet W: 2519/2520, 1 to R 2521/2522
    cmd.cmd_02(dev, "\x92\x00\x00\x7C\x09\x00")
    # Generated from packet 2523/2524
    # bulk2 aggregate: packet W: 2523/2524, 1 to R 2525/2526
    cmd.cmd_57s(dev, "\x91", "\x00\x00")
    # Generated from packet 2527/2528
    # bulk2 aggregate: packet W: 2527/2528, 1 to R 2529/2530
    cmd.led_mask(dev, "pass")
    # Generated from packet 2551/2552
    # bulk2 aggregate: packet W: 2551/2552, 1 to R 2553/2554
    cmd.cmd_49(dev)

    return {'code': code}

def dev_write(dev, devcfg, cont=True, verbose=False, blank=True, erase=True):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)
    
    # Selected device 17
    # Generated by uvusbreplay 0.1
    # uvusbreplay copyright 2011 John McMaster <JohnDMcMaster@gmail.com>
    # cmd: /usr/local/bin/usbrply --packet-numbers --no-setup --comment --fx2 --device-hi -j ./01_read_cont-y_id-y.cap.pcapng
    # Generated from packet 2013/2014
    # None (0xB0)
    # NOTE:: req max 4096 but got 3
    buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
    # Req: 4096, got: 3
    validate_read("\x00\x00\x00", buff, "packet 2013/2014")
    # Generated from packet 2015/2016
    _prefix, buff, _size = cmd.bulk86_next_read(dev)
    validate_read("\x16", buff, "packet 2015/2016")
    # NOTE:: req max 512 but got 136
    # Generated from packet 2055/2056
    # bulk2 aggregate: packet W: 2055/2056, 1 to R 2057/2058
    buff = cmd.bulk2b(dev, 
        "\x43\x19\x10\x00\x00\x3B\x7E\x25\x00\x00\xFE\xFF\x3B\x7C\x25\x00" \
        "\x00\xFE\xFF\x00"
        )
    validate_read("\xA4\x06", buff, "packet W: 2055/2056, R 1 to 2057/2058")
    # NOTE:: req max 512 but got 35
    # Generated from packet 2071/2072
    # bulk2 aggregate: packet W: 2071/2072, 1 to R 2075/2076
    buff = cmd.bulk2b(dev, 
        "\x14\x38\x25\x00\x00\x04\x00\x90\x32\x90\x00\xA7\x02\x1F\x00\x14" \
        "\x40\x25\x00\x00\x01\x00\x3C\x36\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 2071/2072, R 1 to 2075/2076")
    # NOTE:: req max 512 but got 136
    # Generated from packet 2109/2110
    cmd.cmd_43(dev, "\x10")
    # Generated from packet 2113/2114
    bulkWrite(0x02, "\x20\x01\x00\x0C\x04")
    # Generated from packet 2115/2116
    cmd.cmd_41(dev)
    # Generated from packet 2117/2118
    # bulk2 aggregate: packet W: 2117/2118, 1 to R 2121/2122
    cmd.cmd_10(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2155/2156
    # bulk2 aggregate: packet W: 2155/2156, 1 to R 2157/2164
    cmd.cmd_45(dev)
    # NOTE:: req max 512 but got 103
    # Generated from packet 2165/2166
    # bulk2 aggregate: packet W: 2165/2166, 1 to R 2167/2168
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2189/2190
    # bulk2 aggregate: packet W: 2189/2190, 1 to R 2191/2192
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 11
    # Generated from packet 2207/2208
    bulkWrite(0x02, 
        "\x3B\x0C\x22\x00\xC0\x30\x00\x3B\x0E\x22\x00\xC0\x00\x00\x3B\x1A" \
        "\x22\x00\xC0\x18\x00"
        )
    # Generated from packet 2209/2210
    # bulk2 aggregate: packet W: 2209/2210, 1 to R 2211/2212
    cmd.cmd_4A(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2213/2214
    cmd.cmd_4C(dev)
    # Generated from packet 2215/2216
    # None (0xB2)
    buff = controlWrite(0x40, 0xB2, 0x0000, 0x0000, "")
    # Generated from packet 2217/2218
    cmd.cmd_50(dev, "\x4D\x00")
    # Generated from packet 2219/2220
    # bulk2 aggregate: packet W: 2219/2220, 1 to R 2221/2222
    buff = cmd.bulk2b(dev, 
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x10" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x80" \
        "\xE9\x02\x00\x00\x00\x90\x00\xE9\x04\x00\x00\x00\x00\x00\x00\x00" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x80\x00", buff, "packet W: 2219/2220, R 1 to 2221/2222")
    # Generated from packet 2223/2224
    # bulk2 aggregate: packet W: 2223/2224, 1 to R 2225/2226
    cmd.cmd_02(dev, "\x81\x00\x50\x00\x09\x00")
    # Generated from packet 2227/2228
    cmd.cmd_50(dev, "\xC0\x00")
    # Generated from packet 2229/2230
    # bulk2 aggregate: packet W: 2229/2230, 1 to R 2231/2232
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
    validate_read("\x81\x00", buff, "packet W: 2229/2230, R 1 to 2231/2232")
    # Generated from packet 2233/2234
    # bulk2 aggregate: packet W: 2233/2234, 1 to R 2235/2236
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2237/2238
    cmd.cmd_09(dev)
    # Generated from packet 2239/2240
    # bulk2 aggregate: packet W: 2239/2240, 1 to R 2241/2242
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2243/2244
    # bulk2 aggregate: packet W: 2243/2244, 1 to R 2245/2246
    cmd.led_mask(dev, "active")
    # Generated from packet 2247/2248
    cmd.cmd_50(dev, "\x18\x00")
    # Generated from packet 2249/2250
    # bulk2 aggregate: packet W: 2249/2250, 1 to R 2251/2252
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x82\x00", buff, "packet W: 2249/2250, R 1 to 2251/2252")
    # Generated from packet 2253/2254
    # bulk2 aggregate: packet W: 2253/2254, 1 to R 2255/2256
    cmd.cmd_02(dev, "\x83\x00\x30\x01\x09\x00")
    # Generated from packet 2257/2258
    # bulk2 aggregate: packet W: 2257/2258, 1 to R 2259/2260
    buff = cmd.bulk2b(dev, 
        "\x57\x82\x00\x20\x01\x00\x2B\x3B\x0C\x22\x00\xC0\x30\x00\x3B\x0E" \
        "\x22\x00\xC0\x00\x00\x3B\x1A\x22\x00\xC0\x18\x00\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 2257/2258, R 1 to 2259/2260")
    # Generated from packet 2281/2282
    # bulk2 aggregate: packet W: 2281/2282, 1 to R 2283/2284
    buff = cmd.bulk2b(dev, "\x48\x00\x10\x82\x02")
    validate_read("\x82\x00\x10\x01\x09\x00", buff, "packet W: 2281/2282, R 1 to 2283/2284")
    # Generated from packet 2285/2286
    bulkWrite(0x02, "\x20\x01\x00\x50\x7D\x02\x00\x00")
    # Generated from packet 2287/2288
    # bulk2 aggregate: packet W: 2287/2288, 1 to R 2289/2290
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p7497e05e)
    validate_read("\x82\x00", buff, "packet W: 2287/2288, R 1 to 2289/2290")
    # Generated from packet 2291/2292
    # bulk2 aggregate: packet W: 2291/2292, 1 to R 2293/2294
    cmd.cmd_02(dev, "\x83\x00\x90\x03\x09\x00")
    # Generated from packet 2295/2296
    bulkWrite(0x02, "\x57\x82\x00\x50\x1D\x00\x00\x00")
    # Generated from packet 2297/2298
    # bulk2 aggregate: packet W: 2297/2298, 1 to R 2299/2300
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x74\x46\x00\x00\x0B\x00\x00\x00\xFF\x15\x38\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x83\x00", buff, "packet W: 2297/2298, R 1 to 2299/2300")
    # Generated from packet 2301/2302
    # bulk2 aggregate: packet W: 2301/2302, 1 to R 2303/2304
    cmd.cmd_02(dev, "\x84\x00\xB0\x03\x09\x00")
    # Generated from packet 2305/2306
    bulkWrite(0x02, "\x57\x83\x00\x50\x18\x3A\x00\x00")
    # Generated from packet 2307/2308
    # bulk2 aggregate: packet W: 2307/2308, 1 to R 2309/2310
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p06a7b55f)
    validate_read("\x84\x00", buff, "packet W: 2307/2308, R 1 to 2309/2310")
    # Generated from packet 2311/2312
    # bulk2 aggregate: packet W: 2311/2312, 1 to R 2313/2314
    cmd.cmd_02(dev, "\x85\x00\xD0\x3D\x09\x00")
    # Generated from packet 2315/2316
    bulkWrite(0x02, 
        "\x57\x84\x00\xF0\xFF\xFF\x0F\xF0\xFF\xFF\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\xF0\x0F\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        )
    # Generated from packet 2317/2318
    cmd.cmd_50(dev, "\xDE\x03")
    # Generated from packet 2319/2320
    # bulk2 aggregate: packet W: 2319/2320, 1 to R 2321/2322
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pf127b9be)
    validate_read("\x85\x00", buff, "packet W: 2319/2320, R 1 to 2321/2322")
    # Generated from packet 2323/2324
    # bulk2 aggregate: packet W: 2323/2324, 1 to R 2325/2326
    cmd.cmd_02(dev, "\x86\x00\xB0\x41\x09\x00")
    # Generated from packet 2327/2328
    # bulk2 aggregate: packet W: 2327/2328, 1 to R 2329/2330
    cmd.check_cont(dev)
    # Generated from packet 2331/2332
    cmd.cmd_50(dev, "\x71\x1B")
    # Generated from packet 2333/2334
    # bulk2 aggregate: packet W: 2333/2334, 1 to R 2335/2336
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pccc4c386)
    validate_read("\x86\x00", buff, "packet W: 2333/2334, R 1 to 2335/2336")
    # Generated from packet 2337/2338
    # bulk2 aggregate: packet W: 2337/2338, 1 to R 2339/2340
    cmd.cmd_02(dev, "\x87\x00\x30\x5D\x09\x00")
    # Generated from packet 2341/2342
    # bulk2 aggregate: packet W: 2341/2342, 1 to R 2343/2344
    buff = cmd.bulk2b(dev, 
        "\x57\x86\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05" \
        "\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12\x13\x1D\x1E" \
        "\x1F\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2A\x2B\x2C\x2D\x2E" \
        "\x2F\x00\x00"
        )
    validate_read("\x01", buff, "packet W: 2341/2342, R 1 to 2343/2344")
    # Generated from packet 2349/2350
    bulkWrite(0x02, "\x20\x01\x00\x50\x62\x00\x00\x00")
    # Generated from packet 2351/2352
    # bulk2 aggregate: packet W: 2351/2352, 1 to R 2353/2354
    buff = cmd.bulk2b(dev, 
        "\x00\x00\x3C\x00\x38\x00\x34\x00\x30\x00\x3D\x00\x39\x00\x35\x00" \
        "\x31\x00\x3E\x00\x3A\x00\x36\x00\x32\x00\x3F\x00\x3B\x00\x37\x00" \
        "\x33\x00\x1E\x00\x1A\x00\x16\x00\x00\x00\x02\x00\x06\x00\x0A\x00" \
        "\x0E\x00\x23\x00\x27\x00\x2B\x00\x2F\x00\x22\x00\x26\x00\x2A\x00" \
        "\x2E\x00\x21\x00\x25\x00\x29\x00\x2D\x00\x20\x00\x24\x00\x28\x00" \
        "\x1C\x00\x00\x00\x04\x00\x08\x00\x0C\x00\x10\x00\x14\x00\x18\x00" \
        "\x1C\x00"
        )
    validate_read("\x87\x00", buff, "packet W: 2351/2352, R 1 to 2353/2354")
    # Generated from packet 2355/2356
    # bulk2 aggregate: packet W: 2355/2356, 1 to R 2357/2358
    cmd.cmd_02(dev, "\x88\x00\xA0\x5D\x09\x00")
    # Generated from packet 2361/2362
    bulkWrite(0x02, 
        "\x1D\x30\x5D\x09\x00\x28\x00\x15\x60\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x01\x00\x00\x00\x1C\x30\x00\x00\x00\x08\x00\x00\x00\x48" \
        "\x00\x50\x71\x09\x00\x00"
        )
    # Generated from packet 2363/2364
    # bulk2 aggregate: packet W: 2363/2364, 1 to R 2367/2368
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p41a6e1af)
    validate_read("\x88\x00", buff, "packet W: 2363/2364, R 1 to 2367/2368")
    # Generated from packet 2369/2370
    # bulk2 aggregate: packet W: 2369/2370, 1 to R 2371/2372
    cmd.cmd_02(dev, "\x89\x00\x20\x67\x09\x00")
    # Generated from packet 2373/2374
    # bulk2 aggregate: packet W: 2373/2374, 1 to R 2375/2376
    cmd.cmd_57s(dev, "\x88", "\x00\x00")
    # Generated from packet 2377/2378
    cmd.cmd_50(dev, "\x17\x00")
    # Generated from packet 2379/2380
    # bulk2 aggregate: packet W: 2379/2380, 1 to R 2381/2382
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x2C\x00\x09\x00\x04\x04\x00\x00\x66\xB9\x00\x00\xB2\x00" \
        "\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x89\x00", buff, "packet W: 2379/2380, R 1 to 2381/2382")
    # Generated from packet 2383/2384
    # bulk2 aggregate: packet W: 2383/2384, 1 to R 2385/2386
    cmd.cmd_02(dev, "\x8A\x00\x40\x67\x09\x00")
    # Generated from packet 2389/2390
    bulkWrite(0x02, "\x57\x89\x00\x50\x4F\x08\x00\x00")
    # Generated from packet 2391/2392
    # bulk2 aggregate: packet W: 2391/2392, 1 to R 2393/2394
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pb765d18a)
    validate_read("\x8A\x00", buff, "packet W: 2391/2392, R 1 to 2393/2394")
    # Generated from packet 2395/2396
    # bulk2 aggregate: packet W: 2395/2396, 1 to R 2397/2398
    cmd.cmd_02(dev, "\x8B\x00\x90\x6F\x09\x00")
    # Generated from packet 2399/2400
    # bulk2 aggregate: packet W: 2399/2400, 1 to R 2401/2404
    cmd.cmd_57s(dev, "\x8A", "\x00\x00")
    # Generated from packet 2405/2406
    cmd.cmd_50(dev, "\x96\x04")
    # Generated from packet 2407/2408
    # bulk2 aggregate: packet W: 2407/2408, 1 to R 2409/2410
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p040c7668)
    validate_read("\x8B\x00", buff, "packet W: 2407/2408, R 1 to 2409/2410")
    # Generated from packet 2411/2412
    # bulk2 aggregate: packet W: 2411/2412, 1 to R 2413/2414
    cmd.cmd_02(dev, "\x8C\x00\x30\x74\x09\x00")
    # Generated from packet 2415/2416
    # bulk2 aggregate: packet W: 2415/2416, 1 to R 2417/2418
    cmd.cmd_57s(dev, "\x8B", "\x1E\x00")
    # Generated from packet 2419/2420
    cmd.cmd_50(dev, "\x1D\x00")
    # Generated from packet 2421/2422
    # bulk2 aggregate: packet W: 2421/2422, 1 to R 2423/2424
    buff = cmd.bulk2b(dev, 
        "\x66\x8B\x0D\x1A\x24\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x8C\x00", buff, "packet W: 2421/2422, R 1 to 2423/2424")
    # Generated from packet 2425/2426
    # bulk2 aggregate: packet W: 2425/2426, 1 to R 2427/2428
    cmd.cmd_02(dev, "\x8D\x00\x50\x74\x09\x00")
    # Generated from packet 2429/2430
    # bulk2 aggregate: packet W: 2429/2430, 1 to R 2431/2432
    cmd.cmd_57s(dev, "\x8C", "\xFF\x51")
    # Generated from packet 2433/2434
    cmd.cmd_50(dev, "\x8E\x04")
    # Generated from packet 2435/2436
    # bulk2 aggregate: packet W: 2435/2436, 1 to R 2437/2438
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.p99f93b18)
    validate_read("\x8D\x00", buff, "packet W: 2435/2436, R 1 to 2437/2438")
    # Generated from packet 2439/2440
    # bulk2 aggregate: packet W: 2439/2440, 1 to R 2441/2442
    cmd.cmd_02(dev, "\x8E\x00\xE0\x78\x09\x00")
    # Generated from packet 2443/2444
    # bulk2 aggregate: packet W: 2443/2444, 1 to R 2445/2446
    cmd.cmd_57s(dev, "\x8D", "\x00\x00")
    # Generated from packet 2447/2448
    cmd.cmd_50(dev, "\x18\x00")
    # Generated from packet 2449/2450
    # bulk2 aggregate: packet W: 2449/2450, 1 to R 2451/2452
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x8E\x00", buff, "packet W: 2449/2450, R 1 to 2451/2452")
    # Generated from packet 2453/2454
    # bulk2 aggregate: packet W: 2453/2454, 1 to R 2455/2456
    cmd.cmd_02(dev, "\x8F\x00\x00\x79\x09\x00")
    # Generated from packet 2457/2458
    # bulk2 aggregate: packet W: 2457/2458, 1 to R 2459/2464
    cmd.cmd_57s(dev, "\x8E\x8A", "\x00\x00")
    # Generated from packet 2465/2466
    cmd.cmd_50(dev, "\xCB\x02")
    # Generated from packet 2467/2468
    # bulk2 aggregate: packet W: 2467/2468, 1 to R 2469/2470
    buff = cmd.bulk2b(dev, bpmicro.mcs51.at89c51_fw.pe1244dd0)
    validate_read("\x8F\x00", buff, "packet W: 2467/2468, R 1 to 2469/2470")
    # Generated from packet 2471/2472
    # bulk2 aggregate: packet W: 2471/2472, 1 to R 2473/2474
    cmd.cmd_02(dev, "\x90\x00\xD0\x7B\x09\x00")
    # Generated from packet 2475/2476
    # bulk2 aggregate: packet W: 2475/2476, 9 to R 2497/2498
    cmd.cmd_57s(dev, "\x8F", devcfg['code'])
    # Generated from packet 2499/2500
    # bulk2 aggregate: packet W: 2499/2500, 1 to R 2501/2502
    cmd.cmd_57s(dev, "\x8D", "\x00\x00")
    # Generated from packet 2503/2504
    cmd.cmd_50(dev, "\x0D\x00")
    # Generated from packet 2505/2506
    # bulk2 aggregate: packet W: 2505/2506, 1 to R 2507/2508
    buff = cmd.bulk2b(dev, "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00")
    validate_read("\x90\x00", buff, "packet W: 2505/2506, R 1 to 2507/2508")
    # Generated from packet 2509/2510
    # bulk2 aggregate: packet W: 2509/2510, 1 to R 2511/2512
    cmd.cmd_02(dev, "\x91\x00\xE0\x7B\x09\x00")
    # Generated from packet 2513/2514
    bulkWrite(0x02, "\x57\x90\x00\x50\x1A\x00\x00\x00")
    # Generated from packet 2515/2516
    # bulk2 aggregate: packet W: 2515/2516, 1 to R 2517/2518
    buff = cmd.bulk2b(dev, 
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00\x66\xB9\x00" \
        "\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x91\x00", buff, "packet W: 2515/2516, R 1 to 2517/2518")
    # Generated from packet 2519/2520
    # bulk2 aggregate: packet W: 2519/2520, 1 to R 2521/2522
    cmd.cmd_02(dev, "\x92\x00\x00\x7C\x09\x00")
    # Generated from packet 2523/2524
    # bulk2 aggregate: packet W: 2523/2524, 1 to R 2525/2526
    cmd.cmd_57s(dev, "\x91", "\x00\x00")
    # Generated from packet 2527/2528
    # bulk2 aggregate: packet W: 2527/2528, 1 to R 2529/2530
    cmd.led_mask(dev, "pass")
    # Generated from packet 2551/2552
    # bulk2 aggregate: packet W: 2551/2552, 1 to R 2553/2554
    cmd.cmd_49(dev)

class AT89C51(bpmicro.device.Device):
    def __init__(self, dev, verbose=False):
        self.verbose = verbose
        self.dev = dev

    def read(self, opts):
        return dev_read(dev=self.dev, cont=opts.get('cont', True), verbose=opts.get('verbose', False))

    def program(self, devcfg, opts):
        dev_write(dev=self.dev, devcfg=devcfg, cont=opts.get('cont', True), verbose=opts.get('verbose', False))
