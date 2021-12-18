from collections import namedtuple
from pathlib import Path

from iniconfig import IniConfig

from test_client.exceptions.exceptions import UnsupportedEnvironmentError
from test_client.utils.logger import logger

log = logger.get_logger(__file__)


class Environments:
    DEV = 'dev'
    PROD = 'prod'


class Config:
    _fields = ('driver',)
    _dev = namedtuple('_dev', _fields, defaults=(None,) * len(_fields))
    _prod = namedtuple('_prod', _fields, defaults=(None,) * len(_fields))
    _config_file = Path(__file__).parent.parent.parent.joinpath('config.ini').as_posix()

    @classmethod
    def properties(cls, env: str):
        config = IniConfig(cls._config_file)
        environments = (Environments.DEV, Environments.PROD)

        if env not in environments:
            message = f'[{env}] is not supported. Supported environments {environments}'
            log.error(message)
            raise UnsupportedEnvironmentError(message)

        if env == Environments.DEV:
            return cls._dev(*config.sections.get(env).values())

        if env == Environments.PROD:
            return cls._prod(*config.sections.get(env).values())
