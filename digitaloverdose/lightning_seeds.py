from binascii import unhexlify
import random

encrypted_flag = '4fcbac835550403f13c4cc337d8d8da48351921dfb7cd47d33857432c2ee665d821227'
encrypted_flag_bytes = unhexlify(encrypted_flag)


def decrypt(seed):
    random.seed(seed)
    new_bytes = []
    for byte in encrypted_flag_bytes:
        new_bytes.append(byte ^ random.randint(0, 255))
    flag = "".join(chr(x) for x in new_bytes)
    if "DOCTF" in flag:
        print(flag)


for i in range(1000):
    decrypt(i)
