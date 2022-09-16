from server import server
import time
from threading import Thread

def receive_message(input_server):
    while(True):
        try:
            incomingMessage = input_server.read()
        except:
            return
        if(incomingMessage != None):
            print("Message from client: "+incomingMessage);
        time.sleep(2)

def get_input(input_server):
    while(True):
        message=input("Enter message to send: ")
        send_thread = Thread(target=send_message, args=(input_server, message))
        send_thread.start()
        time.sleep(1)

def send_message(input_server, message):
    input_server.write(message)
    print("Message to client: "+message+"\n")

def poll(input_server):
    while True:
        try:
            input_server.write("polling")
        except:
            input_server.disconnect()
            print("Disconnected. Attempting reconnection...")
            input_server.connect()
            receive_thread = Thread(target=receive_message, args=(test_server,))
            send_thread = Thread(target=send_message, args=(test_server, "Hello from reconnected Server!"))
            receive_thread.start()
            send_thread.start()
            time.sleep(2)
            continue

        time.sleep(2)

test_server = server()
test_server.connect()
receive_thread = Thread(target=receive_message, args=(test_server,))
input_thread = Thread(target=get_input, args=(test_server,))
poll_thread = Thread(target=poll, args=(test_server,))
receive_thread.start()
input_thread.start()
time.sleep(2)
poll_thread.start()