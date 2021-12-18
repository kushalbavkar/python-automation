from pytest_bdd import then
from test_client.actions.github import GitHubActions
from test_client.ui.webdriver import WebDriver
from test_client.fixtures.test_context import TestContext


@then('I should see the repository page')
def i_should_see_the_repository_page(test_context: TestContext, web_driver: WebDriver):
    github = GitHubActions(web_driver)
    author, project = github.get_project_details()

    assert test_context.user == author, 'Invalid User'
    assert test_context.project == project, 'Invalid Project'
