import pytest


@pytest.fixture()
def setup_tc():
    print("this is setup at test case level")
    yield True
    print("\n""this statement is inside tear down and will be executed after each test case")