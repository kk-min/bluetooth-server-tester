from server import server

test_server = server()
server.connect()
while(True):
    incomingMessage = server.read()
    if(incomingMessage != None):
        print(incomingMessage)
