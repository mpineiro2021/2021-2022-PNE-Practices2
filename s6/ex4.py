import termcolor
from Seq1 import Seq

def print_seqs(seq_list, color):
    for index, seq in enumerate(seq_list):
        termcolor.cprint(f"Sequence {index}: (length: {seq.len()}) {seq}",color)

def generate_seqs(pattern, number):
    seq_list = []
    bases = pattern
    for _ in range(number):
        seq_list.append(Seq(bases))
        bases += pattern

    return seq_list




seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, 'blue')

print()
termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, 'green')