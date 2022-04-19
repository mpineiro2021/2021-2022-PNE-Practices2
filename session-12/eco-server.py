import socket
import termcolor


# -- Server network parameters
IP = "localhost"
PORT = 8080


def process_client(client_socket):
    # -- Receive the request message
    request_bytes = client_socket.recv(2048)
    request = request_bytes.decode()

    print("Message FROM CLIENT:")
    termcolor.cprint(request, "green")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
server_socket.bind((IP, PORT))

# -- Become a listening socket
server_socket.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
try:
    while True:
        print("Waiting for clients....")

        (client_socket, client_address) = server_socket.accept()
        process_client(client_socket)

        client_socket.close()
except KeyboardInterrupt:
    print("Server Stopped!")
    server_socket.close()
