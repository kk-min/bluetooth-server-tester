# Bluetooth Server Tester

Creates a bluetooth server on the host machine for testing connections.

# Introduction

This program opens a bluetooth socket and acts as a test program to check if information has been sent via bluetooth correctly. Sent and received messages are logged on the console.

Sending and receiving messages are done via separate threads in order not to interfere with each other. The send thread polls for messages from the client every two seconds.

# Requirements

Host machine requires the following installed:

-   Python 3
-   pybluez
