import http.client
import json



PORT = 80
SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"Url: {URL}")

conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", URL)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

if r1.status == 200: #se puede cambiar por HTTPStatus.OK
    print(f"Response received!: {r1.status} {r1.reason}\n")
    print()

#1:32
data = r1.read().decode("utf-8")
ping = json.loads(data)
print(ping)

if ping == 1:
    print("PING OK!!! The database is running.")
else:
    print("Error!")
print(f"Content:{data}")