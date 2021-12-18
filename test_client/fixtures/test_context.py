import pytest

from test_client.entities.environ import Environ
from test_client.ui.webdriver import WebDriverManager
from test_client.utils.logger import logger

log = logger.get_logger(__file__)


class TestContext:
    def __init__(self):
        self.site = None
        self.user = None
        self.project = None


@pytest.fixture(scope='function')
def test_context():
    context = TestContext()
    log.info(f'test_context object created: {id(context)}')
    return context


@pytest.fixture(scope='function')
def web_driver():
    driver = WebDriverManager(Environ.Environment.value).get_driver()
    driver.maximize_window()
    log.info(f'web_driver object created: {id(driver)}')
    return driver


@pytest.fixture(scope='function', autouse=True)
def teardown(test_context, web_driver):
    yield
    log.info(f'test_context object destroyed: {id(test_context)}')
    log.info(f'web_driver object destroyed: {id(web_driver)}')
    if web_driver is not None:
        web_driver.quit()

    del test_context, web_driver
