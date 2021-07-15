#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 13:52:26 2021

@author: basuki
"""

import socket
import select
import sys
from threading import Thread
import os
import socket
import sys
import threading
import time

import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk

ip_chat = '127.0.0.1'
port_chat = 8081

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_chat, port_chat))

# GUI class for the chat
class GUI:
    # constructor method
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

        # login window
        self.login = Toplevel()
        self.login.title("login EMO")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)

        # label
        self.pls = Label(self.login, text="Please login to continue", justify=CENTER, font="Helvetica 14 bold")
        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)
        self.labelName = Label(self.login, text="Name: ", font="Helvetica 12")
        self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)

        # create a entry box
        self.entryName = Entry(self.login, font="Helvetica 14")
        self.entryName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entryName.focus()

        # create a Continue Button
        # along with action
        self.go = Button(self.login, text="CONTINUE", font="Helvetica 14 bold", command=lambda: self.goAhead(self.entryName.get()))
        self.go.place(relx=0.4, rely=0.55)

        self.root.mainloop()

    def goAhead(self,name):

        # client.send(bytes(name, "utf-8"))

        self.login.destroy()
        self.layout(name)

        # thread to receive message
        thread_cli = threading.Thread(target=self.baca_pesan)
        thread_cli.start()
        #
        # print("Selamat datang, kamu sudah masuk kedalam chat room!")


    def layout(self,name):
        self.name = name

        self.root.deiconify()

        self.root.title("CHATROOM EMO")

        self.root.resizable(width=False, height=False)

        self.root.configure(width=470, height=550, bg="#17202A")

        self.labelHead = Label(self.root, bg="#17202A", fg="#EAECEE", text=self.name, font="Helvetica 13 bold", pady=5)

        self.labelHead.place(relwidth=1)

        self.line = Label(self.root, width=450, bg="#ABB2B9")

        self.line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.textCons = Text(self.root, width=20, height=2, bg="#B8D8BE", fg="#EAECEE", font="Helvetica 14", padx=5, pady=5)

        self.textCons.place(relheight=0.745, relwidth=1, rely=0.08)

        self.labelBottom = Label(self.root, bg="#ABB2B9", height=80)

        self.labelBottom.place(relwidth=1, rely=0.825)

        self.entryMsg = Entry(self.labelBottom,
                         bg="#2C3E50",
                         fg="#EAECEE",
                         font="Helvetica 13")

        self.entryMsg.place(relwidth=0.74,
                       relheight=0.06,
                       rely=0.008,
                       relx=0.011)

        self.entryMsg.focus()

        # send button
        self.buttonMsg = Button(self.labelBottom, text="Send", font="Helvetica 10 bold", width=20, bg="#ABB2B9",
                           command=lambda: self.sendButton(self.entryMsg.get()))

        self.buttonMsg.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        self.textCons.config(cursor="arrow")

        scrollbar = Scrollbar(self.textCons)
        scrollbar.place(relheight=1,
                        relx=0.974)
        scrollbar.config(command=self.textCons.yview)
        self.textCons.config(state="DISABLED")


    def sendButton(self,msg):
        self.textCons.config(state=DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, END)
        send = threading.Thread(target=self.sendMessage)
        send.start()

    def baca_pesan(self):
        while True:
            try:
                # receive msg
                message = client.recv(65535).decode("utf-8")

                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    # print("hai")
                    ########### kirim nama client e
                    client.send(name.encode("utf-8"))

                else:
                    # insert messages to text box
                    self.textCons.config(state=NORMAL)
                    self.textCons.insert(END,
                                    message + "\n\n")

                    self.textCons.config(state=DISABLED)
                    self.textCons.see(END)
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                client.close()
                break

            # ngebuat tampilan utama hide

    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode("utf-8"))
            break

# create a GUI class object
g = GUI()



