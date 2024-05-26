import pytest


'''
any python related configurations which are common for all test cases/ suites can be mention in conftest.py

'''

@pytest.fixture()
def setup_tc():
    print("this is setup")

    yield
    print("\n""this statement is inside tear down and will be executed after each test case")

