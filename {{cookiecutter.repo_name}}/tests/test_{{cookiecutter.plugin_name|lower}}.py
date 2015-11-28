import asynctest
from asynctest.mock import patch


class Test{{cookiecutter.plugin_name}}(asynctest.TestCase):

    def setUp(self):
        patcher1 = patch('{{ cookiecutter.package_name|lower }}.{{cookiecutter.plugin_name|lower}}.{{ cookiecutter.plugin_name }}.load_config')  # NOQA
        self.addCleanup(patcher1.stop)
        self.mock_load_config = patcher1.start()

        from {{ cookiecutter.package_name|lower }}.{{cookiecutter.plugin_name|lower}} import {{ cookiecutter.plugin_name }}
        test_plug = {{ cookiecutter.plugin_name }}()  # NOQA

    def tearDown(self):
        pass

    @asynctest.ignore_loop
    def test_something(self):
        pass
