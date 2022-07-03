import socket
import threading
import time

def send_recv():
    while True:
        Input = input("[1 for Rock] [ 2 for Paper] [3 for Scissors]")
        ClientSocket.send(Input.encode())
        print("Wait for opponent")
        message = ClientSocket.recv(1024).decode()
        print('Result: ' + message +'\n')
