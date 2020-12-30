# Based off of 17_read-cont-y_cold.cap
# md5 0fdb988186be94a062adc9d1c0019463

from bpmicro import cmd
from bpmicro.usb import validate_read
from bpmicro.usb import usb_wraps
import bpmicro.device
import struct
import binascii

import bpmicro.pic.pic16f84_fw
import bpmicro.pic.pic17c43_fw


def dev_read(dev, cont=False, verbose=False):
    bulkRead, bulkWrite, controlRead, controlWrite = usb_wraps(dev)
    config = {}

    # Generated from packet 2237/2238
    # NOTE:: req max 4096 but got 3
    buff = controlRead(0xC0, 0xB0, 0x0000, 0x0000, 4096)
    # Req: 4096, got: 3
    validate_read("\x00\x00\x00", buff, "packet 2237/2238")
    # Generated from packet 2239/2240
    _prefix, buff, _size = cmd.bulk86_next_read(dev)
    validate_read("\x16", buff, "packet 2239/2240")
    # NOTE:: req max 512 but got 136
    # Generated from packet 2245/2246
    # bulk2 aggregate: packet W: 2245/2246, 1 to R 2247/2248
    buff = cmd.bulk2b(dev,
        "\x43\x19\x20\x00\x00\x3B\x7E\x25\x00\x00\xFE\xFF\x3B\x7C\x25\x00" \
        "\x00\xFE\xFF\x00"
        )
    validate_read("\xA4\x06", buff, "packet W: 2245/2246, R 1 to 2247/2248")
    # NOTE:: req max 512 but got 35
    # Generated from packet 2257/2258
    # bulk2 aggregate: packet W: 2257/2258, 1 to R 2259/2260
    buff = cmd.bulk2b(dev,
        "\x14\x38\x25\x00\x00\x04\x00\x90\x32\x90\x00\xA7\x02\x1F\x00\x14" \
        "\x40\x25\x00\x00\x01\x00\x3C\x36\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 2257/2258, R 1 to 2259/2260")
    # NOTE:: req max 512 but got 107
    # Generated from packet 2287/2288
    bulkWrite(0x02, "\x43\x19\x20\x00\x00")
    # Generated from packet 2289/2290
    bulkWrite(0x02, "\x20\x01\x00\x0C\x04")
    # Generated from packet 2291/2292
    cmd.cmd_41(dev)
    # Generated from packet 2293/2294
    # bulk2 aggregate: packet W: 2293/2294, 1 to R 2295/2296
    cmd.cmd_10(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2305/2306
    # bulk2 aggregate: packet W: 2305/2306, 1 to R 2307/2308
    cmd.cmd_45(dev)
    # NOTE:: req max 512 but got 103
    # Generated from packet 2309/2310
    # bulk2 aggregate: packet W: 2309/2310, 1 to R 2311/2312
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 35
    # Generated from packet 2333/2334
    # bulk2 aggregate: packet W: 2333/2334, 1 to R 2335/2336
    cmd.cmd_49(dev)
    # NOTE:: req max 512 but got 11
    # Generated from packet 2351/2352
    cmd.cmd_3B(dev)
    # Generated from packet 2353/2354
    # bulk2 aggregate: packet W: 2353/2354, 1 to R 2355/2356
    cmd.cmd_4A(dev)
    # NOTE:: req max 512 but got 5
    # Generated from packet 2357/2358
    cmd.cmd_4C(dev)
    # Generated from packet 2359/2360
    buff = controlWrite(0x40, 0xB2, 0x0000, 0x0000, "")
    # Generated from packet 2363/2364
    cmd.cmd_50(dev, "\x45\x00")
    # Generated from packet 2365/2366
    # bulk2 aggregate: packet W: 2365/2366, 1 to R 2367/2368
    buff = cmd.bulk2b(dev,
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x10" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\xE9\x03\x00\x00\x00\x90\x01\x80" \
        "\xE9\x02\x00\x00\x00\x90\x00\xE9\x04\x00\x00\x00\x00\x00\x00\x00" \
        "\xE9\x03\x00\x00\x00\x90\x00\x00\x66\xB9\x00\x00\xB2\x00\xFB\xFF" \
        "\x25\x44\x11\x00\x00"
        )
    validate_read("\x80\x00", buff, "packet W: 2365/2366, R 1 to 2367/2368")
    # Generated from packet 2371/2372
    # bulk2 aggregate: packet W: 2371/2372, 1 to R 2373/2374
    cmd.cmd_02(dev, "\x81\x00\x50\x00\x09\x00")
    # Generated from packet 2375/2376
    cmd.cmd_50(dev, "\xC0\x00")
    # Generated from packet 2377/2378
    # bulk2 aggregate: packet W: 2377/2378, 1 to R 2381/2382
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
    # bulk2 aggregate: packet W: 2383/2384, 1 to R 2385/2386
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2387/2388
    bulkWrite(0x02,
        "\x04\x20\x05\x3D\x06\x20\x07\x64\x08\x6F\x09\x63\x0A\x75\x0B\x6D" \
        "\x57\x81\x00"
        )
    # Generated from packet 2393/2394
    # bulk2 aggregate: packet W: 2393/2394, 1 to R 2395/2396
    cmd.cmd_02(dev, "\x82\x00\x10\x01\x09\x00")
    # Generated from packet 2397/2398
    # bulk2 aggregate: packet W: 2397/2398, 1 to R 2399/2402
    cmd.led_mask(dev, "active")
    # Generated from packet 2403/2404
    cmd.cmd_50(dev, "\x18\x00")
    # Generated from packet 2405/2406
    # bulk2 aggregate: packet W: 2405/2406, 1 to R 2407/2408
    buff = cmd.bulk2b(dev,
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x82\x00", buff, "packet W: 2405/2406, R 1 to 2407/2408")
    # Generated from packet 2411/2412
    # bulk2 aggregate: packet W: 2411/2412, 1 to R 2413/2414
    cmd.cmd_02(dev, "\x83\x00\x30\x01\x09\x00")
    # Generated from packet 2415/2416
    # bulk2 aggregate: packet W: 2415/2416, 1 to R 2417/2428
    buff = cmd.bulk2b(dev,
        "\x57\x82\x00\x20\x01\x00\x2B\x3B\x0C\x22\x00\xC0\x40\x00\x3B\x0E" \
        "\x22\x00\xC0\x00\x00\x3B\x1A\x22\x00\xC0\x18\x00\x0E\x01"
        )
    validate_read(
        "\x14\x00\x54\x41\x38\x34\x56\x4C\x56\x5F\x46\x58\x34\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x2C"
        , buff, "packet W: 2415/2416, R 1 to 2417/2428")
    # Generated from packet 2455/2456
    # bulk2 aggregate: packet W: 2455/2456, 1 to R 2457/2458
    buff = cmd.bulk2b(dev, "\x48\x00\x10\x82\x02")
    validate_read("\x82\x00\x10\x01\x09\x00", buff,
                  "packet W: 2455/2456, R 1 to 2457/2458")
    # Generated from packet 2461/2462
    bulkWrite(0x02, "\x20\x01\x00\x50\x7D\x02\x00\x00")
    # Generated from packet 2463/2464
    # bulk2 aggregate: packet W: 2463/2464, 1 to R 2465/2466
    buff = cmd.bulk2b(dev, bpmicro.pic.pic16f84_fw.p651)
    validate_read("\x82\x00", buff, "packet W: 2463/2464, R 1 to 2465/2466")
    # Generated from packet 2467/2468
    # bulk2 aggregate: packet W: 2467/2468, 1 to R 2469/2470
    cmd.cmd_02(dev, "\x83\x00\x90\x03\x09\x00")
    # Generated from packet 2471/2472
    bulkWrite(0x02, "\x57\x82\x00\x50\x1D\x00\x00\x00")
    # Generated from packet 2473/2474
    # bulk2 aggregate: packet W: 2473/2474, 1 to R 2475/2476
    buff = cmd.bulk2b(dev,
        "\xC7\x05\x74\x46\x00\x00\x0B\x00\x00\x00\xFF\x15\x38\x11\x00\x00" \
        "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x83\x00", buff, "packet W: 2473/2474, R 1 to 2475/2476")
    # Generated from packet 2477/2478
    # bulk2 aggregate: packet W: 2477/2478, 1 to R 2479/2480
    cmd.cmd_02(dev, "\x84\x00\xB0\x03\x09\x00")
    # Generated from packet 2481/2482
    bulkWrite(0x02, "\x57\x83\x00\x50\x18\x3A\x00\x00")
    # Generated from packet 2483/2484
    # bulk2 aggregate: packet W: 2483/2484, 1 to R 2485/2486
    buff = cmd.bulk2b(dev, bpmicro.pic.pic16f84_fw.p533)
    validate_read("\x84\x00", buff, "packet W: 2483/2484, R 1 to 2485/2486")
    # Generated from packet 2487/2488
    # bulk2 aggregate: packet W: 2487/2488, 1 to R 2489/2490
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
    # bulk2 aggregate: packet W: 2495/2496, 1 to R 2497/2498
    buff = cmd.bulk2b(dev, bpmicro.pic.pic16f84_fw.p555)
    validate_read("\x85\x00", buff, "packet W: 2495/2496, R 1 to 2497/2498")
    # Generated from packet 2499/2500
    # bulk2 aggregate: packet W: 2499/2500, 1 to R 2501/2502
    cmd.cmd_02(dev, "\x86\x00\xB0\x41\x09\x00")

    if cont:
        # Generated from packet 2503/2504
        # bulk2 aggregate: packet W: 2503/2504, 1 to R 2505/2506
        cmd.check_cont(dev)

    # Generated from packet 2507/2508
    cmd.cmd_50(dev, "\x62\x00")
    # Generated from packet 2509/2510
    # bulk2 aggregate: packet W: 2509/2510, 1 to R 2511/2512
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
    # bulk2 aggregate: packet W: 2513/2514, 1 to R 2515/2516
    cmd.cmd_02(dev, "\x87\x00\x20\x42\x09\x00")
    # Generated from packet 2517/2518
    bulkWrite(0x02,
        "\x1D\xB0\x41\x09\x00\x28\x00\x15\x60\x00\x02\x00\x00\x00\x00\x00" \
        "\x01\x00\x00\x00\x00\x00\x1C\x30\x00\x00\x02\x00\x00\x40\x00\x48" \
        "\x00\x50\x71\x09\x00\x00"
        )
    # Generated from packet 2519/2520
    # bulk2 aggregate: packet W: 2519/2520, 1 to R 2521/2522
    buff = cmd.bulk2b(dev, bpmicro.pic.pic17c43_fw.p2519)
    validate_read("\x87\x00", buff, "packet W: 2519/2520, R 1 to 2521/2522")
    # Generated from packet 2523/2524
    # bulk2 aggregate: packet W: 2523/2524, 1 to R 2525/2526
    cmd.cmd_02(dev, "\x88\x00\xA0\x4B\x09\x00")
    # Generated from packet 2527/2528
    # bulk2 aggregate: packet W: 2527/2528, 1 to R 2529/2530
    cmd.cmd_57s(dev, "\x87", "\x00\x00")
    # Generated from packet 2531/2532
    cmd.cmd_50(dev, "\x17\x00")
    # Generated from packet 2533/2534
    # bulk2 aggregate: packet W: 2533/2534, 1 to R 2535/2536
    buff = cmd.bulk2b(dev,
        "\xC7\x05\x2C\x00\x09\x00\x24\x04\x00\x00\x66\xB9\x00\x00\xB2\x00" \
        "\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x88\x00", buff, "packet W: 2533/2534, R 1 to 2535/2536")
    # Generated from packet 2537/2538
    # bulk2 aggregate: packet W: 2537/2538, 1 to R 2539/2540
    cmd.cmd_02(dev, "\x89\x00\xC0\x4B\x09\x00")
    # Generated from packet 2543/2544
    bulkWrite(0x02, "\x57\x88\x00\x50\x18\x00\x00\x00")
    # Generated from packet 2545/2546
    # bulk2 aggregate: packet W: 2545/2546, 1 to R 2547/2548
    buff = cmd.bulk2b(dev,
        "\x66\xB8\x01\x32\x66\x89\x05\x06\x00\x09\x00\x66\xB9\x00\x00\xB2" \
        "\x00\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x89\x00", buff, "packet W: 2545/2546, R 1 to 2547/2548")
    # Generated from packet 2549/2550
    # bulk2 aggregate: packet W: 2549/2550, 1 to R 2551/2552
    cmd.cmd_02(dev, "\x8A\x00\xE0\x4B\x09\x00")
    # Generated from packet 2553/2554
    bulkWrite(0x02, "\x57\x89\x00\x50\x04\x0A\x00\x00")
    # Generated from packet 2555/2556
    # bulk2 aggregate: packet W: 2555/2556, 1 to R 2557/2558
    buff = cmd.bulk2b(dev, bpmicro.pic.pic17c43_fw.p2555)
    validate_read("\x8A\x00", buff, "packet W: 2555/2556, R 1 to 2557/2558")
    # Generated from packet 2559/2560
    # bulk2 aggregate: packet W: 2559/2560, 1 to R 2561/2562
    cmd.cmd_02(dev, "\x8B\x00\xF0\x55\x09\x00")
    # Generated from packet 2563/2564
    # bulk2 aggregate: packet W: 2563/2564, 1 to R 2565/2566
    cmd.cmd_57s(dev, "\x8A", "\x00\x00")
    # Generated from packet 2567/2568
    cmd.cmd_50(dev, "\xBE\x03")
    # Generated from packet 2569/2570
    # bulk2 aggregate: packet W: 2569/2570, 1 to R 2571/2572
    buff = cmd.bulk2b(dev, bpmicro.pic.pic17c43_fw.p2569)
    validate_read("\x8B\x00", buff, "packet W: 2569/2570, R 1 to 2571/2572")
    # Generated from packet 2573/2574
    # bulk2 aggregate: packet W: 2573/2574, 1 to R 2575/2576
    cmd.cmd_02(dev, "\x8C\x00\xB0\x59\x09\x00")

    # Generated from packet 2577/2578
    # bulk2 aggregate: packet W: 2577/2578, 1 to R 2581/2582
    buff = cmd.bulk2b(dev, "\x08\x01\x57\x8B\x00")
    #validate_read("\x00\x00", buff, "packet W: 2577/2578, R 1 to 2581/2582")
    config['secure'] = buff != '\x00\x00'

    # Generated from packet 2583/2584
    cmd.cmd_50(dev, "\x1B\x04")
    # Generated from packet 2585/2586
    # bulk2 aggregate: packet W: 2585/2586, 1 to R 2587/2588
    buff = cmd.bulk2b(dev, bpmicro.pic.pic17c43_fw.p2585)
    validate_read("\x8C\x00", buff, "packet W: 2585/2586, R 1 to 2587/2588")
    # Generated from packet 2589/2590
    # bulk2 aggregate: packet W: 2589/2590, 1 to R 2591/2592
    cmd.cmd_02(dev, "\x8D\x00\xD0\x5D\x09\x00")
    # Generated from packet 2593/2594
    # bulk2 aggregate: packet W: 2593/2594, 1 to R 2597/2600
    cmd.cmd_57s(dev, "\x8C", "\x00\x00")
    # Generated from packet 2603/2604
    # bulk2 aggregate: packet W: 2603/2604, 1 to R 2605/2606
    cmd.cmd_57s(dev, "\x89\x8A", "\x00\x00")
    # Generated from packet 2609/2610
    cmd.cmd_50(dev, "\x12\x03")
    # Generated from packet 2611/2612
    # bulk2 aggregate: packet W: 2611/2612, 1 to R 2613/2614
    buff = cmd.bulk2b(dev, bpmicro.pic.pic17c43_fw.p2611)
    validate_read("\x8D\x00", buff, "packet W: 2611/2612, R 1 to 2613/2614")
    # Generated from packet 2617/2618
    # bulk2 aggregate: packet W: 2617/2618, 1 to R 2619/2620
    cmd.cmd_02(dev, "\x8E\x00\xF0\x60\x09\x00")
    # Generated from packet 2621/2622
    # bulk2 aggregate: packet W: 2621/2622, 17 to R 2681/2682
    main_read = cmd.bulk2b(dev,
        "\x04\x00\x05\x00\x06\x00\x07\x00\x08\x00\x09\x10\x0A\x00\x0B\x00" \
        "\x57\x8D\x00"
        )
    #validate_read(bpmicro.pic.pic17c43_fw.p2681, buff, "packet W: 2621/2622, R 17 to 2681/2682")
    # Generated from packet 2683/2684
    cmd.cmd_50(dev, "\x5E\x00")
    # Generated from packet 2685/2686
    # bulk2 aggregate: packet W: 2685/2686, 1 to R 2687/2688
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
    # bulk2 aggregate: packet W: 2689/2690, 1 to R 2691/2692
    cmd.cmd_02(dev, "\x8F\x00\x50\x61\x09\x00")
    # Generated from packet 2693/2694
    # bulk2 aggregate: packet W: 2693/2694, 1 to R 2695/2696
    cmd.cmd_57s(dev, "\x8E", "\x00\x00")
    # Generated from packet 2697/2698
    cmd.cmd_50(dev, "\x96\x06")
    # Generated from packet 2699/2700
    # bulk2 aggregate: packet W: 2699/2700, 1 to R 2701/2702
    buff = cmd.bulk2b(dev, bpmicro.pic.pic17c43_fw.p2699)
    validate_read("\x8F\x00", buff, "packet W: 2699/2700, R 1 to 2701/2702")
    # Generated from packet 2703/2704
    # bulk2 aggregate: packet W: 2703/2704, 1 to R 2705/2706
    cmd.cmd_02(dev, "\x90\x00\xF0\x67\x09\x00")
    # Generated from packet 2707/2708
    # bulk2 aggregate: packet W: 2707/2708, 1 to R 2709/2710
    cmd.cmd_57s(dev, "\x8F", "\x00\x00")
    # Generated from packet 2711/2712
    cmd.cmd_50(dev, "\x92\x00")
    # Generated from packet 2713/2714
    # bulk2 aggregate: packet W: 2713/2714, 1 to R 2715/2716
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
    # bulk2 aggregate: packet W: 2717/2718, 1 to R 2719/2720
    cmd.cmd_02(dev, "\x91\x00\x90\x68\x09\x00")

    # Generated from packet 2721/2722
    # bulk2 aggregate: packet W: 2721/2722, 1 to R 2723/2724
    # Orig: "\xFF\xFF"
    buff = cmd.cmd_57s(dev, "\x90", None)

    def unpackw(buff):
        struct.unpack('<H', buff)[0]

    if verbose:
        print('2721/2722: %s' % binascii.hexlify(buff))

    # FIXME: confirm
    config['conf_word'] = unpackw(buff)

    # Generated from packet 2725/2726
    # bulk2 aggregate: packet W: 2725/2726, 1 to R 2727/2728
    cmd.cmd_57s(dev, "\x8C", "\x00\x00")

    # Generated from packet 2729/2730
    cmd.cmd_50(dev, "\x0D\x00")
    # Generated from packet 2731/2732
    # bulk2 aggregate: packet W: 2731/2732, 1 to R 2733/2734
    buff = cmd.bulk2b(dev,
                      "\x66\xB9\x00\x00\xB2\x00\xFB\xFF\x25\x44\x11\x00\x00")
    validate_read("\x91\x00", buff, "packet W: 2731/2732, R 1 to 2733/2734")
    # Generated from packet 2735/2736
    # bulk2 aggregate: packet W: 2735/2736, 1 to R 2737/2738
    cmd.cmd_02(dev, "\x92\x00\xA0\x68\x09\x00")
    # Generated from packet 2739/2740
    bulkWrite(0x02, "\x57\x91\x00\x50\x1A\x00\x00\x00")
    # Generated from packet 2741/2742
    # bulk2 aggregate: packet W: 2741/2742, 1 to R 2743/2744
    buff = cmd.bulk2b(dev,
        "\x66\xB9\x00\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00\x66\xB9\x00" \
        "\x00\xB2\x02\xFB\xFF\x25\x44\x11\x00\x00"
        )
    validate_read("\x92\x00", buff, "packet W: 2741/2742, R 1 to 2743/2744")
    # Generated from packet 2745/2746
    # bulk2 aggregate: packet W: 2745/2746, 1 to R 2747/2748
    cmd.cmd_02(dev, "\x93\x00\xC0\x68\x09\x00")
    # Generated from packet 2749/2750
    # bulk2 aggregate: packet W: 2749/2750, 1 to R 2751/2752
    cmd.cmd_57s(dev, "\x92", "\x00\x00")
    # Generated from packet 2753/2754
    # bulk2 aggregate: packet W: 2753/2754, 1 to R 2755/2756
    cmd.led_mask(dev, "pass")
    # Generated from packet 2777/2778
    # bulk2 aggregate: packet W: 2777/2778, 1 to R 2779/2780
    cmd.cmd_49(dev)

    # Is it the full area or just the first half?
    # Ambiguous word vs byte
    # looks like upper memory has misc internal chip data
    # Fairly certain we just want this
    code = main_read[0:4 * 1024]
    #code = main_read
    fuses_buff = main_read[0x1FF0:0x2000]

    def fuse_unpack(buff, i):
        return struct.unpack('<H', buff[2 * i:2 * i + 2])[0]

    for i in range(0, 4):
        config['user_id%d' % i] = fuse_unpack(fuses_buff, i)

    return {'code': code, 'config': config}


class PIC17C43(bpmicro.device.Device):
    def __init__(self, dev, verbose=False):
        self.verbose = verbose
        self.dev = dev

    def read(self, opts):
        return dev_read(dev=self.dev,
                        cont=opts.get('cont', True),
                        verbose=opts.get('verbose', False))

    @staticmethod
    def print_config(config):
        for i in range(0, 4):
            print('  user_id%d:  0x%04X' % (i, config['user_id%d' % i]))
        #print '  conf_word: 0x%04X' % (config['conf_word'])
        print('  secure: %s' % (config['secure']))
