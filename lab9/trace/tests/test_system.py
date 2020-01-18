import os
import logging 
import pytest
from itertools import product
from traces import System


target_dep1 = {
    'a': {'a', 'b', 'c'}, 
    'b': {'a', 'b', 'd'},
    'c': {'a', 'c', 'd'},
    'd': {'b', 'c', 'd'}     
}

target_dep2 = {
    'a': {'a', 'b', 'c', 'e', 'f'},
    'b': {'a', 'b', 'c', 'd', 'f'},
    'c': {'a', 'b', 'c', 'e'},
    'd': {'b', 'd', 'e', 'f'},
    'e': {'a', 'c', 'd', 'e', 'f'},
    'f': {'a', 'b', 'd', 'e', 'f'}
}

systems = ['system1.txt', 'system2.txt']
dep_rel_targets = [target_dep1, target_dep2]
params = zip(systems, dep_rel_targets)


@pytest.mark.parametrize('in_file, target_dep', params)
def test_system(in_dir, in_file, target_dep):
    input_path = os.path.join(in_dir, in_file)
    system = System(input_path, from_ind=True)
    assert system.dep_relation == target_dep
    logging.info(str(system))

