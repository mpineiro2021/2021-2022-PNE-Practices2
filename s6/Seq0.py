
BASES = ["A","C","T","G"]
COMPLEMENTS = {"A": "T", "C": "G", "G": "C", "T": "A"}

def seq_ping():
    print("Ok")
def valid_filename():
    exit = False
    FOLDER = "./sequences/"
    while not exit:
        filename = input("Which file do you want to open: ")
        filename = FOLDER + filename

        try:
            f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File doesn't exist")

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    sequence = ""
    for line in body:
        sequence += line
    return sequence



def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)
    '''for b in seq:
        if b == base:
            total += 1
    return total'''

def seq_count(seq):
    d = {}
    for base in BASES:
        d[base] = seq_count_base(seq,base)
    return d

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    d = ""
    for base in seq:
        d += COMPLEMENTS[base]
    return d

def most_frequent_base(seq):
    max_base = None
    max_count = 0
    for base, count in seq_count(seq).items(): # para recorrer las claves y valores del diccionario que cuenta las bases
        if count >= max_count: # por si la primera base es = 0, así max_base tiene valor
            max_base = base
            max_count = count
    return max_base












