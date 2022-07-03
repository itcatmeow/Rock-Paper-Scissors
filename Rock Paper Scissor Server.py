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
