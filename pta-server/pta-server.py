from socket import *
import os
def cump(num,arg):
    usersPath = (os.path.join( os.path.dirname ( __file__), "users.txt"))
    users = open(usersPath, "r")
    returnString = "NOK"
    for x in (users.readlines()):
        user = (x.replace("\n", ""))
        if user == arg:
            returnString = "OK"
    return str(num) + " " + returnString

def pega(num,arg):
    filesPath = (os.path.join( os.path.dirname ( __file__), "files"))
    returnString = str(num) + " " + "NOK"
    bytesFile = 0
    print("PO")
    for root, dirs, files in os.walk(filesPath):
        for filename in files:
            if(filename == arg):
                (filename)
                size = os.path.getsize(os.path.join( os.path.dirname ( __file__), "files", filename))
                filetest = os.path.join( os.path.dirname ( __file__), "files", filename)
                bytesFile = open( filetest,"rb").read()
                returnString = str(num) + " ARQ "  + str(size)
                print(type(bytesFile))
                return(returnString, bytesFile)
    return(returnString, bytesFile)


def listFiles(num):

    filesPath = (os.path.join( os.path.dirname ( __file__), "files"))
    allfiles = ""
    cont = 0
    for root, dirs, files in os.walk(filesPath):
        for filename in files:
            allfiles += filename + ","
            cont +=1
    stringReturn = str(num) + " ARQS "  + str(cont) + " "+ allfiles[:-1]
    return(stringReturn)

def term(num):
    return(str(num) + " OK")

task = {

'CUMP': lambda num,arg: cump(num,arg),
'LIST': lambda num : listFiles(num),
'PEGA': lambda num,arg: pega(num,arg),
'TERM': lambda num : term(num),
}

serverPort = 11550
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Servidor Online !")
connectionAprove = False
while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        print("connected by ", addr)
        sentence = connectionSocket.recv(1024).decode()
        num, command = sentence.split(' ', 1)
        print(num, command)
        returnMessage = num + " " + "NOK"
        try:
            if(connectionAprove == False and "CUMP" not in command):
                retorno = num + " " + "NOK"
                returnMessage = (retorno)
                connectionSocket.send(returnMessage.encode('ascii'))
                connectionSocket.close()
                connectionAprove = False
            elif("CUMP" in command):         
                command, arg = command.split(" ")
                retorno = task[command](num,arg)
                if(retorno.split(" ")[1] == "OK"):
                    connectionAprove = True
                    returnMessage = (retorno)
                    connectionSocket.send(returnMessage.encode('ascii'))                  
                    print(sentence)            
                else:
                    returnMessage = (retorno)
                    connectionSocket.send(returnMessage.encode('ascii'))
                    connectionSocket.close()
                    connectionAprove = False
            if(connectionAprove == True):
                if(command == "LIST"):
                    print("OPI")
                    retorno = task[command] (num)
                    returnMessage = (retorno)
                    connectionSocket.send(returnMessage.encode('ascii'))
                if("PEGA" in command):
                    command, arg = command.split(" ")
                    print("PEGA")
                    retorno = task[command] (num, arg)
                    returnMessage = (retorno)[0]
                    bytesFile = (retorno)[1]
                    if(bytesFile==0):
                        connectionSocket.send(returnMessage.encode('ascii'))
                    else:
                        teste = bytesFile.decode('utf-8')
                        filesReturn = returnMessage + " " + teste
                        connectionSocket.send(filesReturn.encode('ascii'))
                if(command == "TERM"):
                    returnMessage = task[command](num)
                    connectionSocket.send(returnMessage.encode('ascii'))
                    connectionSocket.close()
                    connectionAprove = False
        except (InterruptedError): 
            returnMessage = (num + " " + "NOK")
            connectionSocket.send(returnMessage.encode('ascii'))
            connectionSocket.close()   
    except (KeyboardInterrupt, SystemExit):
        break


# NUM Command arg

# request = input()

# num, command = request.split(' ', 1)

# print(num)
# print(command)

# if "CUMP" in command or "PEGA" in command:
#     command, arg = command.split(" ", 1)
#     print(task[command](num,arg))
# if "LIST" in command:

#     print(listFiles(num))



