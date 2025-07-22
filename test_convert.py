from convert import convert

def test_conversion():
    assert convert(1) == 149597870700
    assert convert(0) == 0
    assert convert(2.5) == 2.5 * 149597870700

