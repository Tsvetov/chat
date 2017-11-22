import click
from tornado.ioloop import IOLoop
from tornado.web import Application

from chat_take import setup
from chat_take.web.urls import urlpatterns


@click.group()
def cli() -> None:
    print(12123123)
    setup()


@cli.command()
@click.option('--debug', is_flag=True)
@click.option('--host', type=str, default='127.0.0.1')
@click.option('--port', type=int, default=8000)
def serve(debug: bool, host: str, port: int) -> None:
    app = Application(urlpatterns, debug=debug)
    app.listen(port=port, address=host)
    IOLoop.current().start()
