# py.test test.py    -- Run tests in module
# py.test somepath    -- Run all test below somepath
# pytest test_module.py::test_method -- only run test_method in test_module
# -s to print statement
# -v verbose
#
# 1
# Run all tests in a module/file
# pytest -v -s test.py
#
# 2
# Run all tests in path
# pytest -v -s C:\Tests
#
# 3
# Run specific test method from a module
# pytest -v -s test.py::test_login
