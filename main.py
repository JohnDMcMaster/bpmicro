from bpmicro import startup
from bpmicro import devices
from bpmicro.util import hexdump, add_bool_arg

def run(operation, device,
        code_fn, data_fn, config_fn,
        cont, erase, verify, verbose, dir_, init=True):
    device_str = device
    '''
    Device: chip model
    '''
    bp = None
    device = None
    if operation != 'list_device':
        bp = startup.get(verbose=verbose, init=init)
        if operation != 'nop':
            device = devices.get(bp, device_str, verbose=verbose)

    opts = {
        'cont': cont,
        'erase': erase,
        'verify': verify,
        'verbose': verbose,
        }

    if operation == 'list_device':
        print 'Devices:'
        for device in sorted(devices.class_s2c.keys()):
            print device
    elif operation == 'nop':
        pass
    elif operation == 'program':
        devcfg = {}
        devcfg['code'] = open(code_fn, 'r').read()
        if data_fn:
            devcfg['data'] = open(data_fn, 'r').read()
        if config_fn:
            devcfg['config'] = open(config_fn, 'r').read()
        device.program(devcfg, opts)
    elif operation == 'verify':
        raise Exception('FIXME')
    elif operation == 'compare':
        raise Exception('FIXME')
    elif operation == 'read':
        devcfg = device.read(opts)
        code = devcfg['code']
        data = devcfg.get('data', None)
        config = devcfg.get('config', None)
        if not code_fn:
            if dir_:
                raise Exception('FIXME')
            else:
                print
                hexdump(code, indent='  ', label='Code')
    
                if data:
                    print
                    hexdump(data, indent='  ', label='Data')
    
                if config:
                    print
                    print 'Configuration'
                    device.print_config(config)
        else:
            print 'Writing to %s' % code_fn
            open(code_fn, 'w').write(code)
    
        print 'Complete'
    elif operation == 'sum':
        raise Exception('FIXME')
    elif operation == 'blank':
        raise Exception('FIXME')
    elif operation == 'erase':
        raise Exception('FIXME')
    elif operation == 'secure':
        raise Exception('FIXME')
    else:
        raise Exception("Bad operation %s" % operation)

def main():
    import argparse 
    
    parser = argparse.ArgumentParser(description='Read/write device w/ BP Microsystems programmer')
    add_bool_arg(parser, '--cont', default=True, help='Continuity check') 
    add_bool_arg(parser, '--erase', default=None, help='Erase device (write only)') 
    add_bool_arg(parser, '--verify', default=True, help='Read back after write (write only)') 
    add_bool_arg(parser, '--verbose', default=True, help='More verbose output') 
    add_bool_arg(parser, '--dir', default=None, help='Force input/output directory') 
    add_bool_arg(parser, '--init', default=True, help='Advanced / developer only') 
    parser.add_argument('operation', help='Operation: read, program, erase, protect, list_device, nop') 
    parser.add_argument('device', nargs='?', help='Device to use') 
    parser.add_argument('code', nargs='?', help='Read/write input/output file or directory: primary data such as EPROM or flash') 
    parser.add_argument('data', nargs='?', help='Read/write input/output file: secondary data such as EEPROM') 
    parser.add_argument('config', nargs='?', help='Read/write input/output file or directory: additional configuration') 
    args = parser.parse_args()

    run(args.operation, args.device,
            code_fn=args.code, data_fn=args.data, config_fn=args.config,
            cont=args.cont, erase=args.erase, verify=args.verify, verbose=args.verbose, dir_=args.dir, init=args.init)

if __name__ == "__main__":
    main()
