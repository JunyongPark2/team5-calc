import pytest

class Calc:
    # 이곳에 코드를 작성
    def getSum(self, a, b):
        return a + b

    def getDivide(self, a, b):
        return a / b

    def getGop(self,a, b):
        return a * b

    def getMinus(self, a, b):
        return a - b

    def getZegop(self, num:int):
        return num * num

    def getGop(self,a, b):
        return a * b

    def getSumSum(a, b, c):
        return a + b + c


# 테스트 케이스 작성
def test_sample():
    assert Calc().getGop(2,3) == 6

    assert 1 == 1
    pytest.fail()
def test_sum():
    assert Calc().getSum(3,5) == 8


def test_getSumSum():
    assert Calc.getSumSum(1, 2, 3) == 6
    assert Calc.getSumSum(0, 0, 0) == 0
    assert Calc.getSumSum(-1, 2, 1) == 2


def test_divide():
    calc = Calc()
    assert calc.getDivide(6, 2) == 3


def test_minus():
    assert Calc().getMinus(5,2) == 3


@pytest.mark.parametrize(("num", "result"), [(1, 1),(2, 4),(3,9),(4,16),(5,25),(6,36),(7,49),(8,64),(9,81),(10,100)])
def test_zegop(num, result):
    assert Calc().getZegop(num) == result
