import socket
from array import array
from datetime import date
import datetime
import sys
import os

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
port = 1234
address=(ip,port)
server.bind(address)
server.listen(5)

while True:
    print("started listening" ,ip,":",port)
    conn,addr=server.accept()
    print("Got connection from" ,addr[0],":",addr[1])
    info =conn.recv(1024)
    if(info == '1'):
        print("Credit card data will be received ")
        file1=open('torecv.txt', 'wb')
        while True:
            data = conn.recv(1024)
            print data
            if not data:
                break
            else:
                file1.write(data)
            file1.close()
            card = open('torecv.txt').read()
            card=card.replace(' ' ,' ' )
            year=int("20"+card[17]+card[18])
            month=int(card[19]+card[20])
            print(year)
            print(month)
            print(card)
            break
    elif( info == '2'):
        print("aadhar data will be received")
        file1=open('torecv.txt', 'wb')
        while True:
            conn,addr=server.accept()
            data = conn.recv(1024)
            print data
            file1.write(data)      
            file2 = open('Imgrecv.png','wb')
            while True:
                conn, addr = server.accept()   
                print("Got connection from" ,addr[0],":",addr[1])                
                l = conn.recv(1024)
                if l:
                    while(l):
                        file2.write(l)
                        l=conn.recv(1024)
                        print("Receiving...")
                    file2.close()
                    print("Data Received")
                    break
            
                else:
                    break
            file1.close()
            aadhar = int(open('torecv.txt').read())
                        
            break
