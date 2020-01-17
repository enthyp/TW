import logging
from itertools import product 
from collections import defaultdict
from graphviz import Graph


def dependence_relation(alphabet, independence_pairs):
    independence_pairs = set(independence_pairs)
    full_relation = list(product(alphabet, alphabet))

    return [r for r in full_relation if r not in independence_pairs]


class MinDepGraph:
    def __init__(self, alphabet, independence_relation, word):
        self.viz_graph = Graph('dep_graph', node_attr={'style': 'filled'})
        self.viz_graph.attr(
            layout='neato',
            overlap='prism',
            overlap_scaling='10'
        )
        self._prepare(alphabet, independence_relation, word)

    def _prepare(self, alphabet, independence_relation, word):
        dep_map = {l: set(alphabet) for l in alphabet}
        for a, b in independence_relation:
            dep_map[a].discard(b)
            dep_map[b].discard(a)
        
        min_set = defaultdict(set)
        l_count = defaultdict(int)
        
        for l in word[::-1]:
            l_count[l] += 1
            node_name = '{}{}'.format(l, l_count[l])
            self.viz_graph.node(node_name)

            deps = set()        
            for dep, nums in min_set.items():
                if dep in dep_map[l]:
                    logging.debug('from: ' + node_name) 
                    for n in nums:
                        d_name = '{}{}'.format(dep, n)
                        logging.debug('to: ' + d_name)
                        self.viz_graph.edge(node_name, d_name)
                    deps.add(dep)
            for d in deps:
                del min_set[d]            

            min_set[l].add(l_count[l])

    def render(self, filename, show=True):
        self.viz_graph.render(filename, view=show)
 
