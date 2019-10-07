from socket import *

serverName = "localhost"
serverPort = 12007

clientSocket = socket(AF_INET, SOCK_DGRAM)
dest = (serverName,serverPort)

sentence = input('Input lowercase sentence:')

clientSocket.sendto(sentence.encode('utf-8'), dest)

modifiedSentence = clientSocket.recvfrom(1024)[0].decode('utf-8')

print("From Server:", modifiedSentence)

clientSocket.close()