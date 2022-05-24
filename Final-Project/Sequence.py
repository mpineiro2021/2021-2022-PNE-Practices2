class Seq:
    BASES_ALLOWED = ["A", "C", "G", "T"]
    COMPLEMENTS = {"A": "T", "C": "G", "G": "C", "T": "A"}
    NUMBERS = COMPLEMENT = {"A": 2, "C": -1, "G": 3, "T": 5}
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

    def info(self):
        result = f"sequence: {self.bases}\n"
        result = f"Total length: {self.len()}\n"
        most_frequent_base = None
        for base, count in self.count().items():
            result += f"{base}: {count} ({((count*100) / self.len()):.1f}%)\n"
            if most_frequent_base:
                if count > self.count_base(most_frequent_base):
                    most_frequent_base = base
            else:
                most_frequent_base = base
        result += f"Most frequent base: {most_frequent_base}"
        return result

    def multiply(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return f"We could not multiply the bases since the sequence is not correct."
        numb = 1
        for base in self.bases:
            numb = numb * Seq.NUMBERS[base]
        return numb










