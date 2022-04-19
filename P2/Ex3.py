
from Client0 import Client
PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

SERVER_IP = "localhost"
SERVER_PORT = 8081 #cuando el cliente se conecta al servidor el puerto tiene que ser en el que has hecho el bind en el servidor
c = Client(SERVER_IP, SERVER_PORT)
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
