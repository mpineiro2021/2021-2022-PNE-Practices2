from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

SERVER_IP = "localhost"
SERVER_PORT = 8081 #cuando el cliente se conecta al servidor el puerto tiene que ser en el que has hecho el bind en el servidor
c = Client(SERVER_IP, SERVER_PORT)
genes_list = ["U5", "FRAT1", "ADA"]
for gene in genes_list:
    s = Seq()
    s.seq_read_fasta(f"{gene}.txt")
    c.debug_talk(f"Sending {gene} to the server...")
    c.debug_talk(str(s))#el objeto tipo seq se transforma a un string y llama a la función str


