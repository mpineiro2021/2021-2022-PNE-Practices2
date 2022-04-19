import socket
import termcolor
import pathlib


# -- Server network parameters
IP = "localhost"
PORT = 8080


def process_client(client_socket):
    # -- Receive the request message
    request_bytes = client_socket.recv(2048)
    request = request_bytes.decode()

    print("Message FROM CLIENT:")
    lines = request.splitlines()
    request_line = lines[0]
    slices = request_line.split(" ")
    method = slices[0]
    path = slices[1]
    version = slices[2]
    print("Request line: ", end="")
    termcolor.cprint(request_line, "green")

    #HTTP Response
    body = ""
    '''if path == "/info/A":
        body = Path("A.html").read_text()
    elif path == "/info/C":
        body = Path("C.html").read_text()
        
    elif path == "/info/G":
        body = Path("G.html").read_text()
    elif path == "/info/T":
        body = Path("T.html").read_text()'''
    if path == "/":
        body = Path("index1.html").read_text()
        status_line = "HTTP/1.1 200 OK\n"

    elif path.startswith("/info/"):
        slices = path.split("/")
        resource = slices[2]
        try:
            body = Path(f"{resource}.html").read_text()
            status_line = "HTTP/1.1 200 OK\n"
        except FileNotFoundError:
            body = Path("error.html").read_text()
            status_line = "HTTP/1.1 404 NOT_FOUND\n"
    else:
        body = Path("error.html").read_text()
        status_line = "HTTP/1.1 404 NOT_FOUND\n"

    header = "Content-Type: text/html\n"#devuelve texto con formato html
    header += f"Content-Length: {len(body)}\n"
    response = status_line + header + "\n" + body
    response_bytes = response.encode()
    client_socket.send(response_bytes)




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))

server_socket.listen()

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