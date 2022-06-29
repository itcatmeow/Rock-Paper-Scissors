import socket
import threading

ClientSocket = socket.socket()
host = '192.168.56.105'
port = 8888
print('Waiting for connection')
try:
        ClientSocket.connect((host,port))
except socket.error as e:
        print(str(e))
        
def send():
    while True:
        Input = input("[1 for Rock] [ 2 for Paper] [3 for Scissors]")
        ClientSocket.send(Input.encode())
        
def recev():
    while True:
        message = ClientSocket.recv(1024).decode()
        print('Result: ' + message +'\n')
        

thread_send = threading.Thread(target=send)
thread_receive = threading.Thread(target=recev)
thread_send.start()
thread_receive.start()
