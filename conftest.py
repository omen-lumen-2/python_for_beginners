import pytest

from application import Application


@pytest.fixture(scope='class')
def app(request):
    """ Fixture for work with class Application in each test function"""
    application = Application()
    request.addfinalizer(application.wd_quit)
    return application
