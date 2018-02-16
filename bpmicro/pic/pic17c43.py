# Based off of 17_read-cont-y_cold.cap
# md5 0fdb988186be94a062adc9d1c0019463

from bpmicro import cmd
from bpmicro import util
from bpmicro.usb import validate_read
from bpmicro.usb import usb_wraps
from bpmicro.bp1410_fw import load_fx2
import pic16f84_fw
import bpmicro.device

import bpmicro.pic.pic16f84_fw
import pic17c43_fw

import binascii
import struct
import time













def dev_read(dev, cont=False, verbose=False):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)

    # Generated from packet 1755/1756
    # Unexpected SM read
    buff = cmd.bulk2b(dev, "\x22\x02\x25\x00\x25\x00\x06")
    validate_read("\x00\x00", buff, "packet W: 1755/1756, R 1 to 1757/1758")
    # Generated from packet 2237/2238
    # NOTE:: req max 4096 but got 3
    buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
    # Req: 4096, got: 3
    validate_read("\x00\x00\x00", buff, "packet 2237/2238")
    # Generated from packet 2239/2240
    _prefix, buff, _size = cmd.bulk86_next_read(dev)
    validate_read("\x16", buff, "packet 2239/2240")
    # NOTE:: req max 512 but got 4
    # Generated from packet 2241/2242
    cmd.cmd_01(dev)
    # NOTE:: req max 512 but got 136
    # Generated from packet 2245/2246
    buff = cmd.bulk2b(dev, 
        "\x43\x19\x20\x00\x00\x3B\x7E\x25\x00\x00\xFE\xFF\x3B\x7C\x25\x00" \
        "\x00\xFE\xFF\x00"
        )
    validate_read("\xA4\x06", buff, "packet W: 2245/2246, R 1 to 2247/2248")
    # NOTE:: req max 512 but got 5
    # Generated from packet 2249/2250
    cmd.cmd_01(dev)
    # NOTE:: req max 512 but got 136
    # Generated from packet 2253/2254
    cmd.sn_read(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2257/2258
    buff = cmd.bulk2b(dev, 
        "\x14\x38\x25\x00\x00\x04\x00\x90\x32\x90\x00\xA7\x02\x1F\x00\x14" \
        "\x40\x25\x00\x00\x01\x00\x3C\x36\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 2257/2258, R 1 to 2259/2260")
    # NOTE:: req max 512 but got 35
    # Generated from packet 2261/2262
    cmd.gpio_readi(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2265/2266
    cmd.gpio_readi(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2269/2270
    cmd.sm_info22(dev)
    # NOTE:: req max 512 but got 7
    # Generated from packet 2273/2274
    cmd.sm_info24(dev)
    # NOTE:: req max 512 but got 7
    # Generated from packet 2277/2278
    cmd.sm_read(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2281/2282
    cmd.cmd_01(dev)
    if 0:
        # NOTE:: req max 512 but got 32
        # Generated from packet 2285/2286
        _prefix, buff, _size = cmd.bulk86_next_read(dev)
        validate_read(
            "\x09\x00\x08\x00\xFF\x00\xC4\x1E\x00\x00\xCC\x1E\x00\x00\xB4\x46" \
            "\x00\x00\xD0\x1E\x00\x00\xC0\x1E\x01\x00\xB0\x1E\x01\x00\x00\x00" \
            "\x30\x55\x01\x00\x00\x00\x00\x00\x02\x00\x80\x01\xD0\x01\x02\x00" \
            "\x01\x00\x00\x00\x56\x10\x00\x00\xA0\x25\x00\x00\x84\x25\x00\x00" \
            "\x00\x00\x01\x00\x7C\x25\x00\x00\x7E\x25\x00\x00\x80\x25\x00\x00" \
            "\x74\x46\x00\x00\x38\x11\x00\x00\x3C\x11\x00\x00\x40\x11\x00\x00" \
            "\x44\x11\x00\x00\xC0\x1E\x00\x00"
            , buff, "packet 2285/2286")
    # NOTE:: req max 512 but got 107
    # Generated from packet 2287/2288
    bulkWrite(0x02, "\x43\x19\x20\x00\x00")
    # Generated from packet 2289/2290
    bulkWrite(0x02, "\x20\x01\x00\x0C\x04")
    # Generated from packet 2291/2292
    cmd.cmd_41(dev)
    # Generated from packet 2293/2294
    cmd.cmd_10(dev)
    # NOTE:: req max 512 but got 9
    # Generated from packet 2297/2298
    cmd.sm_read(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2301/2302
    cmd.sm_insert(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2305/2306
    cmd.cmd_45(dev)
    # NOTE:: req max 512 but got 103
    # Generated from packet 2309/2310
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2313/2314
    cmd.gpio_readi(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2317/2318
    cmd.gpio_readi(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2321/2322
    cmd.sm_info22(dev)
    # NOTE:: req max 512 but got 7
    # Generated from packet 2325/2326
    cmd.sm_info24(dev)
    # NOTE:: req max 512 but got 7
    # Generated from packet 2329/2330
    cmd.sm_read(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2333/2334
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2337/2338
    cmd.sm_read(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2341/2342
    cmd.sm_insert(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2347/2348
    cmd.sm_info10(dev)
    # NOTE:: req max 512 but got 11
    # Generated from packet 2351/2352
    cmd.cmd_3B(dev)
    # Generated from packet 2353/2354
    cmd.cmd_4A(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2357/2358
    cmd.cmd_4C(dev)
    # Generated from packet 2359/2360
    buff = controlWrite(0x40, 0xB2, 0x0000, 0x0000, "")
    # Generated from packet 2363/2364
    cmd.cmd_50(dev, "\x45\x00")
    # Generated from packet 2365/2366
    buff = cmd.bulk2b(dev, 
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x10" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x80" \
        "\xE9\x02\x00\x00\x00\x90\x00\xE9\x04\x00\x00\x00\x00\x00\x00\x00" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\x66\xB9\x00\x00\xB2\x00\xFB\xFF" \
        "\x25\x44\x11\x00\x00"
        )
    validate_read("\x80\x00", buff, "packet W: 2365/2366, R 1 to 2367/2368")
    # Generated from packet 2371/2372
    cmd.cmd_02(dev, "\x81\x00\x50\x00\x09\x00")
    # Generated from packet 2375/2376
    cmd.cmd_50(dev, "\xC0\x00")
    # Generated from packet 2377/2378
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
    validate_read("\x81\x00", buff, "packet W: 2377/2378, R 1 to 2381/2382")
    # Generated from packet 2383/2384
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2387/2388
    bulkWrite(0x02, 
        "\x04\x20\x05\x3D\x06\x20\x07\x64\x08\x6F\x09\x63\x0A\x75\x0B\x6D" \
        "\x57\x81\x00"
        )
    # Generated from packet 2393/2394
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2397/2398
    cmd.led_mask(dev, "active")
    # Generated from packet 2403/2404
    cmd.cmd_50(dev, "\x18\x00")
    # Generated from packet 2405/2406
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x82\x00", buff, "packet W: 2405/2406, R 1 to 2407/2408")
    # Generated from packet 2411/2412
    cmd.cmd_02(dev, "\x83\x00\x30\x01\x09\x00")
    # Generated from packet 2415/2416
    buff = cmd.bulk2b(dev, 
        "\x57\x82\x00\x20\x01\x00\x2B\x3B\x0C\x22\x00\xC0\x40\x00\x3B\x0E" \
        "\x22\x00\xC0\x00\x00\x3B\x1A\x22\x00\xC0\x18\x00\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 2415/2416, R 1 to 2417/2428")
    # Generated from packet 2429/2430
    cmd.gpio_readi(dev)
    # Generated from packet 2433/2434
    cmd.gpio_readi(dev)
    # Generated from packet 2439/2440
    cmd.sm_info22(dev)
    # Generated from packet 2443/2444
    cmd.sm_info24(dev)
    # Generated from packet 2449/2450
    cmd.sm_read(dev)
    # Generated from packet 2455/2456
    buff = cmd.bulk2b(dev, "\x48\x00\x10\x82\x02")
    validate_read("\x82\x00\x10\x01\x09\x00", buff, "packet W: 2455/2456, R 1 to 2457/2458")
    # Generated from packet 2461/2462
    bulkWrite(0x02, "\x20\x01\x00\x50\x7D\x02\x00\x00")
    # Generated from packet 2463/2464
    buff = cmd.bulk2b(dev, bpmicro.pic.pic16f84_fw.p651)
    validate_read("\x82\x00", buff, "packet W: 2463/2464, R 1 to 2465/2466")
    # Generated from packet 2467/2468
    cmd.cmd_02(dev, "\x83\x00\x90\x03\x09\x00")
    # Generated from packet 2471/2472
    bulkWrite(0x02, "\x57\x82\x00\x50\x1D\x00\x00\x00")
    # Generated from packet 2473/2474
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x74\x46\x00\x00\x0B\x00\x00\x00\xFF\x15\x38\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x83\x00", buff, "packet W: 2473/2474, R 1 to 2475/2476")
    # Generated from packet 2477/2478
    cmd.cmd_02(dev, "\x84\x00\xB0\x03\x09\x00")
    # Generated from packet 2481/2482
    bulkWrite(0x02, "\x57\x83\x00\x50\x18\x3A\x00\x00")
    # Generated from packet 2483/2484
    buff = cmd.bulk2b(dev, bpmicro.pic.pic16f84_fw.p533)
    validate_read("\x84\x00", buff, "packet W: 2483/2484, R 1 to 2485/2486")
    # Generated from packet 2487/2488
    cmd.cmd_02(dev, "\x85\x00\xD0\x3D\x09\x00")
    # Generated from packet 2491/2492
    bulkWrite(0x02, 
        "\x57\x84\x00\xF0\xFF\xFF\x0F\xF0\xFF\xFF\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\xF0\x0F\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF" \
        "\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        )
    # Generated from packet 2493/2494
    cmd.cmd_50(dev, "\xDE\x03")
    # Generated from packet 2495/2496
    buff = cmd.bulk2b(dev, bpmicro.pic.pic16f84_fw.p555)
    validate_read("\x85\x00", buff, "packet W: 2495/2496, R 1 to 2497/2498")
    # Generated from packet 2499/2500
    cmd.cmd_02(dev, "\x86\x00\xB0\x41\x09\x00")
    # Generated from packet 2503/2504
    cmd.cmd_57s(dev, "\x85", "\x01")
    # Generated from packet 2507/2508
    cmd.cmd_50(dev, "\x62\x00")
    # Generated from packet 2509/2510
    buff = cmd.bulk2b(dev, 
        "\x00\x00\x1C\x00\x38\x00\x34\x00\x30\x00\x3D\x00\x39\x00\x35\x00" \
        "\x31\x00\x3E\x00\x00\x00\x36\x00\x32\x00\x3F\x00\x3B\x00\x37\x00" \
        "\x33\x00\x1E\x00\x1A\x00\x16\x00\x12\x00\x02\x00\x06\x00\x0A\x00" \
        "\x0E\x00\x23\x00\x27\x00\x2B\x00\x2F\x00\x22\x00\x26\x00\x00\x00" \
        "\x2E\x00\x21\x00\x25\x00\x29\x00\x2D\x00\x20\x00\x24\x00\x28\x00" \
        "\x2C\x00\x00\x00\x04\x00\x08\x00\x0C\x00\x10\x00\x14\x00\x18\x00" \
        "\x1C\x00"
        )
    validate_read("\x86\x00", buff, "packet W: 2509/2510, R 1 to 2511/2512")
    # Generated from packet 2513/2514
    cmd.cmd_02(dev, "\x87\x00\x20\x42\x09\x00")
    # Generated from packet 2517/2518
    bulkWrite(0x02, 
        "\x1D\xB0\x41\x09\x00\x28\x00\x15\x60\x00\x02\x00\x00\x00\x00\x00" \
        "\x01\x00\x00\x00\x00\x00\x1C\x30\x00\x00\x02\x00\x00\x40\x00\x48" \
        "\x00\x50\x71\x09\x00\x00"
        )
    # Generated from packet 2519/2520
    buff = cmd.bulk2b(dev, pic17c43_fw.p2519)
    validate_read("\x87\x00", buff, "packet W: 2519/2520, R 1 to 2521/2522")
    # Generated from packet 2523/2524
    cmd.cmd_02(dev, "\x88\x00\xA0\x4B\x09\x00")
    # Generated from packet 2527/2528
    cmd.cmd_57s(dev, "\x87", "\x00\x00")
    # Generated from packet 2531/2532
    cmd.cmd_50(dev, "\x17\x00")
    # Generated from packet 2533/2534
    buff = cmd.bulk2b(dev, 
        "\xC7\x05\x2C\x00\x09\x00\x24\x04\x00\x00\x66\xB9\x00\x00\xB2\x00" \
        "\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x88\x00", buff, "packet W: 2533/2534, R 1 to 2535/2536")
    # Generated from packet 2537/2538
    cmd.cmd_02(dev, "\x89\x00\xC0\x4B\x09\x00")
    # Generated from packet 2543/2544
    bulkWrite(0x02, "\x57\x88\x00\x50\x18\x00\x00\x00")
    # Generated from packet 2545/2546
    buff = cmd.bulk2b(dev, 
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x89\x00", buff, "packet W: 2545/2546, R 1 to 2547/2548")
    # Generated from packet 2549/2550
    cmd.cmd_02(dev, "\x8A\x00\xE0\x4B\x09\x00")
    # Generated from packet 2553/2554
    bulkWrite(0x02, "\x57\x89\x00\x50\x04\x0A\x00\x00")
    # Generated from packet 2555/2556
    buff = cmd.bulk2b(dev, pic17c43_fw.p2555)
    validate_read("\x8A\x00", buff, "packet W: 2555/2556, R 1 to 2557/2558")
    # Generated from packet 2559/2560
    cmd.cmd_02(dev, "\x8B\x00\xF0\x55\x09\x00")
    # Generated from packet 2563/2564
    cmd.cmd_57s(dev, "\x8A", "\x00\x00")
    # Generated from packet 2567/2568
    cmd.cmd_50(dev, "\xBE\x03")
    # Generated from packet 2569/2570
    buff = cmd.bulk2b(dev, pic17c43_fw.p2569)
    validate_read("\x8B\x00", buff, "packet W: 2569/2570, R 1 to 2571/2572")
    # Generated from packet 2573/2574
    cmd.cmd_02(dev, "\x8C\x00\xB0\x59\x09\x00")

    # Generated from packet 2577/2578
    buff = cmd.bulk2b(dev, "\x08\x01\x57\x8B\x00")
    0 and validate_read("\x00\x00", buff, "packet W: 2577/2578, R 1 to 2581/2582")

    # Generated from packet 2583/2584
    cmd.cmd_50(dev, "\x1B\x04")
    # Generated from packet 2585/2586
    buff = cmd.bulk2b(dev, pic17c43_fw.p2585)
    validate_read("\x8C\x00", buff, "packet W: 2585/2586, R 1 to 2587/2588")
    # Generated from packet 2589/2590
    cmd.cmd_02(dev, "\x8D\x00\xD0\x5D\x09\x00")
    # Generated from packet 2593/2594
    cmd.cmd_57s(dev, "\x8C", "\x00\x00")
    # Generated from packet 2603/2604
    cmd.cmd_57s(dev, "\x89\x8A", "\x00\x00")
    # Generated from packet 2609/2610
    cmd.cmd_50(dev, "\x12\x03")
    # Generated from packet 2611/2612
    buff = cmd.bulk2b(dev, pic17c43_fw.p2611)
    validate_read("\x8D\x00", buff, "packet W: 2611/2612, R 1 to 2613/2614")
    # Generated from packet 2617/2618
    cmd.cmd_02(dev, "\x8E\x00\xF0\x60\x09\x00")




    # Generated from packet 2621/2622
    code = cmd.bulk2b(dev, 
        "\x04\x00\x05\x00\x06\x00\x07\x00\x08\x00\x09\x10\x0A\x00\x0B\x00" \
        "\x57\x8D\x00"
        )
    #validate_read(pic17c43_fw.p2681, buff, "packet W: 2621/2622, R 17 to 2681/2682")

    return {'code': code, 'data': None, 'config': None}



    # Generated from packet 2683/2684
    cmd.cmd_50(dev, "\x5E\x00")
    # Generated from packet 2685/2686
    buff = cmd.bulk2b(dev, 
        "\x66\xC7\x05\x1C\x24\x00\x00\x00\x00\x66\x8B\x1D\x1C\x24\x00\x00" \
        "\x81\xE3\xFF\xFF\x00\x00\xC1\xE3\x01\x53\x5B\x66\xC7\x83\x38\x24" \
        "\x00\x00\xAD\x0B\x66\xFF\x05\x1C\x24\x00\x00\x66\x8B\x05\x1C\x24" \
        "\x00\x00\x81\xE0\xFF\xFF\x00\x00\xFF\xF0\xB8\x01\x00\x00\x00\x59" \
        "\x39\xC8\x77\xC5\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00" \
        "\x00\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x8E\x00", buff, "packet W: 2685/2686, R 1 to 2687/2688")
    # Generated from packet 2689/2690
    cmd.cmd_02(dev, "\x8F\x00\x50\x61\x09\x00")
    # Generated from packet 2693/2694
    cmd.cmd_57s(dev, "\x8E", "\x00\x00")
    # Generated from packet 2697/2698
    cmd.cmd_50(dev, "\x96\x06")
    # Generated from packet 2699/2700
    buff = cmd.bulk2b(dev, pic17c43_fw.p2699)
    validate_read("\x8F\x00", buff, "packet W: 2699/2700, R 1 to 2701/2702")
    # Generated from packet 2703/2704
    cmd.cmd_02(dev, "\x90\x00\xF0\x67\x09\x00")
    # Generated from packet 2707/2708
    cmd.cmd_57s(dev, "\x8F", "\x00\x00")
    # Generated from packet 2711/2712
    cmd.cmd_50(dev, "\x92\x00")
    # Generated from packet 2713/2714
    buff = cmd.bulk2b(dev, 
        "\xE9\x03\x00\x00\x00\x90\x00\x00\x66\xC7\x05\xF6\x67\x09\x00\x00" \
        "\x00\x66\x8B\x05\xF6\x67\x09\x00\x81\xE0\xFF\xFF\x00\x00\xFF\xF0" \
        "\xB8\x01\x00\x00\x00\x59\x39\xC8\x0F\x86\x57\x00\x00\x00\x66\x8B" \
        "\x1D\xF6\x67\x09\x00\x81\xE3\xFF\xFF\x00\x00\xC1\xE3\x01\x66\x50" \
        "\x66\x8B\x83\x38\x24\x00\x00\xFB\x66\x50\x66\x53\x66\x51\x8A\xC8" \
        "\xFF\x15\x3C\x11\x00\x00\x66\x59\x66\x5B\xFA\x66\x58\x66\xC1\xE8" \
        "\x08\xFB\x66\x53\x66\x51\x8A\xC8\xFF\x15\x3C\x11\x00\x00\x66\x59" \
        "\x66\x5B\xFA\x66\x58\x66\x8B\x05\xF6\x67\x09\x00\x66\xFF\x05\xF6" \
        "\x67\x09\x00\xEB\x8C\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11" \
        "\x00\x00"
        )
    validate_read("\x90\x00", buff, "packet W: 2713/2714, R 1 to 2715/2716")
    # Generated from packet 2717/2718
    cmd.cmd_02(dev, "\x91\x00\x90\x68\x09\x00")
    # Generated from packet 2721/2722
    cmd.cmd_57s(dev, "\x90", "\xFF\xFF")
    # Generated from packet 2725/2726
    cmd.cmd_57s(dev, "\x8C", "\x00\x00")
    # Generated from packet 2729/2730
    cmd.cmd_50(dev, "\x0D\x00")
    # Generated from packet 2731/2732
    buff = cmd.bulk2b(dev, "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00")
    validate_read("\x91\x00", buff, "packet W: 2731/2732, R 1 to 2733/2734")
    # Generated from packet 2735/2736
    cmd.cmd_02(dev, "\x92\x00\xA0\x68\x09\x00")
    # Generated from packet 2739/2740
    bulkWrite(0x02, "\x57\x91\x00\x50\x1A\x00\x00\x00")
    # Generated from packet 2741/2742
    buff = cmd.bulk2b(dev, 
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00\x66\xB9\x00" \
        "\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x92\x00", buff, "packet W: 2741/2742, R 1 to 2743/2744")
    # Generated from packet 2745/2746
    cmd.cmd_02(dev, "\x93\x00\xC0\x68\x09\x00")
    # Generated from packet 2749/2750
    cmd.cmd_57s(dev, "\x92", "\x00\x00")
    # Generated from packet 2753/2754
    cmd.led_mask(dev, "pass")
    # Generated from packet 2757/2758
    cmd.gpio_readi(dev)
    # Generated from packet 2761/2762
    cmd.gpio_readi(dev)
    # Generated from packet 2765/2766
    cmd.sm_info22(dev)
    # Generated from packet 2769/2770
    cmd.sm_info24(dev)
    # Generated from packet 2773/2774
    cmd.sm_read(dev)
    # Generated from packet 2777/2778
    cmd.cmd_49(dev)
    # Generated from packet 2781/2782
    cmd.sm_read(dev)
    # Generated from packet 2785/2786
    cmd.sm_insert(dev)
    # Generated from packet 2789/2790
    cmd.sm_info10(dev)

    return {'code': code, 'data': None, 'config': None}














































class PIC17C43(bpmicro.device.Device):
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
