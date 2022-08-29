from server import server
import time
from threading import Thread

def receive_message(input_server):
    while(True):
        incomingMessage = input_server.read()
        if(incomingMessage != None):
            print("Message from client: "+incomingMessage);
        time.sleep(2)

def send_message(input_server, message):
    input_server.write(message)
    print("Message to client: "+message)

test_server = server()
test_server.connect()
receive_thread = Thread(target=receive_message, args=(test_server,))
send_thread = Thread(target=send_message, args=(test_server, "Hello from Server!"))
receive_thread.start()
send_thread.start()