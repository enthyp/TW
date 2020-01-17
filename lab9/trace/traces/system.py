from itertools import product


class InputFormatError(Exception):
    pass


class System:
    def __init__(self, source, from_ind=True):
        try:
            alphabet, relation, word = self._from_file(source)
        except FileNotFoundError:
            try:
                alphabet, relation, word = self._from_string(source)
            except:
                raise InputFormatError

        self.alphabet = alphabet
        self.word = word

        if from_ind:
            self.ind_relation = relation
            self.dep_relation = self._complement(alphabet, relation)
        else:
            self.dep_relation = relation
            self.ind_relation = self._complement(alphabet, relation)

    def _from_file(self, filepath):
        with open(filepath, 'r') as input_file:
            content = input_file.read()
        return self._from_string(content)
  
    @staticmethod
    def _from_string(string):
        lines = string.splitlines()
        alphabet = lines[0].strip()
        word = lines[-1].strip()
        pairs = [tuple(line.split()) for line in lines[1:-1]]
        
        # We want a symmetric relation.
        relation = set()
        for a, b in pairs:
            relation.add((a, b))
            relation.add((b, a))

        return alphabet, relation, word

    @staticmethod
    def _complement(alphabet, relation):
        complement = set(product(alphabet, alphabet))
        for p in relation:
            complement.discard(p)
        return complement

    def __str__(self):
        alpha_str = 'ALPHABET: {}'.format(self.alphabet)
        word_str = 'WORD: {}'.format(self.word)
        
        ind_pairs = ',\n\t'.join([str(p) for p in self.ind_relation])
        ind_str = 'INDEPENDENCE RELATION:\n{\n\t' + ind_pairs + '\n}'
        
        dep_pairs = ',\n\t'.join([str(p) for p in self.dep_relation])
        dep_str = 'DEPENDENCE RELATION:\n{\n\t' + dep_pairs + '\n}'
   
        return '\n'.join([alpha_str, ind_str, dep_str, word_str]) 

