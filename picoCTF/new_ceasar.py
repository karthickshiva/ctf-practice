import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

'''
def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc
'''


def b16_decode(enc):
    plain = ""
    for i in range(0, len(enc), 2):
        bin_value = "{0:04b}".format(ord(enc[i]) - LOWERCASE_OFFSET)
        bin_value += "{0:04b}".format(ord(enc[i + 1]) - LOWERCASE_OFFSET)
        int_value = int(bin_value, 2)
        plain += chr(int_value)
    return plain


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


flag = 'dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac'


def solve(encrypted_flag):
    for i in range(16):
        rotated_flag = ""
        for c in encrypted_flag:
            rotated_flag += shift(c, chr((LOWERCASE_OFFSET + i) % len(ALPHABET)))
        decoded_flag = b16_decode(rotated_flag)
        if decoded_flag.isprintable():
            print(decoded_flag)


solve(flag)

'''
flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])
print(enc)
'''
