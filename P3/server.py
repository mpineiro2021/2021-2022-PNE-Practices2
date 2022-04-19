import socket
import termcolor
from Sequence import Seq

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

'''def get_command(gene_number):
    #copiar el elif
return response'''

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:

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
        try:
            slices = msg.split(" ")
            command = slices[0]
            termcolor.cprint(f"{command}", 'green')
            response = ""

            if command == "PING":
                response = f"OK\n"

            elif command == "GET":
                genes_number = int(slices[1])
                gene = GENES[genes_number]
                sequence = Seq()
                filename = "U5.txt"
                sequence.seq_read_fasta(filename)
                response = f"{sequence}\n"

                #response = get_command(gene_number)

            elif command == "INFO":
                bases = slices[1]
                sequence = Seq(bases)
                response = f"{sequence.info()}\n"
            elif command == "COMP":
                bases = slices[1]
                sequence = Seq(bases)
                response = f"{sequence.complement()}\n"
            elif command == "REV":
                bases = slices[1]
                sequence = Seq(bases)
                response = f"{sequence.reverse()}\n"
            elif command == "GENE":
                gene = slices[1]
                sequence = Seq()
                filename = f"{gene}.txt"
                sequence.seq_read_fasta(filename)
                response = f"{sequence}\n"
            elif command == "MULT":
                bases = slices[1]
                sequence = Seq(bases)
                response = f"{sequence.multiply()}\n"


            else:
            # -- Send a response message to the client
                response = "This command is not available in the server\n"
        except Exception:
            response = f"ERROR : {command}\n"
        print(response)
        cs.send(response.encode())
        cs.close()
except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("Server stopped by the admin")
    cs.close()