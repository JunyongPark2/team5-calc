import pytest

class Calc:
    # 이곳에 코드를 작성
    def getZegop(self, num:int):
        return num * num

# 테스트 케이스 작성
def test_sample():
    assert 1 == 1
    pytest.fail()

@pytest.mark.parametrize(("num", "result"), [(1, 1),(2, 4),(3,9),(4,16),(5,25),(6,36),(7,49),(8,64),(9,81),(10,100)])
def test_zegop(num, result):
    assert Calc().getZegop(num) == result