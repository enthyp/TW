from collections import defaultdict, deque
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
    
        for i in range(len(word) - 1, -1, -1):
            cur_l = word[i]
            new_node = Node(cur_l, i) 
            self.nodes[i] = new_node

            visited = set()   
            for j in range(i + 1, len(word)):
                if self.nodes[j] in visited or word[j] not in dep_rel[cur_l]:
                    continue

                # Letter not visited and dependent - DFS from it.
                new_node.conn(self.nodes[j])
                self._dfs(self.nodes[j], visited)
 
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

    def _dfs(self, node, visited):
        visited.add(node)
        for n in node.neighbors:
            if n not in visited:
                self._dfs(n, visited)

    def fnf(self):
        # BFS and merge layers to form all FNF blocks.
        roots = set(self.nodes)
        for n in self.nodes:
            roots -= n.neighbors

        q = deque(roots)        
        layers = {r: 1 for r in roots}
        no_layers = 1
        
        while q:
            cur_node = q.popleft()
            layer = layers[cur_node]            
            no_layers = max(no_layers, layer)

            for node in cur_node.neighbors:
                if node not in layers or layers[node] < layer + 1:
                    layers[node] = layer + 1
                    q.append(node)

        blocks = [[] for _ in range(no_layers)]
        for node, layer in layers.items():
            blocks[layer - 1].append(node.label)
     
        blocks = ['(' + ''.join(sorted(b)) + ')' for b in blocks if b]
        return ''.join(blocks)

