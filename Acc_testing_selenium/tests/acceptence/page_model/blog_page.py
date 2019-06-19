from tests.acceptence.locators.blog_page import BlogPAgeLocators
from tests.acceptence.page_model.base_model import BasePage


class BlogPage(BasePage):

    @property
    def urls(self):
        return super(BasePage, self).url + '/blog'


    @property
    def post_section(self):
        return self.driver.find_elment(*BlogPAgeLocators.POST_SECTION)

    @property
    def posts(self):
        return self.driver.find_elment(*BlogPAgeLocators.POST)

    @property
    def post_select(self):
        return self.driver.find_elment(*BlogPAgeLocators.POST_SECTION)

    @property
    def add_post_link(self):
        return self.driver.find_elment(*BlogPAgeLocators.ADD_POST_LINK)

