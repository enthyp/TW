from collections import defaultdict


class InputFormatError(Exception):
    pass

class System:
    def __init__(self, source, from_ind=True):
        try:
            alphabet, relation = self._from_file(source)
        except FileNotFoundError:
            try:
                alphabet, relation = self._from_string(source)
            except:
                raise InputFormatError

        self.alphabet = alphabet
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
        pairs = [tuple(line.split()) for line in lines[1:]]
        
        # We want a symmetric relation.
        relation = defaultdict(set)
        for a, b in pairs:
            relation[a].add(b)
            relation[b].add(a)

        return alphabet, relation

    @staticmethod
    def _complement(alphabet, relation):
        complement = {l: set(alphabet) for l in alphabet}
        for a in relation:
            for b in relation[a]:
                complement[a].discard(b)
        return complement

    def __str__(self):
        alpha_str = 'ALPHABET: {}'.format(self.alphabet)
        
        ind_pairs = ',\n\t'.join([str(p) for p in self.ind_relation])
        ind_str = 'INDEPENDENCE RELATION:\n{\n\t' + ind_pairs + '\n}'
        
        dep_pairs = ',\n\t'.join([str(p) for p in self.dep_relation])
        dep_str = 'DEPENDENCE RELATION:\n{\n\t' + dep_pairs + '\n}'
   
        return '\n'.join([alpha_str, ind_str, dep_str]) 

