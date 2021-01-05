import hashlib


def lillte_endian_on_int(b):
    return int.from_bytes(b, 'little')


def int_to_little_endian(n, length):
    return n.to_bytes(length, 'little')


def hash160(s):
    """ return hash value after sha256 followed by ripemd160 """
    return hashlib.new('ripemd160', hashlib.sha256(s).digest()).digest()


def hash256(s):
    """return hash value after two times sha256"""
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdedfhijkmnopqrstuvwxyz'


def encode_base58(s):
    count = 0
    for c in s:
        if c == 0:
            count += 1
        else:
            break
    num = int.from_bytes(s, 'big')
    prefix = '1' * count
    result = ''
    while num > 0:
        num, mod = divmod(num, 58)
        result = BASE58_ALPHABET[mod] + result
    return prefix + result


def encode_base58_checksum(s):
    return encode_base58(s + hash256(s)[:4])
