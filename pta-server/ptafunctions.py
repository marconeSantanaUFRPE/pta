from socket import *
import os
def cump(num,commandArg,connectionSocket):
    command, arg = commandArg.split()
    usersPath = (os.path.join( os.path.dirname ( __file__), "users.txt"))
    users = open(usersPath, "r")
    returnString = "NOK"
    returnMessage = str(num) + " " + returnString
    notUserInList = True
    for x in (users.readlines()):
        user = (x.replace("\n", ""))
        if user == arg:
            returnString = "OK"
            returnMessage = str(num) + " " + returnString
            connectionSocket.send(returnMessage.encode('ascii'))
            notUserInList = False
            

    if(notUserInList):
        connectionSocket.send(returnMessage.encode('ascii'))
        connectionSocket.close()
        return False
    return True
  

def pega(num,commandArg,connectionSocket):
    command, arg = commandArg.split()
    filesPath = (os.path.join( os.path.dirname ( __file__), "files"))
    returnString = str(num) + " " + "NOK"
    bytesFile = 0
    notInList = True
    for root, dirs, files in os.walk(filesPath):
        for filename in files:
            if(filename == arg):
                size = os.path.getsize(os.path.join( os.path.dirname ( __file__), "files", filename))
                filetest = os.path.join( os.path.dirname ( __file__), "files", filename)
                bytesFile = open( filetest,"rb").read()
                returnString = str(num) + " ARQ "  + str(size)
                teste = bytesFile.decode('utf-8')
                filesReturn = returnString + " " + teste
                notInList = False
                connectionSocket.send(filesReturn.encode('ascii'))
    if(notInList):
        connectionSocket.send(returnString.encode('ascii'))
        return True
    return True
    


def listFiles(num,commandArg,connectionSocket):

    filesPath = (os.path.join( os.path.dirname ( __file__), "files"))
    allfiles = ""
    cont = 0
    for root, dirs, files in os.walk(filesPath):
        for filename in files:
            allfiles += filename + ","
            cont +=1
    
    
    stringReturn = str(num) + " ARQS "  + str(cont) + " "+ allfiles[:-1]
    connectionSocket.send(stringReturn.encode('ascii'))
    return True

def term(num,commandArg,connectionSocket):
    returnMessage = str(num) + " " + "OK"
    connectionSocket.send(returnMessage.encode('ascii'))
    connectionSocket.close()
    return False