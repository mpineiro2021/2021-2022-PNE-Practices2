import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from Sequence import Seq
import http.client
import json




def read_html_file(filename):
    contents = Path( HTML_FOLDER + filename).read_text()#./html/ping.html
    contents = j.Template(contents)#crea una plantilla de ese nombre
    return contents

SERVER = 'rest.ensembl.org'
HTML_FOLDER = "./html/"
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)# a la función urlparse se le pasa el path
        path = url_path.path #endpoint
        arguments = parse_qs(url_path.query)#parameters
        print(path, arguments)

        if path == "/":
            contents = read_html_file("index.html").render()

        elif path == "/listSpecies":

            ENDPOINT = '/info/species'
            PARAMS = "?content-type=application/json"
            conn = http.client.HTTPConnection(SERVER)
            try:
            conn.request("GET", ENDPOINT + PARAMS)
            except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()
            r1 = conn.getresponse()
            data = r1.read().decode("utf-8")
            data = json.loads(data)

        if len(arguments) == 0:
            limit = None
            species = data['species']
            context_html = {
            "total": len(species),
            "species": species,
            "limit": limit
            }
            contents = read_html_file("./html/species.html").render(context=context_html)
            elif len(arguments) == 1:
            try:
            limit = int(arguments['limit'][0])
            species = data['species']
            context_html = {
            "total": len(species),
            "species": species,
            "limit": limit
            }
            contents = read_html_file("./html/species.html").render(context=context_html)
        except Exception:
        contents = read_html_file(HTML_FOLDER + "error.html")


        else:
        contents = Path("error.html").read_text()

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
Handler = TestHandler

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