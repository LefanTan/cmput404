import socket, sys

HOST = ''
PORT = 8080
PAYLOAD = f'GET / HTTP/1.0\r\nHost: {HOST}\r\n\r\n'
buffer_size = 4096

# creates a socket
def create_tcp_socket():
    print("Create socket")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])}, Error: Message: {msg[1]}')
        sys.exit()
    print('Socket created!')
    return s

# Get IPv4 address from hostname
def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
    print(f'Host ip address is {host} is {remote_ip}')
    return remote_ip

def send_data(clientsocket, payload):
    print("sending paylaod")
    try:
        clientsocket.sendall(payload.encode())
    except socket.error:
        print("send payload fail")
        sys.exit()
    print("Payload sent successfully")


def main():
    try:
        #create socket for the client
        s = create_tcp_socket()

        remote_ip = get_remote_ip(HOST)

        # connect to socket at remote_ip of PORT
        s.connect((remote_ip, PORT))
        print(f'Socket connected to {HOST} on {remote_ip}')

        send_data(s, PAYLOAD)

        # shutdown the sends, but receive is still allowed
        s.shutdown(socket.SHUT_WR)

        # print more data receved from socket
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        # close 
        s.close()

if __name__ == "__main__":
    main()
