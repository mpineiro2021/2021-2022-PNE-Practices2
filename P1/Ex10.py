from Seq1 import Seq
GENES = ["U5", "FRAT1", "ADA","FXN","RNU6_269P"]
for gene in GENES:
    filename = gene +".txt"
    try:
        seq = Seq()
        seq.seq_read_fasta(filename)
        appearances = seq.count()
        most_frequent = None
        for base, count in appearances.items():
            if most_frequent:
                if count > most_frequent[1]:
                    most_frequent = (base, count)
            else:
                most_frequent = (base, count)
        print(f"Gene {gene}: {most_frequent[0]}")
    except FileNotFoundError:
        print(f"[ERROR]. file '{filename}' not found")