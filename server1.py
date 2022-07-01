import socket
import sys
import time
import errno
import math
from multiprocessing import Process
import random
import threading
import random

result=''
close = 'You Quit'
startmsg = 'Lets Play'
msg1 = '1 Player chosen'
rps = ["Rock", "Paper", "Scissors"]
player_list = []
listen_list = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",8888))
print("listening...")
def accept():
    while True:
        s.listen()
        s_sock,s_addr = s.accept()
        numplayer = s_sock.recv(1024).decode()

        if numplayer == '1' :
           print("One player mode")
           print("Connected to :",s_addr[0])
           singleplayer_listen(s_sock)

        else:
           print("Double player mode")
           print("Connected to :",s_addr[0])
           player_list.append(s_sock)
           mula_listen(s_sock)

def mula_listen(s_sock):
        #thread objects
        client_thread = threading.Thread( target=listen_and_reply, args=(s_sock,))
        #the list of argument for the function
        client_thread.start()

def listen_and_reply(s_sock):
    while True:
        message = s_sock.recv(1024).decode()
        listen_list.append(message)
        if len(listen_list) == 2:
            playerA =listen_list[0]
            playerB =listen_list[1]
            if (playerA == '1' and playerB =='1') or (playerA == '2' and playerB =='2') or (playerA == '3' and playerB =='3'):
                result = 'Draw'
            elif(playerA == '1' and playerB =='2') or (playerA == '2' and playerB =='3') or (playerA == '3' and playerB =='1'):
                result = 'Player A lOSE, Player B WIN'
            elif (playerA == '1' and playerB =='3') or (playerA == '2' and playerB =='1') or (playerA == '3' and playerB =='2'):
                result = 'Player A WIN, Player B LOSE'
            print(result)
            toall(result)
            listen_list.clear()

def singleplayer_listen (s_sock):
        client_thread = threading.Thread( target=listen_and_reply_single, args=(s_sock,))
        #the list of argument for the function
        client_thread.start()

def listen_and_reply_single(s_sock):
    while True:
        message = s_sock.recv(1024).decode()
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
    for s_sock in player_list:
        s_sock.send(message.encode())
accept()


