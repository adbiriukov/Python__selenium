import unittest

from package_1.TC_loginTest import LoginTest
from package_1.TC_SignUp_test import SignupTest
from  package_2.TC_paymentTest import PaymentTest
from package_2.TC_PaymentReturnsTest import PaymentReturnsTest

# Get all tests from LoginTest, SignupTest, PaymentTest and PaymentReturnsTest
# With this command we getting all test methods from the case
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating test suites
SanityTestSuite = unittest.TestSuite([tc1, tc2])
functionalTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

# unittest.TextTestRunner().run(SanityTestSuite)
# unittest.TextTestRunner().run(functionalTestSuite)
# execute all 9 test cases
unittest.TextTestRunner().run(masterTestSuite)