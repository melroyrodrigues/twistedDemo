from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
        
    def connectionMade(self):
        print "Server: Connection Made"

    def connectionLost(self, reason):
        print "Server: Connection Lost"


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()
    

s = ''
s.lower()
s.upper()


reactor.listenTCP(8001, EchoFactory())
reactor.run()