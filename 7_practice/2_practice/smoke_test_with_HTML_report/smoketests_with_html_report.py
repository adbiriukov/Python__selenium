import unittest
import HTMLTestRunner
import os
from amazon_homePage import HomePageTest
from amazon_search import SearchDDT

# get the directory path to output report file
result_dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchDDT)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# open the report file
outfile = open(result_dir + '\SmokeTestReport.html', 'w')

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       title='Test Report',
                                       description='Smoke Tests')

# run the suite using HTMLTestRunner
runner.run(smoke_tests)
