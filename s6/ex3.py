
from Seq1 import *

def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        print(f"Sequence {index}: (length: {seq.len()}) {seq}")

def generate_seqs(pattern, number):
    seq_list = []
    bases = pattern
    for _ in range(number):
        seq_list.append(Seq(bases))
        bases += pattern

    return seq_list




seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)