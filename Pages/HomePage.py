from selenium.webdriver.common.by import By

from Config.config import TestData


class HomePage:

    ACCOUNT = (By.ID, "welcome")
    MARKET_LINK = (By.ID, "MP_link")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    # Methods #
    # ==========#
    def click_marketplace(self):
        marketplace = self.driver.find_element(*self.MARKET_LINK)
        marketplace.click()

    def get_home_page_title(self, title):
        return self.driver.title

    def get_account_name(self):
        acc_name = self.driver.find_element(*self.ACCOUNT)
        return acc_name.text
