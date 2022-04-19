from Seq1 import Seq

print("----| Exercise 5 |------")
seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence") ]
for index, seq in enumerate(seq_list):
    print(f"Sequence{index}: (Length: {seq.len()}) {seq}")
    for base in Seq.BASES_ALLOWED:
        print(f"{base}: {seq.count_base(base)}", end=" ")
    print()