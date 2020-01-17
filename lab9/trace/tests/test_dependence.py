import os
import logging
import pytest
from traces import read_input, dependence_relation, MinDepGraph


target_dep1 = {
    ('a', 'a'), 
    ('a', 'b'), 
    ('a', 'c'), 
    ('b', 'a'),     
    ('b', 'b'), 
    ('b', 'd'), 
    ('c', 'a'), 
    ('c', 'c'), 
    ('c', 'd'),
    ('d', 'b'),
    ('d', 'c'),
    ('d', 'd')
}

target_dep2 = {
    ('a', 'a'),
    ('a', 'b'),
    ('a', 'c'),
    ('a', 'e'),
    ('a', 'f'),
    ('b', 'a'),
    ('b', 'b'),
    ('b', 'c'),
    ('b', 'd'),
    ('b', 'f'),
    ('c', 'a'),
    ('c', 'b'),
    ('c', 'c'),
    ('c', 'e'),
    ('d', 'b'),
    ('d', 'd'),
    ('d', 'e'),
    ('d', 'f'),
    ('e', 'a'),
    ('e', 'c'),
    ('e', 'd'),
    ('e', 'e'),
    ('e', 'f'),
    ('f', 'a'),
    ('f', 'b'),
    ('f', 'd'),
    ('f', 'e'),
    ('f', 'f')
}

inputs = ['input1.txt', 'input2.txt']
dependence_rel_targets = [target_dep1, target_dep2]


@pytest.mark.parametrize('in_file, target_dep', zip(inputs, dependence_rel_targets))
def test_dependence(in_dir, in_file, target_dep):
    input = os.path.join(in_dir, in_file)
    alphabet, independence_relation, _ = read_input(input)
    dep = dependence_relation(alphabet, independence_relation)

    assert set(dep) == target_dep


@pytest.mark.parametrize('in_file', inputs)
def test_graph(in_dir, in_file):
    input = os.path.join(in_dir, in_file)
    alphabet, independence_relation, word = read_input(input)
    graph = MinDepGraph(alphabet, independence_relation, word)   
    graph.render('graph' + in_file, show=True)

