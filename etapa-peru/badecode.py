def str_xor(secret, key):
    # extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])


flag_enc = chr(0x01) + chr(0x21) + chr(0x08) + chr(0x19) + chr(0x21) + chr(0x51) + chr(0x5c) + chr(0x40) + chr(
    0x3a) + chr(0x24) + chr(0x5d) + chr(0x21) + chr(0x20) + chr(0x07) + chr(0x0a) + chr(0x04),

print(flag_enc)
flag = str_xor(flag_enc[0], 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)
