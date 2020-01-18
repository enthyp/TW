import os
import pytest


@pytest.fixture
def test_dir():
    return os.path.dirname(os.path.realpath(__file__))

@pytest.fixture
def in_dir(test_dir):
    return os.path.join(test_dir, 'in')

