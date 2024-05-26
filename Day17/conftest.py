import pytest


@pytest.fixture()
def setup_tc():
    print("this is setup at test case level")
    yield True
    print("\n""this statement is inside tear down and will be executed after each test case")


@pytest.fixture(scope="class")
def setup_at_cl():
    print("this is setup executed at class level")

    yield
    print("\n""this statement is inside tear down and will be executed at class level")


@pytest.fixture(scope="module")
def setup_at_md():
    print("this is setup executed at module level")

    yield
    print("\n""this statement is inside tear down and will be executed at module level")


def pytest_configure(config):
    config.addinivalue_line("markers", "sanity: this is tag name for sanity test cases")
    config.addinivalue_line("markers", "regression: this is tag name for regression test cases")

