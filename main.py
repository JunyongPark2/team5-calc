import pytest


class Calc:
    def getGop(self,a, b):
        return a * b


    def getSumSum(a, b, c):
        return a + b + c


def test_sample():
    assert Calc().getGop(2,3) == 6

    assert 1 == 1
    pytest.fail()


def test_getSumSum():
    assert Calc.getSumSum(1, 2, 3) == 6
    assert Calc.getSumSum(0, 0, 0) == 0
    assert Calc.getSumSum(-1, 2, 1) == 2
