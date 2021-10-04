# Declare the Sequence class
class Sequence(object):

    # Define the class constructor
    def __init__(self, sequence):

        # Define the instance attributes
        self._sequence = sequence

    @property
    def sequence(self):
        return self._sequence

    @property
    def length(self):
        return len(self._sequence)

if __name__ == "__main__":
    seq = "AACG"
    dna = Sequence(seq)
    print(dna.length)