from Seq1 import Seq
print("----| Exercise 9|------")
s = Seq()
s.seq_read_fasta("U5.txt")

print(f"Sequence: (Length: {s.len()}) {s}")
print(f"\tBases: {s.count()}")
print(f"\tRev: {s.reverse()}")
print(f"\tComp: {s.complement()}")