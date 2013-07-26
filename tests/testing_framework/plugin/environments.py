from flexmock import flexmock
from tests.testing_framework.utils import ExpensiveResourceProxy
from tests.testing_framework.config.environments import PluginConfigEnvironmentBuilder
from framework.plugin.plugin_handler import PluginHandler


class PluginHandlerEnvironmentBuilder():

    plugin_config_proxy = ExpensiveResourceProxy(PluginConfigEnvironmentBuilder())

    def __init__(self):
        self._create_core_mock()
        self._mock_shell_calls_for_scanner()
        self.plugin_handler = PluginHandler(self.core_mock, self._get_options())
        flexmock(self.plugin_handler.scanner)

    def get_plugin_handler(self):
        return self.plugin_handler

    def _create_core_mock(self):
        self.core_mock = flexmock()
        self.core_mock.Config = flexmock()
        self.core_mock.Config.Plugin = self.__class__.plugin_config_proxy.get_instance()

    def _mock_shell_calls_for_scanner(self):
        self.core_mock.Shell = flexmock()
        self.core_mock.Shell.should_receive("shell_exec")

    def _get_options(self):
        return {"Simulation": False,
                "Scope": "localhost",
                "PluginGroup": "web",
                "PluginType": "quiet",
                "Algorithm": "breadth",
                "ListPlugins": None,
                "OnlyPlugins": None,
                "ExceptPlugins": None}
