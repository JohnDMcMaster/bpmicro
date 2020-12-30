import fnmatch
import os
import hashlib
import binascii

FW_DIR = os.path.join(os.path.dirname(__file__), 'fw')

# md5 hash to file content
hash2bin = {}
# absolute paths
hash2fns = {}


def fn2rel(fn):
    return fn.replace(FW_DIR + '/', '')


def hash2fns_get_rel(h, default=None):
    fns = hash2fns.get(h, default)
    if fns is None:
        return None
    return [fn2rel(fn) for fn in fns]


def fwhash(data):
    return binascii.hexlify(hashlib.md5(data).digest())[0:8]


def files_of_ext(srcdir, ext):
    matches = []
    for root, dirnames, filenames in os.walk(srcdir):
        for filename in fnmatch.filter(filenames, '*.' + ext):
            matches.append(os.path.join(root, filename))
    return matches


def reindex():
    hash2bin.clear()
    for f in files_of_ext(FW_DIR, 'bin'):
        b = open(f, 'rb').read()
        h = fwhash(b)
        if h in hash2bin:
            assert hash2bin[h] == b, 'Hash collision!'
            #print('WARNING: duplicate firmware w/ hash %s' % h)
        else:
            hash2bin[h] = b
        hash2fns.setdefault(h, set()).add(f)


reindex()
