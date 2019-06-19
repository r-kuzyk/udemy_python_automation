from tests.acceptence.locators.home_page import HomePageLocators
from tests.acceptence.page_model.base_model import BasePage


class HomePage(BasePage):

    @property
    def urls(self):
        return super(HomePage, self).url + '/'


    @property
    def blog_link(self):
        return self.driver.find_elment(*HomePageLocators.NAVIGATION_LINK)