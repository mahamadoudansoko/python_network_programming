from socket import *

#The server information
serverName = '127.0.0.1'
serverPort = 12000
#We define the typee of IP (IPv4) and the data type for the TCP Protocol
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Taking the string from the user
sentence = input("Input lowercase sentence:")

#Conver the data into bytes before sending them to the server
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

#We decode the message after receiving it fro the server 
print (f"From Server: + {modifiedSentence.decode()}")

#For safety, always close the socket
clientSocket.close()