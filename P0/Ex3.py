
from Seq0 import *

FOLDER = "./sequences/"
GENES = ["U5", "FRAT1", "ADA","FXN","RNU6_269P"]
for gene in GENES:
    filename = gene + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {gene}---> length: {seq_len(sequence)}")
