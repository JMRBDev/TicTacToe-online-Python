from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import os

def createServer():
    PORT_NUMBER = 5000
    SIZE = 1024

    hostName = gethostbyname('')

    mySocket = socket( AF_INET, SOCK_DGRAM )
    mySocket.bind( (hostName, PORT_NUMBER) )

    print("Tic Tac Toe server listening on port {0}\n".format(PORT_NUMBER))

    while True:
        (data,addr) = mySocket.recvfrom(SIZE)

        if data == 'exit':
            (data,addr) = mySocket.recvfrom(SIZE)
            print('Exiting application...')
            exit()
        else:
            (data,addr) = mySocket.recvfrom(SIZE)
            print(data)

createServer()