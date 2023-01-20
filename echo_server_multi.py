#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def echo_back(conn):
    full_data = conn.recv(BUFFER_SIZE)
    print("revieved payload:")
    print(full_data)
    time.sleep(0.5)
    conn.sendall(full_data)
    print("closing")
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
    
    
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            #create process for new connections
            p = Process(target=echo_back, args=(conn,),daemon=True)
            p.start()

if __name__ == "__main__":
    main()
