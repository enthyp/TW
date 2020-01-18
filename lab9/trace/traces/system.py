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
  
    def _from_string(self, string):
        lines = string.splitlines()
        alphabet = lines[0].strip()
        pairs = [tuple(line.split()) for line in lines[1:]]
        self._validate(pairs, alphabet)       

        # We want a symmetric relation.
        relation = defaultdict(set)
        for a, b in pairs:
            relation[a].add(b)
            relation[b].add(a)

        return alphabet, dict(relation)

    @staticmethod
    def _validate(pairs, alphabet):
        if not alphabet:
            raise InputFormatError('Empty alphabet.')
        if not pairs:
            raise InputFormatError('Empty relation.')
   
        if not alphabet.isalpha():
            raise InputFormatError('Only letter symbols allowed.')

        correct = True
        for p in pairs:
            correct = correct and len(p) == 2
            correct = correct and p[0] in alphabet and p[1] in alphabet
        
        if not correct:
            raise InputFormatError('Pairs incorrect.')

    @staticmethod
    def _complement(alphabet, relation):
        complement = {l: set(alphabet) for l in alphabet}
        for a in relation:
            for b in relation[a]:
                complement[a].discard(b)
        return complement

    def __str__(self):
        alpha_str = 'ALPHABET: ' + self.alphabet

        ind_pairs = [str((k, v)) for k, v_set in self.ind_relation.items() for v in v_set]        
        ind_str = '\n'.join([str(p) for p in ind_pairs])
        ind_str = 'INDEPENDENCE:\n' + ind_str

        dep_pairs = [str((k, v)) for k, v_set in self.dep_relation.items() for v in v_set]                
        dep_str = '\n'.join([str(p) for p in dep_pairs])
        dep_str = 'DEPENDENCE:\n' + dep_str  

        return '\n'.join([alpha_str, ind_str, dep_str]) 

    def dump(self, filepath):
        alpha_str = self.alphabet

        ind_pairs = ['{} {}'.format(k, v) for k, v_set in self.ind_relation.items() for v in v_set]        
        ind_str = '\n'.join([str(p) for p in ind_pairs])

        with open(filepath, 'w+') as output:
            output.write('\n'.join([alpha_str, ind_str])) 

