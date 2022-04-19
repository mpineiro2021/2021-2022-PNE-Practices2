import socket
def count_bases(seq):
    d = {"A":0,"C":}
    for b in seq:
        d[b] +=1
        total = sum(d.values())
        p = d = {"A":0,"C":}
        for k,v in d.items():
            d[k] = [v,(v * 100)/ total]
        return d
    def convert_message(bases_count):
        message = ""
        for k,v in bases_count.items():
            message += k+': '+ str(v[0]) + '( '+ str(v[1]) + '%)'+\n''
        return message
def info_operation(arg ):
    response += "Sequence: " + arg + "\n" + response
    response += "Total length: " + str(len(arg) + '\n'
    response = convert_message(bases_count)
    return response

SEQUENCES['AAAAA''ACGT''CCTAG']

    # -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()

    print("A client has connected to the server!")

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode().replace("\n","").strip()
    split_list= msg.split(" ")
    cmd = split_list[0]
    if msg =! "PING":
        arg = split_list[1]
    print("This is printed the server ")
    print(len(msg))#para comprobar si entra en if
    if msg == "PING":
        response = "Ping OK!!!"
    elif cmd == "REV":
        response = arg[::-1]

    elif cmd "INFO":
        response = info_operation(arg)
        bases_count = count_bases(arg)
    elif cmd == "COMP":
        seq = Seq(arg)
        response = seq.complement()
    elif cmd == "GET":
        try:
            index = int(arg)
            response = SEQUENCE[index]
        except ValueError:
            response = 'The argument for the get command must be a number 0-4' '
        except IndexError:
            response = 'The argument must be btw 0-4'


    # -- Print the received message
    print(f"Message received: {msg}")

    # -- Send a response message to the client
    response = "HELLO. I am the Happy Server :-)\n"

    # -- The message has to be encoded into bytes
    cs.send(response.encode())

    # -- Close the data socket
    cs.close()