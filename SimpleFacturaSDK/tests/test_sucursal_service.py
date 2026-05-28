import json
import unittest

from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.services.SucursalService import SucursalService
from SimpleFacturaSDK.tests.mock_utils import (
    DummyRequest,
    MockAiohttpResponse,
    MockRequestContext,
    make_service,
)


class TestSucursalService(unittest.IsolatedAsyncioTestCase):
    async def test_ListarSucursales_Ok(self):
        service, session, client = make_service(SucursalService)
        payload = {
            "status": 200,
            "data": [
                {"nombre": "Casa Matriz", "direccion": "Av. Principal 123"},
            ],
        }
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )

        response = await service.ListarSucursales(DummyRequest())

        client.ensure_token_valid.assert_awaited_once()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].nombre, "Casa Matriz")

    async def test_ListarSucursales_BadRequest(self):
        service, session, _ = make_service(SucursalService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad request"]}')
        )

        response = await service.ListarSucursales(DummyRequest())

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_ListarSucursales_ServerError(self):
        service, session, _ = make_service(SucursalService)
        session.post.side_effect = Exception("server error")

        response = await service.ListarSucursales(DummyRequest())

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertEqual(response.message, "server error")
