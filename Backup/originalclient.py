import socket

ClientSocket = socket.socket()
host = '192.168.56.105'
port = 8888

print('Waiting for connection')
try:
        ClientSocket.connect((host,port))
except socket.error as e:
        print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
        Input=input('\n Press 1 to Play  Press 0 to Quit: ')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        if Input =='1':
                player=input('\n1 Player [Press 1]  2 Player [Press 2]: ')
                ClientSocket.send(str.encode(player))
                num = ClientSocket.recv(1024)
                print(num.decode('utf-8'))
                choose=input('\n[1 for Rock] [ 2 for Paper] [3 for Scissors]: ')
                ClientSocket.send(str.encode(choose))
                result = ClientSocket.recv(1024)
                print(result.decode('utf-8'))
        elif Input =='0':
                close = ClientSocket.recv(1024)
                print(close.decode('utf-8'))
                break
        else:
                break



ClientSocket.close(
