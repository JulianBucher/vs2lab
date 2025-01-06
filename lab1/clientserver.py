"""
Client and server using classes
"""

import logging
import socket

import const_cs
from context import lab_logging

lab_logging.setup(stream_level=logging.INFO)  # init loging channels for the lab

# pylint: disable=logging-not-lazy, line-too-long

class Server:
    """ The server """
    _logger = logging.getLogger("vs2lab.lab1.clientserver.Server")
    _serving = True
    telefon_db = { 'alice': 1234567,
        'bob': 2345678,
        'carol': 3456789
    }
    def handle_request(self, request):
        """ Handle GET and GETALL requests """
        if request.startswith("GET "):
            name = str(request[4:]).lower()
            return self.telefon_db[name]
        elif request == "GETALL":
            return str(self.telefon_db)
        else:
            return "Unbekannte Anfrage"

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # prevents errors due to "addresses in use"
        self.sock.bind((const_cs.HOST, const_cs.PORT))
        self.sock.settimeout(3)  # time out in order not to block forever
        self._logger.info("Server bound to socket " + str(self.sock))

    def serve(self):
        """ Serve echo """
        self.sock.listen(1)
        while self._serving:  # as long as _serving (checked after connections or socket timeouts)
            try:
                # pylint: disable=unused-variable
                (connection, address) = self.sock.accept()  # returns new socket and address of client
                while True:  # forever
                    data = connection.recv(1024)  # receive data from client
                    if not data:
                        break  # stop if client stopped
                    self._logger.info("Sending data thorugh socket")
                    request = data.decode('ascii')
                    response = self.handle_request(request)
                    connection.send(str(response).encode('ascii'))
                    #connection.send(data.decode).encode('ascii')
#                    connection.send(data + "*".encode('ascii'))  # return sent data plus an "*"
                connection.close()  # close the connection
            except socket.timeout:
                pass  # ignore timeouts
        self.sock.close()
        self._logger.info("Server down.")


class Client:
    """ The client """
    logger = logging.getLogger("vs2lab.a1_layers.clientserver.Client")



    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((const_cs.HOST, const_cs.PORT))
        self.logger.info("Client connected to socket " + str(self.sock))

    def call(self, request):
        """ Call server """
        self.sock.send(str(request).encode('ascii'))  # send encoded string as data
        data = self.sock.recv(1024)  # receive the response
        self.logger.info("receiving answer from socket")
        msg_out = str(data.decode('ascii'))
        print(msg_out)  # print the result
        self.sock.close()  # close the connection
        self.logger.info("Client down.")
        return msg_out

    def getall(self):
        return self.call("GETALL")

    def get(self, name):
        return self.call(name)

    def close(self):
        """ Close socket """
        self.logger.info("closing socket.")
        self.sock.close()
