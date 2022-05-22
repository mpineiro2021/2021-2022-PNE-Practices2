import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # We just print a message
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        print("  Path: " + self.path)
        route = self.requestline.split(" ")[1]
        try:
            if route == "/" or route == "/favicon.ico":
                contents = Path("form-ex1.html").read_text()
                self.send_response(200)

            elif route.startswith("/echo?"):#han rellenado y enviado el formulario
                parsed_url = urlparse(route)
                param = parse_qs(parsed_url.query)#diccionario con la clase msg y con valor asociado una lista con el string que recive
                try:
                    msg_param = param['msg'][0]#clave msg, accedo a la posición 0(la unica que hay)
                    contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                            <head>
                              <meta charset="utf-8">
                              <title>Result</title>
                            </head>
                            <body>
                              <h1>Received message</h1>
                              <p>{msg_param}</p>
                              <a href="http://127.0.0.1:8080">Main page</a>
                            </body>
                        </html>"""
                    self.send_response(200)
                except (KeyError, IndexError):
                    contents = Path(f"error.html").read_text()
                    self.send_response(404)
            else:
                contents = Path("error.html").read_text()
                self.send_response(404)


        except FileNotFoundError:
            contents = Path("error.html").read_text()
            self.send_response(404)

        # IN this simple server version:
        # We are NOT processing the client's request
        # We are NOT generating any response message

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = RequestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()