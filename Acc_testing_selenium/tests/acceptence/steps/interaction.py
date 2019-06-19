from behave import *
from selenium import webdriver

from tests.acceptence.page_model.base_model import BasePage
from tests.acceptence.page_model.new_post_page import NewPostPage

use_step_matcher("re")


@when('I click on the link with id "(.*)"')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation
    matching_link = [l for l in links if l.text == link_text]

    if len(matching_link) > 0:
        matching_link[0].click()
    else:
        raise RuntimeError()


@when('I enter "(.*)" int the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keyes(content)


@when('I press the submit button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()