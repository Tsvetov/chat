import click
from tornado.ioloop import IOLoop
from tornado.web import Application

from chat import setup
from chat.web.urls import urlpatterns


@click.group()
def cli() -> None:
    setup()


@cli.command()
@click.option('--autoreload', is_flag=True)
@click.option('--host', type=str, default='127.0.0.1')
@click.option('--port', type=int, default=8000)
def serve(autoreload: bool, host: str, port: int) -> None:
    app = Application(urlpatterns, autoreload=autoreload)
    app.listen(port=port, address=host)
    IOLoop.current().start()
