import unittest

import allure
from selenium import webdriver

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener

from Tests.conftest import ScreenshotListener


@allure.epic("OrangeHRM web Application")
@allure.feature("OrangeHRM Home Page test")
@allure.story("Login Page test with valid data testcases")
class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        edriver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        cls.driver = EventFiringWebDriver(edriver, ScreenshotListener())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    @allure.step("Home Page title check")
    @allure.severity(allure.severity_level.NORMAL)
    def test_h1_home_page_title_check(self):
        loginpage = LoginPage(self.driver)
        loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        homepage = HomePage(self.driver)
        title = homepage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    @allure.step("Account name check")
    @allure.severity(allure.severity_level.NORMAL)
    def test_h2_account_name_check(self):
        homepage = HomePage(self.driver)
        account = homepage.get_account_name()
        assert account == TestData.ACCOUNT_NAME

    @allure.step("Marketplace link check")
    @allure.severity(allure.severity_level.NORMAL)
    def test_h3_marketplace_link_check(self):
        homepage = HomePage(self.driver)
        homepage.click_marketplace()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
