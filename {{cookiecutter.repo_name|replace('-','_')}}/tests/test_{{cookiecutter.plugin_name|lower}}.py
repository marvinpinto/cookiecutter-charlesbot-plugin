import asynctest

from {{ cookiecutter.package_name }} import {{ cookiecutter.plugin_name }}


class Test{{cookiecutter.plugin_name}}(asynctest.TestCase):

    def setUp(self):
        test_plug = {{ cookiecutter.plugin_name }}()  # NOQA

    def tearDown(self):
        pass

    @asynctest.ignore_loop
    def test_something(self):
        pass
