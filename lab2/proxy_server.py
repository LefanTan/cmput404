import socket, sys
from client import get_remote_ip

SERVER_HOST = ""
SERVER_PORT = 8000
BUFFER_SIZE = 1024

HOST = "www.google.com"
PORT = 80

def main():
    # Create a socket that connects to a server in front a client 
    # In order word, a normal proxy server
    # It works by creating a proxy server so a client can connect to it
    # then it also creates a proxy client that connects to google
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start:
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        start.bind((SERVER_HOST, SERVER_PORT))
        start.listen(1)

        while True:
            print("Listening for connection ...")
            conn, addr = start.accept()
            print("Connected by", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as end:
                print("Connecting to google")
                remote_ip = get_remote_ip(HOST)

                # connect proxy client to google
                end.connect((remote_ip, PORT))

                # get data from client 
                full_data = conn.recv(BUFFER_SIZE)
                print(f'Sending received data from client - {full_data} to google')
                # send data to google
                end.sendall(full_data)

                end.shutdown(socket.SHUT_WR)
                data = end.recv(BUFFER_SIZE)
                print(f'Sending received data from google - {data} to client')
                # send data to cleint
                conn.send(data)

            conn.close()


if __name__ == "__main__":
    main()