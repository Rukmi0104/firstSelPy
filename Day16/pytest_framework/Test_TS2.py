import pytest


# use fixture from conftest.py file

class Test_cl2:

    def test_01(self, setup_tc):
        print("this is first test case")

    def test_02(self, setup_tc):
        print("this is 2nd test case")

    def test_03(self, setup_tc):
        print("this is third test case")



