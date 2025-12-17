#TCPServer.PythonFinalizationError
from socket import *
#Define the server port 
serverPort = 12000

#Define the IPv4 version and the data type for the TCP Protocol
serverSocket = socket(AF_INET,SOCK_STREAM)

#We associate the port number with the server's Socket whch is  our welcoming socket
serverSocket.bind(('' ,serverPort))

#We wait for a client to knock to the door (the socket) specifying the max of queued connections (one (1)) in our case
serverSocket.listen(1)

#Let know that the server is ready to listen
print(f"The server is ready to receive")


#Always do the following tasks
while 1:

    #Create the connection socket for the cleint to communicate with the server (this is unique to TCP and ensures communication reliability)
    #This is the handshaking phasing between the client and the server.
    connectionSocket, addr = serverSocket.accept()

    #We create "sentence" variable that store the byte data from the connection socket guaranteed and in order
    sentence = connectionSocket.recv(1024)

    #Capitalize the string we receive
    capitalizedSentence = sentence.upper()

    #Send the capitilized string to the client
    connectionSocket.send(capitalizedSentence)

    #Close for safety
    connectionSocket.close()