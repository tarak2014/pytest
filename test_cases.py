from basicmath import util

def test_add_num():
    assert util.add_num(3,4) == 7

def test_sub_num():
    assert util.sub_num(3,4) == -1

def test_mul_num():
    assert util.mul_num(3,4) == 12

def test_div_num():
    assert util.div_num(3,4) == 0.75