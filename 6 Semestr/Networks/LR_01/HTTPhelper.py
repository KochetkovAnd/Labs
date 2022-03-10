import socket

bufferSize = 1024

class HTTPHelper():    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.createConnection(host, port)

    def createConnection(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def sendRequest(self, info, host):

        request = "GET "+info+" HTTP/1.1\r\n"
        request += "Host:"+host+"\r\n"
        request += "Connection:close\r\n\r\n"

        self.socket.send(request.encode())

    def getResponse(self):
        data = ""
        d = repr(self.socket.recv(bufferSize))
        while d:
            data += str(d)
            d = self.socket.recv(bufferSize)
        return data 