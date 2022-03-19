import pytest

from fixture.application import Application

application = None


@pytest.fixture()
def app(request):
    """ Fixture for work with class Application in each test function"""
    global application
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption("--base_url")
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")
    if application is None or application.is_not_valid():
        application = Application(browser=browser, base_url=base_url)
    application.session.ensure_login(login=login, password=password)
    return application


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def _inner():
        application.session.ensure_logout()
        application.wd_quit()
    request.addfinalizer(_inner)


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='firefox', help='type of browser')
    parser.addoption("--base_url", action='store', default='http://localhost/addressbook/', help='base_url')
    parser.addoption("--login", action='store', default='admin', help='login admin')
    parser.addoption("--password", action='store', default='secret', help='password')
