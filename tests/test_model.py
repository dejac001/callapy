from callapy.model import Model
import pytest


def test_model():
    with pytest.raises(Exception):
        I = Model()

# todo: test that get same results with all floats vs all np arrays
