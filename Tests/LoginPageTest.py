
import unittest

import allure
from selenium import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.conftest import ScreenshotListener


@allure.epic("OrangeHRM web Application")
@allure.feature("OrangeHRM Login Page test")
@allure.story("Login Page test with valid data testcases")
class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        edriver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        cls.driver = EventFiringWebDriver(edriver, ScreenshotListener())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    @allure.step("Login Page title check")
    def test_l1_login_page_title_check(self):
        loginpage = LoginPage(self.driver)
        title = loginpage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    @allure.step("Login with valid data")
    def test_l2_login_with_valid_data(self):
        loginpage = LoginPage(self.driver)
        loginpage.enter_username("Admin")
        loginpage.enter_password("admin123")
        loginpage.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()





