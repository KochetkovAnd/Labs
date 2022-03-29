import ftplib

HOST = "91.222.128.11"
LOGIN = "testftp_guest"
PASSWORD = "12345"

def removeEmpty(list):
    newlist = []
    for l in list:
        if l != '':
            newlist.append(l)
    return newlist

def parsePage(lines):
    weight = 0
    directories = []
    for line in lines:
        words = removeEmpty(line.split(" "))
        weight += int(words[4])
        filename = words[8]       
        directories.append(filename)
    return directories, weight

def start():
    ftp = ftplib.FTP(HOST)
    ftp.login(LOGIN, PASSWORD)
    return recursion(ftp, "/", "/")

def recursion(ftp, currentDirectory, lastDirectory):
    try:
        ftp.cwd(currentDirectory)
    except:
        return 0

    lines = []
    ftp.dir(lines.append)
    directories, weight = parsePage(lines)
    fullcurrentDirectory = ftp.pwd()
    for newDirectory in directories:
        weight += recursion(ftp,newDirectory, fullcurrentDirectory)
    ftp.cwd(lastDirectory) 
    return weight