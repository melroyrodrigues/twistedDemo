from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello, world!")

    def dataReceived(self, data):
        print "Server said:", data
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print "EchoClient: Connection lost to server"


class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed."
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "EchoFactory: Connection lost."
        reactor.stop()


reactor.connectTCP("localhost", 8001, EchoFactory())
reactor.run()
