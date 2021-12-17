from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.webdriver import WebDriver
from test_client.config import Config, Environments


class WebDriverManager:
    def __init__(self, env: str):
        self._env = env
        self._config = Config.properties(env)

    def get_driver(self) -> WebDriver:
        if self._env == Environments.DEV:
            return self._local()

        if self._env == Environments.PROD:
            return self._remote()

    def _local(self):
        return webdriver.Chrome(executable_path=self._config.driver, desired_capabilities=DesiredCapabilities.CHROME)

    def _remote(self):
        connection = RemoteConnection(remote_server_addr=self._config.driver, resolve_ip=False)
        capabilities = {
            'browserName': 'chrome',
            'browserVersion': '80.0',
            'moon:options': {
                'enableVNC': True,
                'enableVideo': False
            }
        }
        return webdriver.Remote(connection, desired_capabilities=capabilities)
