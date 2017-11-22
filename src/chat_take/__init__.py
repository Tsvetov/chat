from tornado.ioloop import IOLoop
import typing
from asyncio import AbstractEventLoop, tasks

from tornado.gen import convert_yielded
from tornado.platform.asyncio import AsyncIOMainLoop, to_asyncio_future


def task_factory(loop: AbstractEventLoop, coro: typing.Coroutine) -> tasks.Task:
    loop._check_closed()
    return to_asyncio_future(convert_yielded(coro))


def make_loop() -> AsyncIOMainLoop:
    main_loop = AsyncIOMainLoop()
    main_loop.asyncio_loop.set_task_factory(task_factory)
    return main_loop


def install_ioloop() -> AsyncIOMainLoop:
    main_loop = make_loop()
    main_loop.install()
    return main_loop


def setup() -> None:
    install_ioloop()
