# Bluetooth Server Tester
Copyright © 2023 Min Kabar Kyaw

Creates a bluetooth server on the host machine for testing connections.

## Introduction

This program opens a bluetooth socket and acts as a test program to check if information has been sent via bluetooth correctly. Sent and received messages are logged on the console.

## Requirements

The host machine requires the following installed:

-   Python 3
-   pybluez

## Features

- **Multi-threading:** Three threads are used for receiving messages, sending messages, and polling the device (similar to send) to check the connection status.
- **Reconnection:** When the polling thread fails to write via the socket, the socket is closed and reopened while creating new threads for receive/send operations
