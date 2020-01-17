import os
import logging
import pytest
from traces import MinDependenceGraph, System

inputs = [
    ('system1.txt', 'baadcb'),
    ('system2.txt', 'acdcfbbe')
]

@pytest.mark.skip()
@pytest.mark.parametrize('in_file, word', inputs)
def test_graph_render(in_dir, in_file, word):
    input_path = os.path.join(in_dir, in_file)
    system = System(input_path)
    graph = MinDependenceGraph(word, system)   
    graph.render('graph' + in_file, show=True)

@pytest.mark.parametrize('in_file, word', inputs)
def test_graph_fnf(in_dir, in_file, word):
    input_path = os.path.join(in_dir, in_file)
    system = System(input_path)
    graph = MinDependenceGraph(word, system)   
    logging.info(graph.fnf())

