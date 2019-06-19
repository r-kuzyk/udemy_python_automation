from tests.acceptence.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return "http://127.0.0.1:5000"

    @property
    def title(self):
        return self.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        self.driver.find_elements(*BasePageLocators.NAV_LINKS)
