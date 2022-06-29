import socket
import sys
import time
import errno
import math
from multiprocessing import Process
import random


result3 = 'Win'
close = 'You Quit'
startmsg = 'Lets Play'
msg1 = '1 Player chosen'
rps = ["Rock", "Paper", "Scissors"]

def process_start(s_sock):
        plyr_score=0
        com_score=0
        s_sock.send(str.encode('Rock Paper Scissors Online Game'))
        while True:
                data = s_sock.recv(2048).decode()
                if data == '1':
                        s_sock.sendall(str.encode(startmsg))
                        player = s_sock.recv(2048).decode()
                        if player == '1':
                                s_sock.sendall(str.encode(msg1))
                                while plyr_score <3 and com_score <3:
                                    choose = s_sock.recv(2048).decode()
                                    com = random.choice(rps)#random for computer to pick option
                                    if (choose == '1' and com =='Rock') or (choose == '2' and com =='Paper') or (choose == '3' and com =='Scissors'):
                                            result = 'Draw'
                                    elif (choose == '1' and com =='Paper') or (choose == '2' and com =='Scissors') or (choose == '3' and com =='Rock'):
                                            result = 'Lose'
                                            com_score=com_score+1
                                    elif (choose == '1' and com =='Scissors') or (choose == '2' and com =='Rock') or (choose == '3' and com =='Paper'):
                                            result = 'Win'
                                            plyr_score=plyr_score+1
                                    if plyr_score <3 and com_score <3:
                                            total='ongoing..'
                                    elif com_score ==3:
                                            total='You lose the match'
                                    elif plyr_score ==3:
                                            total='You win the match'
                                    s_sock.sendall(str.encode(result))
                                    s_sock.sendall(str.encode(total))
                                    
                elif data == '0':
                        s_sock.sendall(str.encode(close))
                else:
                        break

        s_sock.close()

if __name__=='__main__':
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(("",8888))
        print("listening...")
        s.listen(3)
        try:
                while True:
                        try:
                                s_sock,s_addr = s.accept()
                                print('Connected to: ' + s_addr[0] + ':' + str(s_addr[1]))
                                p = Process(target=process_start, args=(s_sock,))
                                p.start()
                        except socket.error:
                                print('got a socket error')

        except Exception as e:
                print('an exception occured!')
                print(e)
                sys.exit(1)
        finally:
                s.close()
