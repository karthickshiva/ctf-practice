from util.interactive_socket import ISocket
from binascii import unhexlify

socket = ISocket('mercury.picoctf.net', 36981)

output = socket.recv_until('What data would you like to encrypt? ')
output = output.split('\n')
encrypted_flag_hex = output[2]
encrypted_flag = unhexlify(encrypted_flag_hex)
socket.send(b'a' * (50000 - len(encrypted_flag)))
socket.recv_until('What data would you like to encrypt? ')
socket.send(encrypted_flag)
output = socket.recv_until('What data would you like to encrypt? ')
flag_hex = output.split('\n')[1]
print(unhexlify(flag_hex).decode())



