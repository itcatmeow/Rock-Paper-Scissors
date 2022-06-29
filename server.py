import socket
import sys
import time
import errno
import math
from multiprocessing import Process
import random

result1 = 'Draw'
result2 = 'Lose'
result3 = 'Win'
result4 = 'Win'
result5 = 'Draw'
result6 = 'Lose'
result7 = 'Lose'
result8 = 'Win'
result9 = 'Draw'
close = 'You Quit'
startmsg = 'Lets Play'
msg1 = '1 Player chosen'
rps = ["Rock", "Paper", "Scissors"]

def process_start(s_sock):
        s_sock.send(str.encode('Rock Paper Scissors Online Game'))
        while True:
                data = s_sock.recv(2048).decode()
                if data == '1':
                        s_sock.sendall(str.encode(startmsg))
                        player = s_sock.recv(2048).decode()
                        if player == '1':
                                s_sock.sendall(str.encode(msg1))
                                choose = s_sock.recv(2048).decode()
                                com = random.choice(rps)
                                if choose == '1' and com =='Rock':
                                        s_sock.sendall(str.encode(result1))
                                elif choose == '1' and com =='Paper':
                                        s_sock.sendall(str.encode(result2))
                                elif choose == '1' and com =='Scissors':
                                        s_sock.sendall(str.encode(result3))
                                elif choose == '2' and com =='Rock':
                                        s_sock.sendall(str.encode(result4))
                                elif choose == '2' and com =='Paper':
                                        s_sock.sendall(str.encode(result5))
                                elif choose == '2' and com =='Scissors':
                                        s_sock.sendall(str.encode(result6))
                                elif choose == '3' and com =='Rock':
                                        s_sock.sendall(str.encode(result7))
                                elif choose == '3' and com =='Paper':
                                        s_sock.sendall(str.encode(result8))
                                elif choose == '3' and com =='Scissors':
                                        s_sock.sendall(str.encode(result9))
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
