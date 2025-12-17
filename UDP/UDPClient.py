from socket import *

serverName = '127.0.0.1' # or 'hostname' (localhost) if testing on same machine
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

# Python 3 uses input(), not raw_input()
message = input('Input lowercase sentence: ')

# In Python 3, strings must be encoded to bytes before sending
clientSocket.sendto(message.encode(), (serverName, serverPort))

# buffer size 2048 is fine
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Decode bytes back to string to print nicely
print(modifiedMessage.decode())

clientSocket.close()