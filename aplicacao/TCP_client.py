from socket import *

serverName = "localhost"
serverPort = 12007

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = input('Input lowercase sentence:')

clientSocket.send(sentence.encode('utf-8'))

modifiedSentence = clientSocket.recv(1024).decode('utf-8')

print("From Server:", modifiedSentence)

clientSocket.close()