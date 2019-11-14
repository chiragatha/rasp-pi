import socket
import os
name=socket.gethostname()
print(name)
ip=socket.gethostbyname(name)
client = socket.socket()
client.connect((str(ip),1234))

command = raw_input("Please enter the command: ")
def communicate(data):
    client.send(data.encode())
    print (client.recv(1024).decode())
    return
communicate(command)
os.system('python clientdemo.py')
