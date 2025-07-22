import pytest
from convert import convert

def test_int_conversion():
    assert convert(1) == 149597870700
    assert convert(0) == 0
    assert convert(2.5) == 2.5 * 149597870700

def test_error():
    with pytest.raises(TypeError):
        convert("1")

def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)