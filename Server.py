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


class ServerChat:
    # untuk jumlah client
    list_of_clients = []

    last_received_message = ""

    def __init__(self):
        self.server = None
        self.create_listening_server()

    def create_listening_server(self):
        # create socket

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip_address = '127.0.0.1'
        port = 8081
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # binding socket object to IP addr and certain port
        self.server.bind((ip_address, port))

        print("Listening for incoming messages..")
        self.server.listen(4)

        self.terima_pesan_melalui_thread()

    # menerima pesan
    def baca_pesan(self, conn):
        while True:
            # menerima pesan
            msg = conn.recv(256)
            if not msg:
                break
            self.last_received_message = msg.decode('utf-8')
            # if len(data) == 0:
            #     break

            # parsing msg
            # dest, msg_raw = data.decode("utf-8").split("|")
            # msg = "<{}>: {}".format(username_cli, msg_raw)

            # print(msg)

            # relay msg to all client
            self.kirim_broadcast(conn)
            # if dest == "broadcast":
            #     kirim_broadcast(msg)

            # direct msg
            # else:
            #     dest_sock_cli = clients[dest][0]
            #     send_msg(dest_sock_cli, msg)

        conn.close()
        # print("Connection Closed", addr)
    # create dictionary for client's info
    # clients = {}

    # send message to all client
    def kirim_broadcast(self, so_pengirim):
        for client in self.list_of_clients:
            socket, (ip, port_a) = client
            if socket is not so_pengirim:
                socket.sendall(self.last_received_message.encode('utf-8'))

    def terima_pesan_melalui_thread(self):
        while True:
            client = conn, (ip, port) = self.server.accept()
            self.tambah_list_client(client)
            print('Tersambung ke ', ip, ':', str(port))
            t = threading.Thread(target=self.baca_pesan, args=(conn,))
            t.start()

    # add a new client
    def tambah_list_client(self, client):
        if client not in self.list_of_clients:
            self.list_of_clients.append(client)

if __name__ == "__main__":
    ServerChat()

    # def remove(connection):
    #     if connection in ready_client:
    #         ready_client.remove(connection)


    # def mulaiChat():
    #
    #     print("Server sudah bekerja")
    #     # listen for an incoming connection
    #
    #
    #     while True:
    #         # get connection
    #         conn, addr = server.accept()
    #
    #         # returns a new connection to the client
    #         # and  the address bound to it
    #         conn.send("NAME".encode("utf-8"))
    #
    #         # calculate how many connection in list
    #         # size = 0
    #         # for x in list_of_clients:
    #         #     size += 1
    #         # print(list_of_clients[size - 1])
    #         # print('connected\n')
    #         # print("sum of client is: ", size)
    #
    #         # ambil username client
    #         username_cli = conn.recv(65535).decode("utf-8")
    #
    #         # put the connection to list
    #         client_name.append(username_cli)
    #         list_of_clients.append(conn)
    #
    #         # print(username_cli, "joined")
    #         print(f"Name is :{username_cli}")
    #
    #         # broadcast message
    #         kirim_broadcast(f"{username_cli} has joined the chat!".encode("utf-8"))
    #         conn.send('Connection successful!'.encode("utf-8"))
    #
    #         # create new thread for msg read and relay the thread
    #         thread_cli = threading.Thread(target=baca_pesan, args=(conn, addr))
    #         thread_cli.start()
    #
    #         # no. of clients connected
    #         # to the server
    #         print(f"active connections {threading.activeCount() - 1}")
    #
    #         # # save client info to dictionary
    #         # clients[username_cli] = (conn, addr, thread_cli)


# # panggil method untuk memulai komunikasi
# mulaiChat()

