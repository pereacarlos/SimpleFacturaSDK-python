from dataclasses import dataclass
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock


@dataclass
class DummyRequest:
    value: str = "ok"

    def to_dict(self):
        return {"value": self.value}


class MockAiohttpResponse:
    def __init__(self, status=200, text_data="", read_data=b""):
        self.status = status
        self._text_data = text_data
        self._read_data = read_data

    async def text(self):
        return self._text_data

    async def read(self):
        return self._read_data


class MockRequestContext:
    def __init__(self, response):
        self._response = response

    async def __aenter__(self):
        return self._response

    async def __aexit__(self, exc_type, exc, tb):
        return False


def make_service(service_cls):
    session = MagicMock()
    session.closed = True
    session.close = AsyncMock()
    client = SimpleNamespace(ensure_token_valid=AsyncMock())
    service = service_cls("https://api.test", {}, session, client)
    return service, session, client
