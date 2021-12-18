from pytest_bdd import when, parsers

from test_client.fixtures.test_context import TestContext
from test_client.ui.webdriver import WebDriver
from test_client.actions.github import GitHubActions


@when(parsers.parse('I search for "{user}" user'))
def i_search_for_user(test_context: TestContext, web_driver: WebDriver, user):
    test_context.user = user
    github = GitHubActions(web_driver)
    github.search(user)
    github.select_user(user)


@when(parsers.parse('I select "{project}" project'))
def i_select_project(test_context: TestContext, web_driver: WebDriver, project):
    test_context.project = project
    github = GitHubActions(web_driver)
    github.search_project(project)
    github.select_project(project)

