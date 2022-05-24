import http.client
import json




SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"Url: {URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()


print(f"Response received!: {r1.status} {r1.reason}\n")


print(data)
data = r1.read().decode("utf-8")
data = json.loads(data)


if data['ping'] == 1:
    print("PING OK!!! The database is running.")
else:
    print("Error!")

