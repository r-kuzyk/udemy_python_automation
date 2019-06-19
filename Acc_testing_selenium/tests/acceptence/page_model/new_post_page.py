from selenium.webdriver.common.by import By

from tests.acceptence.locators.new_post_page import NewPostPageLocators
from tests.acceptence.page_model.base_model import BasePage


class NewPostPage(BasePage):

    @property
    def urls(self):
        return super(NewPostPage, self).url + '/post'

    @property
    def form(self):
        return self.driver.find_element(*NewPostPageLocators.NEW_POST_FORM)
    
    @property
    def submit_button(self):
        return self.driver.find_element(*NewPostPageLocators.SUBMIT_BUTTON)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)

