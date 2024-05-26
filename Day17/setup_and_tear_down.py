import pytest


#
#
# ######### executing setup at test case level
@pytest.fixture()
def setup_tc():
    print("this is setup")

    yield
    print("\n""this statement is inside tear down and will be executed after each test case")

# class Test_TS2:
#     def test_01(self, setup_tc):
#         print("this is first test case")
#
#     def test_02(self, setup_tc):
#         print("this is 2nd test case")
#
#     def test_03(self, setup_tc):
#         print("this is third test case")


######### executing setup /teardownn at class level before executing any test case ####

class Test_TS2:
    def test_01(self, setup_at_cl):
        print("this is first test case in Test_TS2")

    def test_02(self, setup_at_cl):
        print("this is 2nd test case in Test_TS2")

    def test_03(self, setup_at_cl):
        print("this is third test case in Test_TS2")


######### executing setup /tear downn at module level before executing any test case

class Test_TS3:
    def test_01(self, setup_at_md):
        print("this is first test case in Test_TS3")

    def test_02(self, setup_at_md):
        print("this is 2nd test case in Test_TS3")

    def test_03(self, setup_at_md):
        print("this is third test case in Test_TS3")


class Test_TS4:
    def test_04(self, setup_at_md):
        print("this is 4th test case in Test_TS4")
