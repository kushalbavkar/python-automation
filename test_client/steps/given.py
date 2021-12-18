import allure
from pytest_bdd import given, parsers

from test_client.actions.github import GitHubActions
from test_client.entities.sites import Sites
from test_client.fixtures.test_context import TestContext
from test_client.ui.webdriver import WebDriver


@given(parsers.parse('I am on "{site}" homepage'))
@allure.step('I am on "GitHub" homepage')
def i_am_on_github_homepage(test_context: TestContext, web_driver: WebDriver, site: str):
    test_context.site = getattr(Sites, site)
    github = GitHubActions(web_driver)
    github.navigate(test_context.site)
