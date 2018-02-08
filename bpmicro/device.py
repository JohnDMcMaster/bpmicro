from bpmicro.cmd import Unsupported

class Device(object):
    def read(self, opts):
        '''
        Returns the devcfg structure write uses
        
        opts: cont standard
        '''
        raise Unsupported()

    def program(self, devcfg, opts):
        '''
        devcfg: device configuration. A dict containining areas to configure
        Standard keys are:
        -code: the primary memory such as EPROM, flash ,etc
        -data: secondary memory, if applicable, such as EEPROM
        -config: misc fuses not in a main configuration area
        -blank_check: don't program unless blank
        Most devices will only have a single entry named "code"
        For consistency, use code even if its generic memory such as EPROM

        opts: operation options
        Standard keys are:
        cont: whether to do continuity check
        erase: whether to erase
        verify: whether to readback result
        '''
        raise Unsupported()

    def sum(self, opts):
        raise Unsupported()

    def blank(self, opts):
        raise Unsupported()

    def erase(self, opts):
        raise Unsupported()

    def secure(self, opts):
        raise Unsupported()

    @staticmethod
    def print_config(config):
        print config
