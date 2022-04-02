import importlib
import jsonpickle
import os.path

import pytest

from fixture.application import Application
from fixture.db import DbFixture

application = None
target = None


def load_config(file):
    global target
    if target is None:
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(file) as config_file:
            target = jsonpickle.decode(config_file.read())
    return target


@pytest.fixture()
def app(request):
    """ Fixture for work with class Application in each test function"""
    global application
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--config_file'))['web']
    if application is None or application.is_not_valid():
        application = Application(browser=browser, base_url=web_config['base_url'])
    application.session.ensure_login(login=web_config['login'], password=web_config['password'])
    return application

@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption('--config_file'))['bd']
    dbfixture = DbFixture(host=db_config['host'],
                          name=db_config['name'],
                          user=db_config['user'],
                          password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return  dbfixture


@pytest.fixture(scope='session')
def check_ui(request):
    return request.config.getoption('--check_ui')


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def _inner():
        application.session.ensure_logout()
        application.wd_quit()
    request.addfinalizer(_inner)


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='firefox', help='type of browser')
    parser.addoption("--config_file", action='store', default='config.json', help='file with config')
    parser.addoption("--check_ui", action='store_true', help='file with config')


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
