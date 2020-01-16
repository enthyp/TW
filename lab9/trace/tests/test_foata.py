import os
import logging
import pytest
from traces import read_input, fnf


params = [
    ('input1.txt', '(b)(ad)(a)(bc)'),
    ('input2.txt', '(ad)(cf)(c)(be)(b)')
]

@pytest.mark.parametrize('in_file, target_form', params)
def test_foata(in_dir, in_file, target_form):
    input = os.path.join(in_dir, in_file)
    alphabet, independence_relation, word = read_input(input)

    assert fnf(word, alphabet, independence_relation) == target_form

