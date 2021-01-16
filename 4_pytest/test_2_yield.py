import pytest


@pytest.yield_fixture()
def setup():
    print(" Once vefore every method")
    yield
    print(" Once after every method")

def testMethod1(setup):
    print("This is test method 1")

def testMethod2(setup):
    print("This is test method 2")

def testMethod3(setup):
    print("This is test method 3")

def testMethod4(setup):
    print("This is test method 4")

# pytest -v -s test_2_yield.py