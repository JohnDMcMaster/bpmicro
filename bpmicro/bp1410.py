class BP1410(object):
    def __init__(self, dev, usbcontext, verbose=False):
        self.dev = dev
        self.usbcontext = usbcontext
        self.timeout = 1000
        self.verbose = verbose

    def bulkRead(self, endpoint, length, timeout=None):
        timeout = timeout if timeout is not None else self.timeout
        return self.dev.bulkRead(endpoint, length, timeout=timeout)

    def bulkWrite(self, endpoint, data, timeout=None):
        timeout = timeout if timeout is not None else self.timeout
        self.dev.bulkWrite(endpoint, data, timeout=timeout)
    
    def controlRead(self, request_type, request, value, index, length,
                    timeout=None):
        timeout = timeout if timeout is not None else self.timeout
        return self.dev.controlRead(request_type, request, value, index, length,
                    timeout=timeout)

    def controlWrite(self, request_type, request, value, index, data,
                     timeout=None):
        timeout = timeout if timeout is not None else self.timeout
        self.dev.controlWrite(request_type, request, value, index, data,
                     timeout=timeout)
