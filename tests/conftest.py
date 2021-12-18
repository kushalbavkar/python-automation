import pytest

# Import fixtures functions
from test_client.fixtures.test_context import test_context, web_driver, teardown

# Import glue functions
from test_client.steps.given import *
from test_client.steps.when import *
from test_client.steps.then import *

# Import test packages
from test_client.entities.environ import Environ
from test_client.exceptions.exceptions import MissingEnvironmentError
from test_client.utils.logger import logger

log = logger.get_logger(__file__)


@pytest.fixture(scope='session', autouse=True)
def init_session():
    env = Environ.Environment
    if env.value is None:
        message = f'Please create/specify test environment using [{env.value}] environment variable'
        log.error(message)
        raise MissingEnvironmentError(message)
