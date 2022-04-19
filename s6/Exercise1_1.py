from Seq1 import Seq
st1 = ["ACCTGC","Hello? Am I a valid sequence?"]
sequence_list = []
for st in st1:
    if Seq.validate_sequence2(st):
        sequence_list.append(Seq(st))
    else:
        sequence_list.append("Error")

for i in range(0,len(sequence_list)):
    print("Sequence", str(i)+":",sequence_list[i])


