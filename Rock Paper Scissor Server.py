import socket
import sys
from multiprocessing import Process
import random
import threading

result=''
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

        elif numplayer =='2':
           print("Double player mode")
           mula_listen(s_sock,s_addr[0])
            
        elif numplayer == '3':
            s_sock.sendall(str.encode("Good game, Bye!"))#message if quit

def mula_listen(s_sock,s_addr):
        #thread objects
        client_thread = threading.Thread( target=listen_and_reply, args=(s_sock,s_addr))
        #the list of argument for the function
        client_thread.start()

def listen_and_reply(s_sock,s_addr):
    while True:
        message = s_sock.recv(1024).decode()
        if message == '4':
            s_sock.sendall(str.encode("Good game, Bye!"))#message if quit
        listen_list.append(message)#list for players' hand
        player_list.append(s_addr)#list for player name
        send_list.append(s_sock)#list of client to broadcast
        print(player_list)
        if len(listen_list) == 2:
           if listen_list[0]:
                #To assign user input with the correct hand. 1 for rock...
                if listen_list[0] == '1': 
                    playerA = 'Rock'
                elif listen_list[0] == '2':
                    playerA = 'Paper'
                elif listen_list[0] == '3':
                    playerA = 'Scissors'
            if listen_list[1]:
                if listen_list[1] == '1':
                    playerB = 'Rock'
                elif listen_list[1] == '2':
                    playerB = 'Paper'
                elif listen_list[1] == '3':
                    playerB = 'Scissors'
            # ip address: hand
            print(f'{player_list[0]} : {playerA}')
            print(f'{player_list[1]} : {playerB}')
            # Ip address : Hand VS Ip address 2 : Hand2
            result= player_list[0] + ": "+ playerA + " VS " + player_list[1]+": "+playerB
            print(result)
            #Decide who wins
            if (playerA == 'Rock' and playerB =='Rock') or (playerA == 'Paper' and playerB =='Paper') or (playerA == 'Scissors' and playerB =='Scissors'):
                fin_result = f'{result} \nResult: Draw' 
                """
                Ip address : Hand VS Ip address 2 : Hand2
                Result: Draw
                """
            elif(playerA == 'Rock' and playerB =='Paper') or (playerA == 'Paper' and playerB =='Scissors') or (playerA == 'Scissors' and playerB =='Rock'):
                fin_result = f'{result} \nResult:{player_list[1]} WIN!'
            elif (playerA == 'Rock' and playerB =='Scissors') or (playerA == 'Paper' and playerB =='Rock') or (playerA == 'Scissors' and playerB =='Paper'):
                fin_result = f'{result} \nResult:{player_list[0]} WIN!'
            print(fin_result)
            toall(fin_result)
            listen_list.clear()
            player_list.clear()
            
def process_start(s_sock):
    while True:
       choose = s_sock.recv(2048).decode()
       com = random.choice(rps)# Random func to decide what computer chooses
       if choose== '1':
             hand = 'Rock'
       elif choose== '2':
             hand = 'Paper'
       elif choose== '3':
             hand = 'Scissors'
       elif choose == '4' :
            s_sock.sendall(str.encode("Good game, Bye!"))
            
        # Ip address : Hand VS Computer : Hand2    
       result= "Player: "+ hand + " VS  Computer: "+ com
       if (hand == 'Rock' and com =='Rock') or (hand == 'Paper' and com =='Paper') or (hand == 'Scissors' and com =='Scissors'):
                fin_result = f'{result} \nResult: Draw'
                 """
                Ip address : Hand VS Computer : Hand2
                Result: Draw
                """
       elif(hand == 'Rock' and com =='Paper') or (hand == 'Paper' and com =='Scissors') or (hand == 'Scissors' and com =='Rock'):
                fin_result = f'{result} \nResult: Computer WIN!'
       elif (hand == 'Rock' and com =='Scissors') or (hand == 'Paper' and com =='Rock') or (hand == 'Scissors' and com =='Paper'):
                fin_result = f'{result} \nResult:Player WIN!'


def toall(message):
    for s_sock in send_list:
        s_sock.send(str.encode(message))
        
accept()
