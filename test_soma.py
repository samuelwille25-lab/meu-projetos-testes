from soma import soma

def test_soma_1():
    assert soma(1, 1) == 2

def test_soma_2():
    assert soma(2, 3) == 5

def test_soma_3():
    assert soma(-1, -1) == -2

def test_soma_4():
    assert soma(5, -3) == 2

def test_soma_5():
    assert soma(0, 10) == 10
