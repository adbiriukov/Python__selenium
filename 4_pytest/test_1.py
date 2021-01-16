import pytest


@pytest.fixture()
def setup():
    print("Once before every method")

def testmethod1(setup):
    print("This is method1")

def testmethod2(setup):
    print("This is method2")


# pytest -v -s test_1.py