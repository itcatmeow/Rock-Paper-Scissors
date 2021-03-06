import socket
import threading
import time

def send_recv():
    while True:
        Input = input("[1 for Rock] [ 2 for Paper] [3 for Scissors][4 to Quit game]")
        if Input == '4':
            quit()
        elif Input:
            ClientSocket.send(Input.encode())
            print("\n Wait for opponent...")
            message = ClientSocket.recv(1024).decode()
            print(message+'\n')

ClientSocket = socket.socket()
host = '192.168.56.105'
port = 8888
print('Waiting for connection')
try:
        ClientSocket.connect((host,port))
        print (" Welcome to Rock - Paper - Scissor game ")
        numplayer = input("Choose number of players. Single (1) or Double (2) players. \n Enter 1 or 2 : ")
        ClientSocket.send(numplayer.encode())
        if numplayer =='3':
            result = ClientSocket.recv(1024)
            quit()
        elif numplayer =='1':
               while True:
                    choose=input('\n[1 for Rock] [ 2 for Paper] [3 for Scissors][4 to Quit game]: ')
                    ClientSocket.send(str.encode(choose))
                    result = ClientSocket.recv(1024)
                    print(result.decode('utf-8'))
                    if choose == '4':
                       quit()
        elif numplayer =='2':
                thread_send_recv = threading.Thread(target=send_recv)
                thread_send_recv.start()

except socket.error as e:
        print(str(e))
