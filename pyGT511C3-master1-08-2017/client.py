import socket
import os
import sys
import time
from time import sleep

name=socket.gethostname()
print(name)
ip=socket.gethostbyname(name)
client = socket.socket()
client.connect((str(ip),1234))
def decision(value):
    client.send(value)

def txtfile(value):
    print("Info is: %s"%(value))
    with open('tosend.txt', 'rb') as file_to_send:
        for data in file_to_send:
            client.sendall(data)
            
    print 'end'
    sleep(1)

def image(value):
    print (value)
    f = open('img_temp.png','rb')
    print 'Sending...'
    l = f.read(1024)
    while(l):
        print 'Sending...'
        client.send(l)
        l = f.read(1024)
    f.close()
    print "Done Sending"
    client.close()
    os.system('python client.py')
    
