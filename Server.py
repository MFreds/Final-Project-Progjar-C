#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:22:13 2021

@author: basuki
"""
import socket
import select
import sys
import threading
import socket
import threading

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = '127.0.0.1'
port = 8081

# binding socket object to IP addr and certain port
server.bind((ip_address, port))

# listen for an incoming connection
server.listen(4)

# create dictionary for client's info
clients = {}

# untuk jumlah client
list_of_clients = []
ready_client = []
ready_client_addr = []


def remove(connection):
    if connection in ready_client:
        ready_client.remove(connection)


# send message to all client
def kirim_broadcast(clients, data, sender_addr_cli):
    for conn, adrr, _ in clients.values():
        if not (sender_addr_cli[0] == addr[0] and sender_addr_cli[1] == addr[1]):
            kirim_pesan(conn, data)


# send direct msg
def kirim_pesan(conn, data):
    conn.send(bytes(data, "utf-8"))


# membaca pesan
def baca_pesan(clients, conn, addr, username_cli):
    while True:
        # menerima pesan
        data = conn.recv(65535)
        if len(data) == 0:
            break

        # parsing msg
        dest, msg_raw = data.decode("utf-8").split("|")
        msg = "<{}>: {}".format(username_cli, msg_raw)

        print(msg)
        # relay msg to all client
        if dest == "broadcast":
            kirim_broadcast(clients, msg, addr)

        # direct msg
        # else:
        #     dest_sock_cli = clients[dest][0]
        #     send_msg(dest_sock_cli, msg)

    conn.close()
    print("Connection Closed", addr)


while True:
    # get connection
    conn, addr = server.accept()

    # put the connection to list
    list_of_clients.append(conn)

    # calculate how many connection in list
    size = 0
    for x in list_of_clients:
        size += 1
    print(list_of_clients[size - 1])
    print('connected\n')
    print("sum of client is: ", size)

    # ambil username client
    username_cli = conn.recv(65535).decode("utf-8")
    print(username_cli, "joined")

    # create new thread for msg read and relay the thread
    thread_cli = threading.Thread(target=baca_pesan, args=(clients, conn, addr, username_cli))
    thread_cli.start()

    # save client info to dictionary
    clients[username_cli] = (conn, addr, thread_cli)

