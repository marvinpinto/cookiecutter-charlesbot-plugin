from charlesbot.base_plugin import BasePlugin
import asyncio


class {{cookiecutter.plugin_name}}(BasePlugin):

    def __init__(self):
        super().__init__("{{cookiecutter.plugin_name}}")

    def get_help_message(self):
        return "!command - Does a really neat thing!"

    @asyncio.coroutine
    def process_message(self, message):
        self.log.info("Processing message %s" % message)
