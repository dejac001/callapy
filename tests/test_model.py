from callapy.model import DataPoint
import pytest


def test_model():
    with pytest.raises(TypeError):
        I = DataPoint()

# todo: test that get same results with all floats vs all np arrays
