from Seq0 import *

FOLDER = "./sequences/"
GENES = ["U5", "FRAT1", "ADA","FXN","RNU6_269P"]
BASES = ["A","C","T","G"]
for gene in GENES:
    filename = gene + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {gene}:")
    for base in BASES:
        print(f"  {base}: {seq_count_base(sequence, base)}")

