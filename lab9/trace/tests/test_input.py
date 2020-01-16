import os
import logging
from traces.input import read_input


def test_input(in_dir):
    input1 = os.path.join(in_dir, 'input1.txt')
    read_input(input1)
