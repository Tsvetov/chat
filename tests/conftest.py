import pytest
import tornado.web

from chat.web.urls import urlpatterns


@pytest.fixture
def app():
    return tornado.web.Application(urlpatterns)
