import socket
import sys
import os

BUFFER_SIZE = 1024
PORT = 1234  # You can choose any port number


def server_mode(directory):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', PORT))

    while True:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        filename = data.decode()
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8-sig') as file:
                content = file.readline()
                while content:
                    server_socket.sendto(content.encode(), addr)
                    content = file.readline()
        else:
            server_socket.sendto('File not found'.encode(), addr)


def client_mode(filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client_socket.bind(('', PORT))
    client_socket.settimeout(5)  # Set a timeout for receiving responses

    client_socket.sendto(filename.encode(), ('<broadcast>', PORT))

    with open(filename, 'w') as f:
        while True:
            try:
                data, addr = client_socket.recvfrom(BUFFER_SIZE)
                if data.decode() == 'File not found':
                    print('File not found on the server.')
                    break
                f.write(data.decode() + "\n")
            except socket.timeout:
                print('Timeout: No response from the server.')
                break


def main():
    mode = sys.argv[1]
    if mode == '-server':
        if len(sys.argv) < 3:
            print('Directory not specified. Usage: python main.py -server <directory>')
            return
        directory = sys.argv[2]
        if not os.path.isdir(directory):
            print('Invalid directory. Please provide a valid directory.')
            return
        server_mode(directory)
    elif mode == '-receive':
        if len(sys.argv) < 3:
            print('Filename not specified. Usage: python main.py -receive <filename>')
            return
        filename = sys.argv[2]
        client_mode(filename)
    else:
        print('Invalid mode. Use -server or -receive.')


if __name__ == '__main__':
    main()
