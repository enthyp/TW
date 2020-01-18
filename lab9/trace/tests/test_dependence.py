import os
import logging
import pytest
from traces import MinDependenceGraph, System

inputs = [
    ('system1.txt', 'baadcb', True),
    ('system2.txt', 'acdcfbbe', True),
    ('system3.txt', 'acebdac', False)
]


def get_graph(in_dir, in_file, word, from_ind):
    input_path = os.path.join(in_dir, in_file)
    system = System(input_path, from_ind)
    graph = MinDependenceGraph(word, system)   
    return graph

@pytest.mark.parametrize('in_file, word, from_ind', inputs)
def test_graph_render(test_dir, in_dir, in_file, word, from_ind):
    graph = get_graph(in_dir, in_file, word, from_ind)
    path = os.path.join(test_dir, 'out', 'graph_{}'.format(word))
    graph.render(path, show=True)


@pytest.mark.parametrize('in_file, word, from_ind', inputs)
def test_graph_fnf(in_dir, in_file, word, from_ind):
    graph = get_graph(in_dir, in_file, word, from_ind)
    logging.info(graph.fnf())

