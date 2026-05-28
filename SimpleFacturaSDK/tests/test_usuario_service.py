import json
import unittest

from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.services.UsuarioService import UsuarioService
from SimpleFacturaSDK.tests.mock_utils import (
    DummyRequest,
    MockAiohttpResponse,
    MockRequestContext,
    make_service,
)


class TestUsuarioService(unittest.IsolatedAsyncioTestCase):
    async def test_ListarUsuario_Ok(self):
        service, session, client = make_service(UsuarioService)
        payload = {
            "status": 200,
            "data": [
                {
                    "rut": "78181331-1",
                    "nombre": "Carlos",
                    "apellidos": "Perea",
                    "email": "cperea@chilesystems.com",
                }
            ],
        }
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )

        response = await service.ListarUsuario(DummyRequest())

        client.ensure_token_valid.assert_awaited_once()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].email, "cperea@chilesystems.com")

    async def test_ListarUsuario_BadRequest(self):
        service, session, _ = make_service(UsuarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad request"]}')
        )

        response = await service.ListarUsuario(DummyRequest())

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_ListarUsuario_ServerError(self):
        service, session, _ = make_service(UsuarioService)
        session.post.side_effect = Exception("server error")

        response = await service.ListarUsuario(DummyRequest())

        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertEqual(response.message, "server error")
