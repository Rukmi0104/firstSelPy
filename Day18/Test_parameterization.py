import pytest


class Test_TS_P:
    @pytest.mark.parametrize("a", [1, 2, 3, 4, 5])  # in this case for parameter a different inputs are passed.
    # test case will run 5 times for each input value of a
    def test_tc01(self, a):
        print("this is test case01 from Test_TS_P", a)

    @pytest.mark.parametrize("b, c, d", [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    # in this case for parameter a different inputs are passed.
    # test case will run 3 times for each input value of b, c, d
    def test_tc02(self, b, c, d):
        print("this is test case02 from Test_TS_P", b, c, d)
