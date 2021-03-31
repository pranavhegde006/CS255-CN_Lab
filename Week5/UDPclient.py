from socket import *
serverName = '10.2.20.60'
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Enter your message:	')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()
