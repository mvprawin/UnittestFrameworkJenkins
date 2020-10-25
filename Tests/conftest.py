from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        screenshot_name = "exception.png"
        driver.get_screenshot_as_file(screenshot_name)
        #driver.save_screenshot(screenshot_name)
        print("Screenshot saved as '%s'" % screenshot_name)
