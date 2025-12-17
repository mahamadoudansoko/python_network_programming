# UDPServer.py
from socket import *

serverPort = 12000
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to the port so it can listen
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    # Receive the message and the client's address
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # Process the message (turn it to uppercase)
    modifiedMessage = message.decode().upper()
    
    # Send it back to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)