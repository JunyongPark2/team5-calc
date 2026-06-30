import pytest


class Calc:
    # 이곳에 코드를 작성

    def getGop(self,a, b):
        return a * b

    def getMinus(self, a, b):
        return a - b

# 테스트 케이스 작성
def test_sample():
    assert Calc().getGop(2,3) == 6

    assert 1 == 1
    pytest.fail()

def test_minus():
    assert Calc().getMinus(5,2) == 3
