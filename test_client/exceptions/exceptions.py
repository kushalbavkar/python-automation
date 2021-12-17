class ConfigError(Exception):
    def __init__(self, message: str):
        super(ConfigError, self).__init__(message)


class MissingEnvironmentError(ConfigError):
    pass


class UnsupportedEnvironmentError(ConfigError):
    pass


class UnsupportedConfigKeyError(ConfigError):
    pass
