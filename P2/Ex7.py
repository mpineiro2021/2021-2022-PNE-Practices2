from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 7
GENE = "FRAT1"
FRAGMENTS = 10
BASES = 10

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

SERVER_IP = "localhost"
SERVER1_PORT = 8084 #cuando el cliente se conecta al servidor el puerto tiene que ser en el que has hecho el bind en el servidor
SERVER2_PORT = 8085

c1 = Client(SERVER_IP, SERVER1_PORT)
print(c1)
c2 = Client(SERVER_IP, SERVER2_PORT)
print(c2)


s = Seq()
s.seq_read_fasta(f"{GENE}.txt")

print(f"Gene {GENE}: {s}")

c1.debug_talk(f"Sending {GENE} to the server, in fragments of {BASES} bases")
c2.debug_talk(f"Sending {GENE} to the server, in fragments of {BASES} bases")

start_index = 0
end_index = BASES

for f in range(1, FRAGMENTS + 1):
    fragment = s.bases[start_index:end_index]
    print(f"Fragment {f}: {fragment}")
    if f % 2 == 0:
        c2.debug_talk(f"Fragment {f}: {fragment}")
    else:
        c1.debug_talk(f"Fragment {f}: {fragment}")
    start_index += BASES
    end_index += BASES