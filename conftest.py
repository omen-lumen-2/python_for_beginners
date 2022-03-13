import pytest

from fixture.application import Application

application = None
login = "admin"
password = "secret"


@pytest.fixture()
def app():
    """ Fixture for work with class Application in each test function"""
    global application
    if application is None or application.is_not_valid():
        application = Application()
    application.session.ensure_login(login=login, password=password)
    return application


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def _inner():
        application.session.ensure_logout()
        application.wd_quit()
    request.addfinalizer(_inner)

