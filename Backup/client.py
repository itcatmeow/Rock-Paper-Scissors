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
        
def send_recv():
    while True:
        Input = input("[1 for Rock] [ 2 for Paper] [3 for Scissors]")
        ClientSocket.send(Input.encode())
        print("Wait for opponent")
        message = ClientSocket.recv(1024).decode()
        print('Result: ' + message +'\n')
thread_send_recv = threading.Thread(target=send_recv)
thread_send_recv.start()
