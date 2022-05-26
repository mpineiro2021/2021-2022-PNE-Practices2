import http.client
import json
from pathlib import Path
HTML_FOLDER = "./html/"

def read_html_file(filename):
    contents = Path( HTML_FOLDER + filename).read_text()#./html/ping.html
    contents = j.Template(contents)#crea una plantilla de ese nombre
    return contents



def info_server(ENDPOINT):
    SERVER = 'rest.ensembl.org'
    PARAMS = '/' + f"?content-type=application/json"
    URL = SERVER + ENDPOINT + PARAMS
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    data = r1.read().decode("utf-8")
    data = json.loads(data)
    return data

