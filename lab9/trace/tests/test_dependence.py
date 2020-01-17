import os
import logging
import pytest
from traces import read_input, dependence_relation, MinDepGraph


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

