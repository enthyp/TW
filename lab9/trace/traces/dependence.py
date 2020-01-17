from collections import defaultdict
from graphviz import Digraph


class Node:
    def __init__(self, letter, identifier):
        self.letter = letter
        self.identifier = identifier
        self.neighbors = set()

    @property
    def id(self):   
         return '{}{}'.format(self.label, self.identifier) 

    @property
    def label(self):
        return self.letter

    def conn(self, other):
        self.neighbors.add(other)


class MinDependenceGraph:
    def __init__(self, word, system, hasse=False):
        self.nodes = []
        if hasse:
            self._prepare_hasse(word, system)
        else:
            self._prepare_mindep(word, system)

        self.visualized = False
        self.viz_graph = Digraph('dep_graph', node_attr={'style': 'filled'})
        self.viz_graph.attr(rankdir='LR')

    def _prepare_hasse(self, word, system):
        dep_rel = system.dep_relation
        min_set = set()
        
        for i, l in enumerate(word[::-1]):
            new_node = Node(l, i) 
            
            tb_removed = set() 
            for node in min_set:
                if node.label in dep_rel[l]:
                    new_node.conn(node)
                    tb_removed.add(node)
           
            min_set -= tb_removed           
            self.nodes.append(new_node)
            min_set.add(new_node)

    def _prepare_mindep(self, word, system):
        self.nodes = [None] * len(word)
        dep_rel = system.dep_relation
        min_set = set()
 
        def dfs(node, visited):
            visited.add(node.identifier)
            for n in node.neighbors:
                if n.identifier not in visited:
                    dfs(n, visited)
       
        for i in range(len(word) - 1, -1, -1):
            cur_l = word[i]
            new_node = Node(cur_l, i) 
            self.nodes[i] = new_node

            visited = set()   
            for j in range(i + 1, len(word)):
                if j in visited or word[j] not in dep_rel[cur_l]:
                    continue

                # Letter not visited and dependent - DFS from it.
                new_node.conn(self.nodes[j])
                dfs(self.nodes[j], visited)
 
    def _visualize(self):
        for node in self.nodes:
            self.viz_graph.node(node.id, label=node.label)
            for neighbor in node.neighbors:
                self.viz_graph.edge(node.id, neighbor.id)

        self.visualized = True

    def render(self, filename, show=True):
        if not self.visualized:
            self._visualize()
        self.viz_graph.render(filename, view=show)

    def fnf(self):
        # Topo sort first to find the first block of FNF.
        

        # BFS and merge layers to form all FNF blocks.
        pass

