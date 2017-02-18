# This relies on each of the submodules having an __all__ variable.

from .client import *
from .exceptions import *
from .protocol import *
from .server import *
from .uri import *
from .version import version as __version__                             # noqa
from .protocol import connections
import asyncio

@asyncio.coroutine
def emit(data):
    for connection in connections:
        yield from connection.send(data)


__all__ = (
    client.__all__ +
    exceptions.__all__ +
    protocol.__all__ +
    server.__all__ +
    uri.__all__
)
