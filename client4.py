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

ClientSocket = socket.socket()
host = '192.168.56.105'
port = 8888
print('Waiting for connection')
try:
        ClientSocket.connect((host,port))
        print (" Welcome to Rock - Paper - Scissor game ")
        numplayer = input("Choose number of players. Single (1) or Double (2) players. \n En>
        ClientSocket.send(numplayer.encode())
        if numplayer =='1':
                while True:
                    choose=input('\n[1 for Rock] [ 2 for Paper] [3 for Scissors]: ')
                    ClientSocket.send(str.encode(choose))
                    result = ClientSocket.recv(1024)
                    print(result.decode('utf-8'))
        elif numplayer =='2':
                thread_send_recv = threading.Thread(target=send_recv)
                thread_send_recv.start()

except socket.error as e:
        print(str(e))


