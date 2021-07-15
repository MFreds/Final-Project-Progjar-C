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


ip_address = '127.0.0.1'
port = 8081

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# binding socket object to IP addr and certain port
server.bind((ip_address, port))

# create dictionary for client's info
# clients = {}

# untuk jumlah client
list_of_clients, client_name= [],[]
# ready_client_addr = []


# def remove(connection):
#     if connection in ready_client:
#         ready_client.remove(connection)


def mulaiChat():

    print("Server sudah bekerja")
    # listen for an incoming connection
    server.listen()

    while True:
        # get connection
        conn, addr = server.accept()

        # returns a new connection to the client
        # and  the address bound to it
        conn.send("NAME".encode("utf-8"))

        # calculate how many connection in list
        # size = 0
        # for x in list_of_clients:
        #     size += 1
        # print(list_of_clients[size - 1])
        # print('connected\n')
        # print("sum of client is: ", size)

        # ambil username client
        username_cli = conn.recv(65535).decode("utf-8")

        # put the connection to list
        client_name.append(username_cli)
        list_of_clients.append(conn)

        # print(username_cli, "joined")
        print(f"Name is :{username_cli}")

        # broadcast message
        kirim_broadcast(f"{username_cli} has joined the chat!".encode("utf-8"))
        conn.send('Connection successful!'.encode("utf-8"))

        # create new thread for msg read and relay the thread
        thread_cli = threading.Thread(target=baca_pesan, args=(conn, addr))
        thread_cli.start()

        # no. of clients connected
        # to the server
        print(f"active connections {threading.activeCount() - 1}")

        # # save client info to dictionary
        # clients[username_cli] = (conn, addr, thread_cli)

# membaca pesan
def baca_pesan(conn, addr):

    print(f"new connection {addr}")
    connected = True
    while connected:
        # menerima pesan
        msg = conn.recv(65535)

        # if len(data) == 0:
        #     break

        # parsing msg
        # dest, msg_raw = data.decode("utf-8").split("|")
        # msg = "<{}>: {}".format(username_cli, msg_raw)

        # print(msg)

        # relay msg to all client
        kirim_broadcast(msg)
        # if dest == "broadcast":
        #     kirim_broadcast(msg)

        # direct msg
        # else:
        #     dest_sock_cli = clients[dest][0]
        #     send_msg(dest_sock_cli, msg)

    conn.close()
    # print("Connection Closed", addr)

# send message to all client
def kirim_broadcast(message):
    for client in list_of_clients:
        client.send(message)

# panggil method untuk memulai komunikasi
mulaiChat()

