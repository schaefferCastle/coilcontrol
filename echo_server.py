import socket
import threading
from PyQt5.QtCore import pyqtSignal
from queue import Queue


class MsgHandler:

    def __init__(self, *args, **kwargs):
        super(MsgHandler, self).__init__()
        self.msg = None
        self.killme = False

    def catchmsg(self, in_q, out_q):
        while True:
            self.msg = in_q.get()
            print(self.msg)
            out_q.put(self.msg)
            in_q.task_done()


class Server:

    def __init__(self, *args, **kwargs):
        super(Server, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.args = args
        self.kwargs = kwargs
        self.killme = False

        self.msg = None
        self.signal = pyqtSignal()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = '127.0.0.1'
        self.port = 65432

        print('Starting up a server!')
        try:
            self.sock.bind((self.address, self.port))
        except:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.bind((self.address, self.port))
        self.sock.listen(1)

    def thread_server_worker(self, out_q, in_q):
        while not self.killme:
            connection, client_address = self.sock.accept()
            with connection:
                try:
                    value_1 = []
                    value_2 = []
                    datain = connection.recv(512)
                    data = datain.decode('utf-8')
                    if data.find(':') != -1:
                        data, value_1 = data.split(':')
                        if value_1.find(',') != -1:
                            value_1, value_2 = value_1.split(',')
                            print(value_1, value_2)
                    if data:
                        out_q.put(data)
                    else:
                        break
                finally:
                    self.msg = in_q.get()
                    sendstring = self.msg + '\n'
                    connection.sendall(bytes(sendstring, 'utf-8'))
                    in_q.task_done()
                    out_q.join()
                    print('Closing Connection!')
                    connection.close()
        connection.close()
        self.sock.close()

def main():
    q1 = Queue()
    q2 = Queue()
    serv = Server()
    rcv = MsgHandler()

    t1 = threading.Thread(target=rcv.catchmsg, args=(q1, q2,))
    t2 = threading.Thread(target=serv.thread_server_worker, args=(q1, q2,))

    t1.start()
    t2.start()

    # in_q = q.get()
    # print(in_q)
    # q.join()


if __name__ == '__main__':
    main()
