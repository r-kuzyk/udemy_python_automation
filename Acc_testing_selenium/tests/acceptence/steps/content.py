from behave import *

from tests.acceptence.page_model.base_model import BasePage
from tests.acceptence.page_model.blog_page import BlogPage

use_step_matcher("re")


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title_tag.text == content


@then('I can see there is a posts section on the page')
def step_impl(context, content):
    page = BlogPage(context.driver)

    assert page.post_section.is_displayed()


@then('I can see there is a post with the title "(.*)" in the post section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.ext == title]

    assert len(posts_with_title) > 0
    assert all([post.is_displayed() for post in posts_with_title])