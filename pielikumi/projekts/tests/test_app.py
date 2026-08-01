from app import add

def test_add_1():
    assert add(2, 3) == 5

def test_add_2():
    assert add(0, 0) == 0

def test_add_3():
    assert add(-1, 1) == 0