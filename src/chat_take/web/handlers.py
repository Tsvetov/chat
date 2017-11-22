import logging
from redis import StrictRedis
from tornado import web, websocket, escape

r = StrictRedis(db=1)

logger = logging.getLogger('handlers')


class PingHandler(web.RequestHandler):
    def get(self):
        self.write('ok')  # pylint: disable=no-member


class LogoutHandler(web.RequestHandler):
    @web.authenticated
    def get(self):
        self.clear_cookie('user')
        self.redirect('/')