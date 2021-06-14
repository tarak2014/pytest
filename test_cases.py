from basicmath import util

def test_add_num():
    """Test is to Addition of two numbers, and return the output value"""
    assert util.add_num(3,4) == 7

def test_sub_num():
    """Test is to Substraction of two numbers, and return the output value"""
    assert util.sub_num(3,4) == -1

def test_mul_num():
    """Test is to Multiplication of two numbers, and return the output value"""
    assert util.mul_num(3,4) == 12

def test_div_num():
    """Test is to Division of two numbers, and return the output value"""
    assert util.div_num(3,4) == 0.75