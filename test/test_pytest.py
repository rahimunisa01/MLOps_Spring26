from src.calculator import fun1, fun2, fun3, fun4


def test_fun1():
    assert fun1(3, 2) == 5
    assert fun1(-1, 1) == 0


def test_fun2():
    assert fun2(5, 3) == -2
    assert fun2(3, 5) == 2


def test_fun3():
    assert fun3(4, 2) == 8
    assert fun3(0, 5) == 0


def test_fun4():
    # fun4 = fun1 + fun2 + fun3
    # for (4, 2): (4+2) + (4-2) + (4*2) = 6 + 2 + 8 = 16
    assert fun4(4, 2) == 12

