import socket

class Network:
    def __init__(self, port):
        self.ip = ip
        self.port = port
        s = socket.socket()
        print("Socket created successfully")
        s.bind((socket.gethostname(), port)
        print("Socket bound to port " + port)
        s.listen(5)
        print("Socket is listening")
        c, addr = s.accept()
        self.c = c
        print("Connection established with " + addr)

    def alert_server(self, msg):
        byt = msg.encode()
        self.c.send(byt)

    def close_connection(self):
        self.c.close()
