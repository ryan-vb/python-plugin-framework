import importlib
import configparser
import os
import itertools

class PluginBase:
    def __init__(self, conf_file: str, context: dict):
        self.context = context
        self.conf = configparser.ConfigParser()
        self.conf.read(conf_file)
        self._search()
        self._enabled_plugin_files = self.plugins
        self._import_enabled_plugins()
        self._execute_plugins()

    def _search(self):
        plugin_dir = self.conf.get("plugins", "plugin_dir")
        walk_files = (file_names for _, _, file_names in os.walk(plugin_dir))
        all_files = list(itertools.chain.from_iterable(walk_files))
        self._plugin_files = all_files

    def _import_plugins(self):
        self._plugins = [importlib.import_module(plugin, ".") for plugin in self._enabled_plugin_files]

    def _execute_plugins(self):
        map(lambda p: p.run(self.context), self._plugins)


