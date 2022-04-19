from Seq1 import Seq

print("----| Exercise 7 |------")
seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence") ]
for index, seq in enumerate(seq_list):
    print(f"Sequence{index}: (Length: {seq.len()}) {seq}")
    print(f"\tBases: {seq.count()}")
    print(f"\tRev: {seq.reverse()}")