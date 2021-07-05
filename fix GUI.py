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


def goAhead(name):
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip_chat, port_chat))
    
    server.send(bytes(name, "utf-8"))
    
    login.destroy()
    layout(name)
    
    #thread to receive message
    thread_cli = threading.Thread(target=baca_pesan, args=(server,))
    thread_cli.start()
    
    print("Selamat datang, kamu sudah masuk kedalam chat room!")
    
def layout(name):
    name = name
    
    root.deiconify()
    
    root.title("CHATROOM EMO")
    
    root.resizable(width = False, height = False)
    
    root.configure(width = 470,height = 550,bg = "#17202A")
    
    labelHead = Label(root,bg = "#17202A", fg = "#EAECEE",text = name , font = "Helvetica 13 bold",pady = 5)
    
    labelHead.place(relwidth = 1)
    
    line = Label(root,width = 450, bg = "#ABB2B9")
    
    line.place(relwidth = 1,rely = 0.07,relheight = 0.012)
    
    textCons = Text(root,width = 20,height = 2,bg = "#17202A",fg = "#EAECEE",font = "Helvetica 14", padx = 5,pady = 5)
    
    textCons.place(relheight = 0.745,relwidth = 1, rely = 0.08)
    
    labelBottom = Label(root,bg = "#ABB2B9",height = 80)
    
    labelBottom.place(relwidth = 1,rely = 0.825)
    
    entryMsg = Entry(labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
    
    entryMsg.place(relwidth = 0.74,
                            relheight = 0.06,
                            rely = 0.008,
                            relx = 0.011)
    
    entryMsg.focus()
    
    #send button
    buttonMsg = Button(labelBottom,text = "Send",font = "Helvetica 10 bold",width = 20, bg = "#ABB2B9", command =lambda: sendButton(entryMsg.get()))
    
    buttonMsg.place(relx = 0.77,rely = 0.008, relheight = 0.06, relwidth = 0.22)
    
    textCons.config(cursor = "arrow")
    
    scrollbar = Scrollbar(textCons)
    scrollbar.place(relheight = 1,
                        relx = 0.974)
    scrollbar.config(command = textCons.yview)
    textCons.config(state = "DISABLED")
    
def sendButton(msg):
    textCons.config(state = DISABLED)
    msg=msg
    entryMsg.delete(0, END)

def sendMessage():
    textCons.config(state=DISABLED)
    while True:
        message = (f"{self.name}: {self.msg}")
        
        #### masukkan code kirim pesan di sini
        #####
        #####
        #####
        break
    
def baca_pesan():
    while True:
        try:
            #receive msg
            data = server.recv(65535).decode("utf-8")
              
            # if the messages from the server is NAME send the client's name
            if message == 'NAME':
                print("hai")
                ########### kirim nama client e
                
            elif len(data) == 0:
                break
                
            else:
                # insert messages to text box
                textCons.config(state = NORMAL)
                textCons.insert(END,
                                     message+"\n\n")
                  
                textCons.config(state = DISABLED)
                textCons.see(END)
        except:
            # an error will be printed on the command line or console if there's an error
            print("An error occured!")
            client.close()
            break 
    

#ngebuat tampilan utama hide
root = tk.Tk()
root.withdraw()

#login window
login = Toplevel()
login.title("login EMO")
login.resizable(width=False,height=False)
login.configure(width = 400,height = 300)

#label
pls = Label(login, text = "Please login to continue",justify = CENTER, font = "Helvetica 14 bold")
pls.place(relheight = 0.15,relx = 0.2,rely = 0.07)
labelName = Label(login,text = "Name: ",font = "Helvetica 12")
labelName.place(relheight = 0.2,relx = 0.1,rely = 0.2)


#create a entry box
entryName = Entry(login,font = "Helvetica 14")
entryName.place(relwidth = 0.4,relheight = 0.12,relx = 0.35,rely = 0.2)
entryName.focus()

# create a Continue Button 
# along with action
go = Button(login,text = "CONTINUE", font = "Helvetica 14 bold", command = lambda: goAhead(entryName.get()))
go.place(relx = 0.4,rely = 0.55)

root.mainloop()
    
    
    
    
    
    