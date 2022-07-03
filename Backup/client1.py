import socket
import threading
import time

ClientSocket = socket.socket()
host = '192.168.56.108'
port = 8888
print('Waiting for connection')
try:
        ClientSocket.connect((host,port))
        print (" Welcome to Rock - Paper - Scissor game ")
        numplayer = input("Choose number of players. Single (1) or Double (2) players. \n Enter 1 or 2 : ")
        ClientSocket.send(numplayer.encode())

except socket.error as e:
        print(str(e))

def send():
    while True:
        Input = input("[1 for Rock] [ 2 for Paper] [3 for Scissors]\n Player 1 : ")
        ClientSocket.send(Input.encode())
        time.sleep(0.5)
def recev():
    while True:
        message = ClientSocket.recv(1024).decode()
        print('Result: ' + message +'\n')


thread_send = threading.Thread(target=send)
thread_receive = threading.Thread(target=recev)
thread_send.start()
thread_receive.start()
