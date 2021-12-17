from test_client.ui.webdriver import WebDriver
from test_client.ui.base import Base


class GitHubActions(Base):
    def __init__(self, driver: WebDriver):
        super(GitHubActions, self).__init__(driver)

