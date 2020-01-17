import os
import logging
import pytest
from traces import System, fnf


params = [
    ('system1.txt', 'baadcb', '(b)(ad)(a)(bc)'),
    ('system2.txt', 'acdcfbbe', '(ad)(cf)(c)(be)(b)')
]

@pytest.mark.parametrize('in_file, word, target_form', params)
def test_foata(in_dir, in_file, word, target_form):
    input_path = os.path.join(in_dir, in_file)
    system = System(input_path)

    assert fnf(word, system) == target_form

