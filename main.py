import pytest


class Calc:
    # 이곳에 코드를 작성
    def getSumSum(a, b, c):
        return a + b + c


# 테스트 케이스 작성
def test_getSumSum():
    assert Calc.getSumSum(1, 2, 3) == 6
    assert Calc.getSumSum(0, 0, 0) == 0
    assert Calc.getSumSum(-1, 2, 1) == 2
