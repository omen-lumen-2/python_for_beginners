import importlib
import jsonpickle
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
            target = jsonpickle.decode(config_file.read())
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

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[repr(x) for x in testdata])
        elif fixture.startswith('json_'):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[repr(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module(f"data.{module}").data


def load_from_json(module):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", f"{module}.json"), 'r') as f:
        return jsonpickle.decode(f.read())
