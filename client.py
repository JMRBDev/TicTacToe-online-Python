import sys
from socket import socket, AF_INET, SOCK_DGRAM

def connectToServer():
    SERVER_IP = '127.0.0.1'
    PORT_NUMBER = 5000
    SIZE = 1024
    print("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

    mySocket = socket( AF_INET, SOCK_DGRAM )
    try:
        response = 'Connection stablished successfully'
        mySocket.sendto(response.encode(),(SERVER_IP,PORT_NUMBER))
    except KeyboardInterrupt:
        response = 'exit'
        mySocket.sendto(response.encode(),(SERVER_IP,PORT_NUMBER))

while True:
    connectToServer()