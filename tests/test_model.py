from callapy.model import DataPoint
import pytest


def test_model():
    with pytest.raises(TypeError):
        I = DataPoint()
