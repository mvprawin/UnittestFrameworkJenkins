import os
import unittest

import xmlrunner

from Tests.LoginPageTest import LoginPageTest
from Tests.HomePagTest import HomePageTest

# get the directory path to output report file
current_directory = os.getcwd()

# Create a TestSuite comprising the two test cases
test_suite = unittest.TestSuite()

# Add the test cases to the Test Suite
test_suite.addTests([
    unittest.TestLoader().loadTestsFromTestCase(LoginPageTest),
    unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
])

# open the report file
outfile = open(current_directory + "/Reports/XMLReport/TestSummary", "w")

# configure HTMLTestRunner options
runner = xmlrunner.XMLTestRunner(output=outfile)

# run the suite using HTMLTestRunner
runner.run(test_suite)
