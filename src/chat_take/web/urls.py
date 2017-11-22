from tornado.web import url
from chat_take.web.handlers import LogoutHandler, PingHandler


urlpatterns = [
    (r"/logout", LogoutHandler),
    (r"/ping", PingHandler)
]
