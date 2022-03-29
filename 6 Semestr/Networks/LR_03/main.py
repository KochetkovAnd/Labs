from http import client
from pickle import TRUE
from re import T
import socket
from tabnanny import check

HOST = "91.222.128.11"
PORT = 21
LOGIN = "testftp_guest"
PASSWORD = "12345"
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connection():
    s.connect((HOST, PORT))
    s.recv(4096)
    user = "USER " + LOGIN +"\r\n"
    pwd = "PASS " + PASSWORD + "\r\n"
    s.sendall(user.encode())
    s.recv(4096)    
    s.sendall(pwd.encode())
    s.recv(4096) 

def list_files(directory):    
    portCommand = "PORT 192,168,33,35,4,150\r\n"
    listCommand = "LIST " + directory + "\r\n"
    s.sendall(portCommand.encode())
    s.recv(BUFFER_SIZE)  
    s.sendall(listCommand.encode())

def changeDirectory(directory):
    command = 'CWD ' + directory + "\r\n"
    s.sendall(command.encode())
    data = str(s.recv(4096))
    return "250 Directory successfully changed." in data

def removeEmpty(list):
    newlist = []
    for l in list:
        if l != '':
            newlist.append(l)
    return newlist

def parsePage(page):
    weight = 0
    directories = []
    lines = removeEmpty(page.split('\\r\\n'))
    for line in lines:
        words = removeEmpty(line.split(" "))
        weight += int(words[4])
        filename = words[8]
        directories.append(filename)

    return directories, weight

'''def start():
    sum = 0 
    s2.bind(("192.168.33.35" , 1174))
    s2.listen() 
    connection()
    list_files("")

    clientSocket, clientAdress = s2.accept()
    data = str(clientSocket.recv(BUFFER_SIZE))
    directories, weight = parsePage(data[2:-1])
    sum += weight
    for directory in directories:
        sum += recursion(directory, clientSocket)
        
    
def recursion(directory,clientSocket):
    sum = 0
    if changeDirectory(directory):
        list_files(directory)
        data = str(clientSocket.recv(BUFFER_SIZE))
        directories, weight = parsePage(data[2:-1]) 
        sum += weight

        for dir in directories:
            sum += recursion(dir, clientSocket)

    return sum'''

def start():
    connection()
    s2.bind(("192.168.33.35" , 1174))
    sum = recursion("..")

    
    
        
    
def recursion(directory): 
    s2.listen()
    sum = 0
    if changeDirectory(directory):
        list_files(directory)
        clientSocket, clientAdress = s2.accept()
        data = str(clientSocket.recv(BUFFER_SIZE))
        directories, weight = parsePage(data[2:-1]) 
        sum += weight

        for dir in directories:
            sum += recursion(".log")

    return sum

    
start()   
    


s.close()

    


