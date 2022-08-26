from server import server
import time

test_server = server()
test_server.connect()
test_server.write("Hello from Server!".encode()) # Send a test message to client
while(True):
    incomingMessage = test_server.read()
    if(incomingMessage != None):
        print(incomingMessage)
    time.sleep(2000)
