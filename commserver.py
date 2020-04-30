import sys
# from PyQt5.QtCore import QByteArray, QDataStream, QIODevice
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtNetwork import QHostAddress, QTcpServer
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject


class Server(QDialog):
    def __init__(self):
        super().__init__()
        self.tcpServer = None
        self.signals = ServerSignals()
        self.clientConnection = None

    def sessionOpened(self):
        self.tcpServer = QTcpServer(self)
        PORT = 65432
        address = QHostAddress('127.0.0.1')
        if not self.tcpServer.listen(address, PORT):
            print("cant listen!")
            self.close()
            return
        self.tcpServer.newConnection.connect(self.dealCommunication)

    @pyqtSlot()
    def dealCommunication(self):
        # Get a QTcpSocket from the QTcpServer
        self.clientConnection = self.tcpServer.nextPendingConnection()

        # wait until the connection is ready to read
        self.clientConnection.waitForReadyRead()
        # read incomming data
        instr = self.clientConnection.readAll()

        # rais signal with message
        tomaingui = str(instr, encoding='utf-8')
        self.signals.msg.emit(tomaingui)

    # def sendtoclient(self, msg):
    #     # OLD Might be deleted in next version
    #
    #     # instantiate a QByteArray
    #     block = QByteArray()
    #     out = QDataStream(block, QIODevice.ReadWrite)
    #     out.setVersion(QDataStream.Qt_5_0)
    #
    #     # this is the message we will send it could come from a widget.
    #     message = msg + '\n'
    #     # message = msg
    #     message = bytes(message, encoding='utf-8')
    #     # now use the QDataStream and write the byte array to it.
    #     out.writeString(message)
    #     out.device().seek(0)
    #     out.writeUInt16(block.size() - 2)
    #
    #     # get the connection ready for clean up
    #     self.clientConnection.disconnected.connect(self.clientConnection.deleteLater)
    #     # now send the QByteArray.
    #     self.clientConnection.write(block)
    #     # now disconnect connection.
    #     self.clientConnection.disconnectFromHost()

    def sendeasy(self, msg):
        message = msg + '\n'
        out = bytes(message, 'utf-8')
        self.clientConnection.write(out)
        self.clientConnection.disconnectFromHost()


class ServerSignals(QObject):
    msg = pyqtSignal(str)
    response = pyqtSignal(str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    server = Server()
    server.sessionOpened()
    sys.exit(server.exec_())
