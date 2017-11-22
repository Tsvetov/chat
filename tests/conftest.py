import pytest
import tornado.web

from chat_take.web.urls import urlpatterns


@pytest.fixture
def app():
    return tornado.web.Application(urlpatterns)
