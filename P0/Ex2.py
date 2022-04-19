import Seq0
filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename)
print(f"DNA file: {filename}")
print("The first 20 bases are:")
print(sequence[:20])