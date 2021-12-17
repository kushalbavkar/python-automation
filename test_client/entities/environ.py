import os
from enum import Enum


class Environ(Enum):
    Environment = os.getenv('Environment')
