import pytest


class Calc:
    # 이곳에 코드를 작성
    def getSum(self, a, b):
        return a + b

    pass


# 테스트 케이스 작성
def test_sample():
    assert 1 == 1
    pytest.fail()


def test_sample_getSum():
    calc = Calc()
    # 3과 5를 더했을 때 결과가 8이 되는지 검증
    assert calc.getSum(3, 5) == 8