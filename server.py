import socket
import sys
import time
import errno
import math
from multiprocessing import Process
import random
import threading

result1 = 'Draw'
result2 = 'Lose'
result3 = 'Win'
result=''
close = 'You Quit'
startmsg = 'Lets Play'
msg1 = '1 Player chosen'
rps = ["Rock", "Paper", "Scissors"]
player_list = []
listen_list = []
send_list = []
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",8888))
print("listening...")
def accept():
    while True:
        s.listen()
        s_sock,s_addr = s.accept()
        numplayer = s_sock.recv(1024).decode()
        print("Connected to :",s_addr[0])
        if numplayer == '1' :
           print("One player mode")
           p = Process(target=process_start, args=(s_sock,))
           p.start()

        else:
           print("Double player mode")
           mula_listen(s_sock,s_addr[0])

def mula_listen(s_sock,s_addr):
        #thread objects
        client_thread = threading.Thread( target=listen_and_reply, args=(s_sock,s_addr))
        #the list of argument for the function
        client_thread.start()

def listen_and_reply(s_sock,s_addr):
    while True:
        message = s_sock.recv(1024).decode()
        listen_list.append(message)
        player_list.append(s_addr)
        send_list.append(s_sock)
        if len(listen_list) == 2:
            playerA =listen_list[0]
            playerB =listen_list[1]
            if (playerA == '1' and playerB =='1') or (playerA == '2' and playerB =='2') or (playerA == '3' and playerB =='3'):
                result = 'Draw'
            elif(playerA == '1' and playerB =='2') or (playerA == '2' and playerB =='3') or (playerA == '3' and playerB =='1'):
                result = f'{player_list[1]}WIN, {player_list[0]} LOSE'
            elif (playerA == '1' and playerB =='3') or (playerA == '2' and playerB =='1') or (playerA == '3' and playerB =='2'):
                result = f'{player_list[0]}WIN, {player_list[1]}B LOSE'
            print(result)
            toall(result)
            listen_list.clear()

def process_start(s_sock):
    while True:
       choose = s_sock.recv(2048).decode()
       com = random.choice(rps)
       if choose == '1' and com =='Rock':
            s_sock.sendall(str.encode(result1))
       elif choose == '1' and com =='Paper':
            s_sock.sendall(str.encode(result2))
       elif choose == '1' and com =='Scissors':
            s_sock.sendall(str.encode(result3))
       elif choose == '2' and com =='Rock':
            s_sock.sendall(str.encode(result3))
       elif choose == '2' and com =='Paper':
            s_sock.sendall(str.encode(result1))
       elif choose == '2' and com =='Scissors':
            s_sock.sendall(str.encode(result2))
       elif choose == '3' and com =='Rock':
            s_sock.sendall(str.encode(result2))
       elif choose == '3' and com =='Paper':
            s_sock.sendall(str.encode(result3))
       elif choose == '3' and com =='Scissors':
            s_sock.sendall(str.encode(result1))

def listen_and_reply_single(s_sock):
    while True:
        message = s_sock.recv(1024).decode()
        if not message:
            print(f"Player has been disconnected: {s_addr[0]}")
            return
        listen_list.append(message)
        com = random.choice(rps)
        print("Com : ", com)
        if len(listen_list) == 2:
            player =listen_list[0]
            if (player == '1' and com =='Rock') or (player == '2' and com =='Paper') or (player == '3' and com =='Scissors'):
                result = 'Draw'
            elif(player == '1' and com =='Paper') or (player == '2' and com =='Scissors') or (player == '3' and com =='Rock'):
                result = 'You Lose'
            elif (player == '1' and com =='Scissors') or (player == '2' and com =='Rock') or (player == '3' and com =='Paper'):
                result = 'You Win'
            print(result)
            toall(result)
            listen_list.clear()

def toall(message):
    for s_sock in send_list:
        s_sock.send(str.encode(message))
accept()
