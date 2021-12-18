from typing import Tuple

from test_client.ui.base import Base
from test_client.ui import By, WebDriver, Keys


class GitHubLocators:
    SEARCH_GITHUB = (By.XPATH, '//input[@placeholder="Search GitHub"]')
    NAV_USERS = (By.XPATH, '//nav/a[text()="Users"]')
    NAV_USERS_SELECTED = (By.XPATH, '//a[contains(@class, "selected") and text()="Users"]')
    USER = (By.XPATH, '//a[contains(text(),"{}")]')
    SEARCH_PROJECT = (By.ID, 'your-repos-filter')
    PROJECT = (By.XPATH, '//a[contains(text(),"{}")]')
    AUTHOR = (By.XPATH, '//h1/descendant::a[@rel="author"]')
    REPOSITORY = (By.XPATH, '//h1/strong/a')

    @classmethod
    def format(cls, locator: Tuple[By, str], *args: str):
        how, value = locator
        return how, value.format(*args)


class GitHubActions(Base):
    def __init__(self, driver: WebDriver):
        super(GitHubActions, self).__init__(driver)

    def search(self, text: str):
        self.send_keys(text, GitHubLocators.SEARCH_GITHUB)
        self.send_keys(Keys.ENTER, GitHubLocators.SEARCH_GITHUB)

    def select_user(self, user: str):
        self.click(GitHubLocators.NAV_USERS)
        self.wait(GitHubLocators.NAV_USERS_SELECTED, 10)
        self.click(GitHubLocators.format(GitHubLocators.USER, user))

    def search_project(self, project: str):
        self.send_keys(project, GitHubLocators.SEARCH_PROJECT)

    def select_project(self, project):
        self.click(GitHubLocators.format(GitHubLocators.PROJECT, project))

    def get_project_details(self):
        author = self.find_element(GitHubLocators.AUTHOR).text
        project = self.find_element(GitHubLocators.REPOSITORY).text

        return author, project
