from itertools import product 


def dependence_relation(alphabet, independence_pairs):
    independence_pairs = set(independence_pairs)
    full_relation = list(product(alphabet, alphabet))

    return [r for r in full_relation if r not in independence_pairs]
