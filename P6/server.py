import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from Sequence import Seq
import os


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
GENE_LIST = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
SEQUENCES_LIST = ["AAAAAAAAAT", "AAACCCCCCCTTTTGGGA", "CCCCCCCGGCGCA", "TTTATATATTATA", "GGGAGAGAGTCTCTCA", "TAATCGAAACCC"]

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
                contents = Path("html/index.html").read_text()
                self.send_response(200)
            elif route == "/ping?":
                parsed_url = urlparse(route)
                param = parse_qs(parsed_url.query)
                contents = Path("html/ping.html").read_text()

            elif route.startswith("/get"):#han rellenado y enviado el formulario
                parsed_url = urlparse(route)
                param = parse_qs(parsed_url.query)#diccionario con la clase msg y con valor asociado una lista con el string que recive
                try:
                    sequence = Seq()
                    sequence_number= int(param['sequence_number'][0])#clave sequence_number que eliges en el desplegable, accedo a la posición 0(la unica que hay)
                    filename = os.path.join(".","sequences", f"{SEQUENCES_LIST[sequence_number]}.txt")
                    sequence.seq_read_fasta(filename)
                    contents = Path("html/get.html")
                    self.send_response(200)

                except (ValueError, IndexError):
                    contents = Path(f"html/error.html").read_text()
                    self.send_response(404)

            elif route.startswith("/gene?"):
                parsed_url = urlparse(route)
                param = parse_qs(parsed_url.query)
                try:
                    sequence = Seq()
                    gene_name = param['gene_name'][0]#clave sequence_number que eliges en el desplegable, accedo a la posición 0(la unica que hay)
                    filename = os.path.join(".","sequences", f"{gene_name}.txt")
                    sequence.seq_read_fasta(filename)
                    contents = Path("html/gene.html").read_text()
                    self.send_response(200)

                except IndexError:
                    contents = Path(f"html/error.html").read_text()
                    self.send_response(404)
            elif route.startswith("/operation?"):
                parsed_url = urlparse(route)
                param = parse_qs(parsed_url.query)
                try:
                    bases = param['bases'][0]
                    operation = param['operation'][0]
                    if operation in ["complementary", "reverse", "information"]:
                        sequence = Seq(bases)
                        contents = Path("html/operation.html").read_text()
                        if operation == "information":
                            contents += f"<p> {sequence.info()}</p>"
                        elif operation == "complementary":
                            contents += f"<p> {sequence.complement()}</p>"
                        elif operation == "reverse":
                            contents += f"<p> {sequence.reverse()}</p>"
                        self.send_response(200)
                    else:
                        contents = Path("html/error.html").read_text()
                        self.send_response(404)
                except IndexError:
                    contents = Path("html/error.html").read_text()
                    self.send_response(404)
            else:
                contents = Path("html/error.html").read_text()
                self.send_response(404)


        except FileNotFoundError:
            contents = Path("html/error.html").read_text()
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