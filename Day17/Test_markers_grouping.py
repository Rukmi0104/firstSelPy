import pytest


######### executing setup /teardownn at class level before executing any test case ####

class Test_TS:
    def test_01(self, setup_tc):
        print("this is first test case in Test_TS")

    def test_02(self, setup_tc):
        print("this is 2nd test case in Test_TS")

    def test_03(self, setup_tc):
        print("this is third test case in Test_TS")


######### executing setup /teardownn at class level before executing any test case ####

class Test_TS2:
    def test_01(self, setup_at_cl):
        print("this is first test case in Test_TS2")

    @pytest.mark.regression
    def test_02(self, setup_at_cl):
        print("this is 2nd test case in Test_TS2")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_03(self, setup_at_cl):
        print("this is third test case in Test_TS2")


class Test_TS3:
    @pytest.mark.sanity
    @pytest.mark.xfail()
    def test_01(self, setup_at_md):
        print("this is first test case in Test_TS3")
        assert False        # this will indicate that test case is returning some failure.
                            # But with this we will get failure msg on console with red mark.
                            # If we dont want to show this flag to customer we can mark tc as Xfail.
                            #  We can ignore this failure

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.skip
    def test_02(self, setup_at_md):
        print("this is 2nd test case in Test_TS3")

    @pytest.mark.regression
    @pytest.mark.skipif(True, reason="skipped the test case because the condition is true")
    def test_03(self, setup_at_md):
        print("this is third test case in Test_TS3")


@pytest.mark.sanity
class Test_TS4:
    @pytest.mark.regression
    def test_04(self, setup_at_md):
        print("this is 4th test case in Test_TS4")


