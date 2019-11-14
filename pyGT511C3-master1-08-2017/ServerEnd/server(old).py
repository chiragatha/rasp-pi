import socket
from array import array
from datetime import date
import datetime
import sys  

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
port = 1234
address=(ip,port)
server.bind(address)
server.listen(5)


def image(self):
    file1 = open("torecv.png","wb")
    while True:
        client,addr=server.accept()
#        info = client.recv(1024)
        while(l):
            file1.write(info)
            print('Receiving...')
            info=client.recv(1024).decode()
        file1.close()
        print("Image Received")
while True:
    print("started listening" ,ip,":",port)
    client,addr=server.accept()
    print("Got connection from" ,addr[0],":",addr[1])
    while True:
        file=open('Info_received.txt','w')
        client,addr=server.accept()
        info=client.recv(1024).decode()
        
        if (len(info)==12) :
            print("proccessing data")
            client.send("Data received".encode())
            print ("Data send")
            file.write("Aadhaar Number : %s" %(info))
            file.close()
            break
            
        elif (len(info)==31) :
            print("Credit card info:%s" %(info))
            print("proccessing data")
            client.send("Data received".encode())
            print ("Data send")
            info=info.replace(' ' ,' ' )
            if (int(info[0]) == 4):
                print("\nIt is a VISA card")
                client.send("\nIt is a Visa Card")
            elif(int(info[0]) == 5):
                print("It is a MASTER card")
            elif(int(info[1]) == 6):
                print("It is a Discover card")
                
            year=int("20"+info[17]+info[18])
            month=int(info[19]+info[20])
            print("year is %s and month is %s" %(year,month))   
            now = datetime.datetime.now()
            current_year = now.year
            current_month = now.month
            print (current_year)
            if (year == current_year and month <= current_month):
                print("card is valid")
                file.write("Card Info: %s, Validity year:  %s, Validity month:  %s "%(info,year,month))
                file.close()
            elif (year > current_year):
                print("Card is valid")
                file.write("Card Info: %s, Validity year:  %s, Validity month:  %s "%(info,year,month))
                file.close()
            else:
                print("Card Invalid")

            break
    
        else:
            pass
