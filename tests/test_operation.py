from src.math_operations import add,sub,mul

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_sub():
    assert sub(5,3) ==2
    assert sub(9,3) ==6
    assert sub(5,2) ==3
    assert sub(-4,1)==-5
def test_mul():
    assert mul(5,4)==20
    assert mul(3,5)==15
