from Client0 import Client
PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

SERVER_IP = "localhost"
SERVER_PORT = 8080
c = Client(SERVER_IP, SERVER_PORT)
print(c)


