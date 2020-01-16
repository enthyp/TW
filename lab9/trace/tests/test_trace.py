import os
import logging
import pytest
from traces import read_input, trace


params = [('input1.txt', 'baadbc')]

@pytest.mark.parametrize('in_file, target_trace', params)
def test_trace(in_dir, in_file, target_trace):
    input = os.path.join(in_dir, in_file)
    alphabet, independence_relation, word = read_input(input)

    assert trace(word, independence_relation) == target_trace

