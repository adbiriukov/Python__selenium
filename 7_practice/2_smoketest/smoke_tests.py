import unittest
from amazon_homePage import HomePageTest
from amazon_search import SearchDDT


# get all tests from HomePageTest and SearchDDT class
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchDDT)

# create a test suite combining HomePageTest and SearchDDT
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
