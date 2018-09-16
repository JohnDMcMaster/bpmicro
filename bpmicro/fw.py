import fnmatch
import os
import md5
import binascii

FW_DIR = os.path.join(os.path.dirname(__file__), 'fw')

# md5 hash to file content
hash2bin = {}
# absolute paths
hash2fn = {}

def hash2fn_get_rel(h, default=None):
    fn = hash2fn.get(h, default)
    if fn is None:
        return fn
    return fn.replace(FW_DIR + '/', '')

def fwhash(data):
    return binascii.hexlify(str(md5.new(data).digest()))[0:8]

def files_of_ext(srcdir, ext):
    matches = []
    for root, dirnames, filenames in os.walk(srcdir):
        for filename in fnmatch.filter(filenames, '*.' + ext):
            matches.append(os.path.join(root, filename))
    return matches

def reindex():
    hash2bin.clear()
    for f in files_of_ext(FW_DIR, 'bin'):
        b = open(f, 'r').read()
        h = fwhash(b)
        if h in hash2bin:
            assert hash2bin[h] == b, 'Hash collision!'
            print('WARNING: duplicate firmware w/ hash %s' % h)
            continue
        hash2bin[h] = b
        hash2fn[h] = f

reindex()
