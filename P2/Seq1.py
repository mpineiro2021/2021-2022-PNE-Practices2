class Seq:
    BASES_ALLOWED = ["A", "C", "G", "T"]
    COMPLEMENTS = {"A": "T", "C": "G", "G": "C", "T": "A"}
    @staticmethod
    def validate_sequence(bases):
        valid = len(bases) != 0
        i = 0
        while i < len(bases) and valid:
            if bases[i] not in Seq.BASES_ALLOWED:
                valid = False
            i += 1
        return valid

    def __init__(self, bases="NULL"):#no se retorna nada en la init functio

        if bases =="NULL":
            self.bases = bases
            print("NULL Sequence created!")
        elif Seq.validate_sequence(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = 'ERROR'
            print("INVALID sequence detected!")


    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or  self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def count(self):
        d = {}
        for base in Seq.BASES_ALLOWED:
            d[base] = self.count_base(base)
        return d

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        return self.bases[::-1]


    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        comp = ""
        for base in self.bases:
            comp += Seq.COMPLEMENTS[base]
        return comp


    def seq_read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line




