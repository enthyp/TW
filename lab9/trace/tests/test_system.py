import os
import logging 
import pytest
from itertools import product
from traces import System


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
dep_rel_targets = [target_dep1, target_dep2]
params = zip(inputs, dep_rel_targets)

@pytest.mark.parametrize('in_file, target_dep', params)
def test_system(in_dir, in_file, target_dep):
    input_path = os.path.join(in_dir, in_file)
    system = System(input_path, from_ind=False)
    assert system.ind_relation == target_dep

