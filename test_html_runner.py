import os
import unittest

from HtmlTestRunner import HTMLTestRunner

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
outfile = open(current_directory + "/Reports/HTMLReport/SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
