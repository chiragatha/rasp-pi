import socket
import os
import sys  

name=socket.gethostname()
print(name)
ip=socket.gethostbyname(name)
client = socket.socket()
client.connect((str(ip),1234))

def communicate(data):
    client.send(data.encode())
    print (client.recv(1024).decode())
    return
    os.system('python client.py')
'''  
def image(self):
   f = open('img_temp.png','rb')
   print 'Sending...'
   l = f.read(1024)
   while(l):
       print 'Sending...'
       client.send(l)
       l = f.read(1024)
   f.close()
   print "Done Sending"
   print client.recv(1024)
   os.system('python client.py')
'''
