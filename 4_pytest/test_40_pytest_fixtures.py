import pytest

@pytest.yield_fixture()
def setup():
    print(" Once before every method")
    yield
    print(" Once after every method")

def testMethod1(setup):
    print('test 11111111111111')

def testMethod2(setup):
    print('test 22222222222222222')