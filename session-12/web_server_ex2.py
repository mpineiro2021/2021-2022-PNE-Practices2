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
    lines = request.splitlines()
    request_line = lines[0]
    slices = request_line.split(" ")
    method = slices[0]
    path = slices[1]
    version = slices[2]
    print("Request line: ", end="")
    termcolor.cprint(request_line, "green")

    #HTTP Response
    body = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Green server</title>
      </head>
      <body style="background-color: lightgreen;">
        <h1>GREEN SERVER</h1>
        <p>I am the Green Server! :-)</p>
      </body>
    </html>
    """
    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/plain\n"#devuelve texto con formato plano asiq el body se ve tal cual
    header += f"Content-Length: {len(body)}\n"
    response = status_line + header + "\n" + body
    response_bytes = response.encode()
    client_socket.send(response_bytes)
