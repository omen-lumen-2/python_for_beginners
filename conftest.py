import json
import os.path

import pytest

from fixture.application import Application

application = None
target = None


@pytest.fixture()
def app(request):
    """ Fixture for work with class Application in each test function"""
    global application
    global target
    browser = request.config.getoption('--browser')
    if target is None:
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--config_file'))
        with open(file) as config_file:
            target = json.load(config_file)
    if application is None or application.is_not_valid():
        application = Application(browser=browser, base_url=target['base_url'])
    application.session.ensure_login(login=target['login'], password=target['password'])
    return application


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def _inner():
        application.session.ensure_logout()
        application.wd_quit()
    request.addfinalizer(_inner)


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='firefox', help='type of browser')
    parser.addoption("--config_file", action='store', default='config.json', help='file with config')
