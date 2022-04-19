class Seq:
    BASES_ALLOWED= ["A","C","G","T"]

    def __init__(self,bases):#no se retorna nada en la init function
        if Seq.validate_sequence(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("Incorrect sequence detected!")

    @staticmethod
    def validate_sequence(bases):
        valid = len(bases) != 0
        i = 0
        while i < len(bases) and valid:
            if bases[i] in Seq.BASES_ALLOWED:
                i += 1
            else:
                valid = False
        return valid


    '''def validate_sequence(self):
        valid = True
        i = 0
        while i < len(self.bases) and valid:
            c = self.bases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid'''

    def __str__(self):
        # -- We just return the string with the sequence
        return self.bases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.bases)

'''class Gene(Seq):
    def __init__(self, bases, name=""):
        super().__init__(bases)
        self.name = name
        print("New gene created!!!")
    def __str__(self):
        return self.name +"-"+self.bases

s1= Seq("AGTACACTGGT")
g = Gene("CGTAAC","FRAT1")
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Gene: {g}")
print(f"  Length: {g.len()}")'''
