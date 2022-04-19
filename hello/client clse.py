import socket

# SERVER IP, PORT
PORT = 8080
IP = "127.0.0.1"

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))
print("Testing PING")
s.send(str.encode("Ping"))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = s.recv(2048)
print( msg.decode("uft-8"))

print("MESSAGE FROM THE SERVER:\n")
print(msg.decode("utf-8"))#imprime msg dsd el server


c = Client(IP,PORT)

print("Get 0", msg.decode("uft-8"))
msg = c.talk("Get 0")
print("Get 0", msg.decode("uft-8"))
msg = c.talk("Get 0")
print("Get 0: ",msg)

print("Tesyting info", msg.decode("uft-8"))
msg = c.talk("AAAAAACCCTGGG")
print(msg)









# Closing the socket
s.close()