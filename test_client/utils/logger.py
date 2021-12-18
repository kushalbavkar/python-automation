import logging
from enum import Enum
from pathlib import Path

__all__ = ['Levels', 'Patterns', 'Handlers', 'Logger', 'logger']


class Levels(Enum):
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0


class Patterns(Enum):
    BASIC = '%(name)s - [%(levelname)s] - %(message)s'
    ADVANCED = '%(name)s - [%(levelname)s] - %(filename)s - [%(lineno)d] - %(message)s'


class Handlers(Enum):
    STREAM = 'StreamHandler'
    FILE = 'FileHandler'


class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(Logger)
        return cls.__instance

    def __init__(self):
        self.level = Levels.INFO.value
        self.pattern = logging.Formatter(Patterns.BASIC.value)
        self.handler = logging.StreamHandler()

    def set_level(self, level: Levels):
        self.level = level.value

    def set_pattern(self, pattern: Patterns):
        self.pattern = logging.Formatter(pattern.value)

    def set_handler(self, handler: Handlers, *, file: str = 'log.txt'):
        if handler == Handlers.FILE:
            self.handler = logging.FileHandler(file)
        else:
            self.handler = logging.StreamHandler

    def get_logger(self, name: str):
        log = logging.getLogger(self.resolve_name(name))
        log.setLevel(self.level)
        self.handler.setFormatter(self.pattern)
        log.addHandler(self.handler)

        return log

    @staticmethod
    def resolve_name(name: str):
        path = Path(name)
        return path.name if path.exists() else name


logger = Logger()
