import socket


class ISocket:
    def __init__(self, host: str, port: int):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        self.buffer = b''

    def recv_until(self, until: str or bytes, debug=False):
        self.buffer = b''
        if isinstance(until, str):
            until = until.encode()
        while not self.buffer.endswith(until):
            self.buffer += self.sock.recv(1)
        return self.buffer.decode()

    def send(self, data: str or bytes):
        if isinstance(data, str):
            data = data.encode()
        self.sock.send(data + b'\n')
        print(data)

    def close(self):
        self.sock.close()
