import socket, sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    s.sendall(b"GET / HTTP/1.1\nHost: www.google.com\n\n")
    response = s.recv(4096)
    print(response.decode())
    s.close()


if __name__ == "__main__":
    main()