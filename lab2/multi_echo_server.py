import socket, time
from multiprocessing import Process

# local 
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((HOST, PORT))
        s.listen(2)

        print("Listening....")

        # keep listening for connection
        while True:
            conn, addr = s.accept()
            p = Process(target=handle_echo, args=(addr,conn))
            p.daemon = True
            p.start()
            print("Started process ", p)
            


def handle_echo(addr, conn):
    print("Connected by", addr)

    #receive data, wait a bit then send it back
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == "__main__":
    main()