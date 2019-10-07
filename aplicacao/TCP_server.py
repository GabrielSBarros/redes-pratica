from socket import *

serverPort = 12007
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print ("The server is ready to receive")

try:
    while 1:
        connectionSocket, addr = serverSocket.accept()

        sentence = connectionSocket.recv(1024).decode('utf-8')

        capitalizedSentence = sentence.upper()
        sentenceParts = sentence.split()
        print(sentenceParts)
        op = sentenceParts[0]
        returning = "ERROR"
        if(op == "CONCATENAR"):
            returning = sentenceParts[1] + sentenceParts[2]
        elif(op == "COMPARAR"):
            returning = "igual" if (sentenceParts[1] == sentenceParts[2]) else "diferente"
        elif(op == "SUBSTRING"):
            returning = sentenceParts[1][int(sentenceParts[2]):int(sentenceParts[3])]
        elif(op == "CONTEM"):
            returning = "sim" if(sentenceParts[2] in sentenceParts[1]) else "nao"
        elif(op == "SUBSTITUIR"):
            returning = sentenceParts[1].replace(sentenceParts[2], sentenceParts[3])
        
        connectionSocket.send(returning.encode('utf-8'))
        connectionSocket.close()
except:
    serverSocket.close()