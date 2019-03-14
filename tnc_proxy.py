#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Tomasz SQ5T

import socket
import threading

listen_address = "127.0.0.1" # listen IP, "" == listen all
listen_port = 8002 # listen port

destination_address = "127.0.0.1" # connect to IP
destination_port = 8001 # connect to port

def cli_msg(conn):
    while True:
            try:
                message = conn.recv(1024)
                if message:
                    broadcast(message, conn)
                else:
                    remove(conn)
                    return
            except:
                continue

# broadcast message to all connected clients
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)
                return

# remove connection
def remove(connection):
    connection.close()
    if connection in list_of_clients:
        list_of_clients.remove(connection)

list_of_clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((destination_address, destination_port))
list_of_clients.append(s)
main_connection = s

thread = threading.Thread(target=cli_msg, args=(s,))
thread.daemon = True
thread.start()

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

cli.bind((listen_address, listen_port)) # start listening
cli.listen(2) # max waiting connection

while True:
    conn,address = cli.accept() # accept connection from client
    conn.setblocking(1)
    list_of_clients.append(conn) # add client to array of clients
    thread_client = threading.Thread(target=cli_msg, args=(conn,))
    thread_client.daemon = True
    thread_client.start()
