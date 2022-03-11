import pytest

from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    """ Fixture for work with class Application in each test function"""
    application = Application()
    request.addfinalizer(application.wd_quit)
    return application
