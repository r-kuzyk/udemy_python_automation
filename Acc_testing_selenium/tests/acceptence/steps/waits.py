from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptence.locators.blog_page import BlogPageLocators

use_step_matcher("re")

@given("I wait for the post to load")
def step_implementation(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_all_elements_located(BlogPageLocators.POST)
    )
