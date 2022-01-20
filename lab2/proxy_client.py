import socket

# A client that connects to a proxy server thats between this client and google

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

PAYLOAD = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(PAYLOAD.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)

    except Exception as e:
        print(e)
    finally:
        s.close()


def main():
    # proxy_server host ip and port
    connect(('127.0.0.1', 8000))

if __name__ == "__main__":
    main()
