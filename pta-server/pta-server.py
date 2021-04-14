from socket import *
import os
from ptafunctions import cump, listFiles, pega, term

task = {

'CUMP': lambda num,arg,socket: cump(num,arg, socket),
'LIST': lambda num,arg,socket : listFiles(num, arg,socket),
'PEGA': lambda num,arg,socket: pega(num,arg,socket),
'TERM': lambda num,arg,socket : term(num,arg,socket),
}


serverPort = 11550
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Servidor refatorado Online !")
isConnection = False
while True:
    try:
        if(isConnection == False):
            connectionSocket, addr = serverSocket.accept()
        
        sentence = connectionSocket.recv(1024).decode()
        num, command = sentence.split(' ', 1)
        print(command)
        try:
            if(isConnection == False and "CUMP" not in command):
                returnMessage = (num + " " + "NOK")
                connectionSocket.send(returnMessage.encode('ascii'))
                isConnection = False
            elif(isConnection or "CUMP" in command):
                retorno = task[command.split()[0]](num, command, connectionSocket)
                isConnection = retorno
                print(isConnection)
                
        except:
            returnMessage = (num + " " + "NOK")
            connectionSocket.send(returnMessage.encode('ascii'))
            isConnection = False
              
    except (KeyboardInterrupt, SystemExit):
        break