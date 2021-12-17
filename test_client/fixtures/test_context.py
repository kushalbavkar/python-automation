import pytest

from test_client.entities.environ import Environ
from test_client.ui.webdriver import WebDriverManager


class TestContext:
    def __init__(self):
        self.site = None
        self.user = None
        self.project = None


@pytest.fixture(scope='function')
def test_context():
    context = TestContext()
    return context


@pytest.fixture(scope='function')
def web_driver():
    driver = WebDriverManager(Environ.Environment.value).get_driver()
    return driver


@pytest.fixture(scope='function')
def teardown(test_context, web_driver):
    yield
    del test_context
    if web_driver is not None:
        web_driver.quit()