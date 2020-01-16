import os
import pytest


@pytest.fixture
def in_dir():
    root_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(root_dir, 'in')

