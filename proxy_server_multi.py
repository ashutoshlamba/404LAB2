#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process
#define address & buffer size
HOST = ""
PORT = 8080
BUFFER_SIZE = 4096

def handle_multi(conn,google):
    full_data = conn.recv(BUFFER_SIZE)
    google.sendall(full_data)
    google.shutdown(socket.SHUT_WR)
    google_data = google.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(google_data)
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(1)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            google = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            google.connect(("www.google.com", 80))
            p = Process(target=handle_multi, args=(conn, google),daemon=True)
            p.start()

if __name__ == "__main__":
    main()