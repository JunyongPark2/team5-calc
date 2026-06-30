import pytest


class Calc:
    # 이곳에 코드를 작성
    def getSum(self, a, b):
        return a + b

    pass


# 테스트 케이스 작성
def test_sample():
    assert Calc().getSum(3, 5) == 8

    assert 1 == 1
    pytest.fail()