import os
import logging
import pytest
from traces import System, trace


params = [
    ('system1.txt', 'baadbc'),
    ('system2.txt', 'acdcfbbe')
]

@pytest.mark.parametrize('in_file, execution', params)
def test_trace(in_dir, in_file, execution):
    input_path = os.path.join(in_dir, in_file)
    system = System(input_path)
    logging.info(trace(execution, system))

