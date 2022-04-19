import socket
import termcolor

PORT = 8080
IP = "localhost"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
n = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print(f"Waiting for connections at {IP}, {PORT}... ")
        (client_socket, client_address) = serversocket.accept()
        n += 1
        print(f"CONNECTION: {n} from ({client_address})")
        msg_bytes = client_socket.recv(2048)
        msg = msg_bytes.decode("utf-8")
        print(f"Message from client: ", end="")
        termcolor.cprint(msg, 'green')
        msg = "Hello from the teacher's server"
        msg_bytes = str.encode(msg)
        # We must write bytes, not a string
        client_socket.send(msg_bytes)
        client_socket.close()

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()