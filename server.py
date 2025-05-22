#! /bin/python
# server.py

import socket

IP_PORT = ('192.168.12.34', 9090)
mysocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

mysocket.bind(IP_PORT)
mysocket.listen()

while True:
    client, client_information = mysocket.accept()
    client_IP = client_information[0]
    print(f'A TCP connection is opened for {client_IP}')
  
    received_data = client.recv(1024)
    print(f'{client_IP} said: {received_data.decode()}')
  
    client.send(input("   ").encode())