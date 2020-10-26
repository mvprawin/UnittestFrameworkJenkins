import time

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class ScreenshotListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)

    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)

    def on_exception(self, exception, driver):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        print(timestr)
        screenshot_name = "Screenshots/exception_"+timestr+".png"
        driver.get_screenshot_as_file(screenshot_name)
        print("Screenshot saved as '%s'" % screenshot_name)
