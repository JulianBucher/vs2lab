import constRPC
import rpc
import logging
import time
import threading
from context import lab_channel


class DBList:
    def __init__(self, basic_list):
        self.value = list(basic_list)

    def append(self, data):
        self.value = self.value + [data]
        return self


class Client:
    def __init__(self):
        self.chan = lab_channel.Channel()
        self.client = self.chan.join('client')
        self.server = None

    def run(self):
        self.chan.bind(self.client)
        self.server = self.chan.subgroup('server')

    def stop(self):
        self.chan.leave('client')




    def append(self, data, db_list, callback):
        assert isinstance(db_list, DBList)
        msglst = (constRPC.APPEND, data, db_list)  # message payload
        self.chan.send_to(self.server, msglst)  # send msg to server

        # thread 
        response_thread =  threading.Thread(target=self._wait_for_response, args=[callback, ])
        response_thread.start()
        
        #    self.other_work()

    def _wait_for_response(self, callback):
        while True:
          msgrcv = self.chan.receive_from(self.server)
          #print(msgrcv)
          if msgrcv:
            if msgrcv[1]=="ACK":
                print("Client received acknoledgement from server.")
            else:
                callback(msgrcv[1])
                break
          else:
            print("Client is active, waiting for server acknoledgement...")
            time.sleep(1)

       # msgrcv = self.chan.receive_from(self.server)  # wait for response
       # return msgrcv[1]  # pass it to caller


class Server:
    def __init__(self):
        self.chan = lab_channel.Channel()
        self.server = self.chan.join('server')
        self.timeout = 3

    @staticmethod
    def append(data, db_list):
        assert isinstance(db_list, DBList)  # - Make sure we have a list
        return db_list.append(data)

    def run(self):
        self.chan.bind(self.server)
        while True:
            msgreq = self.chan.receive_from_any(self.timeout)  # wait for any request
            if msgreq is not None:
                client = msgreq[0]  # see who is the caller
                msgrpc = msgreq[1]  # fetch call & parameters
                self.chan.send_to({client}, "ACK")  # Bestätige Empfang
                time.sleep(5)
                if constRPC.APPEND == msgrpc[0]:  # check what is being requested
                    result = self.append(msgrpc[1], msgrpc[2])  # do local call
                    self.chan.send_to({client}, result)  # return response
                else:
                    pass  # unsupported request, simply ignore
