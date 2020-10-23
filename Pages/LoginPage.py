import allure
from selenium.webdriver.common.by import By

from Config.config import TestData


class LoginPage:

    USERNAME = (By.NAME, "txtUsername")
    PASSWORD = (By.NAME, "txtPassword")
    SUBMIT_BUTTON = (By.NAME, "Submit")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL)


    def enter_username(self, name):
        username = self.driver.find_element(*self.USERNAME)
        username.send_keys(name)

    def enter_password(self, pwd):
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys(pwd)

    def click_login(self):
        submit = self.driver.find_element(*self.SUBMIT_BUTTON)
        submit.click()

    def get_login_page_title(self, title):
        return self.driver.title

    def do_login(self, name, pwd):
        self.enter_username(name)
        self.enter_password(pwd)
        self.click_login()
