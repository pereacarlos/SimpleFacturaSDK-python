import json
import unittest
from uuid import uuid4

from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.services.ClientesService import ClientesService
from SimpleFacturaSDK.tests.mock_utils import (
    DummyRequest,
    MockAiohttpResponse,
    MockRequestContext,
    make_service,
)


def cliente_payload():
    return {
        "receptorId": str(uuid4()),
        "emisorId": str(uuid4()),
        "rut": 78181331,
        "dv": "1",
        "rutFormateado": "78181331-1",
        "razonSocial": "CHILESYSTEMS SPA",
        "giro": "Servicios",
        "dirPart": "Direccion 1",
        "dirFact": "Direccion 1",
        "correoFact": "facturacion@chilesystems.cl",
        "ciudad": "Santiago",
        "comuna": "Santiago",
        "activo": True,
    }


class TestClientesService(unittest.IsolatedAsyncioTestCase):
    async def test_CrearClientes_Ok(self):
        service, session, client = make_service(ClientesService)
        payload = {"status": 200, "data": [cliente_payload()]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )

        response = await service.CrearClientes(DummyRequest())

        client.ensure_token_valid.assert_awaited_once()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].razonSocial, "CHILESYSTEMS SPA")

    async def test_CrearClientes_BadRequest(self):
        service, session, _ = make_service(ClientesService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad request"]}')
        )
        response = await service.CrearClientes(DummyRequest())
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_CrearClientes_ServerError(self):
        service, session, _ = make_service(ClientesService)
        session.post.side_effect = Exception("server error")
        response = await service.CrearClientes(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_ListarClientes_Ok(self):
        service, session, _ = make_service(ClientesService)
        payload = {"status": 200, "data": [cliente_payload()]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ListarClientes(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].rutFormateado, "78181331-1")

    async def test_ListarClientes_BadRequest(self):
        service, session, _ = make_service(ClientesService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad request"]}')
        )
        response = await service.ListarClientes(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_ListarClientes_ServerError(self):
        service, session, _ = make_service(ClientesService)
        session.post.side_effect = Exception("server error")
        response = await service.ListarClientes(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_ObtenerDatosCliente_Ok(self):
        service, session, _ = make_service(ClientesService)
        payload = {"status": 200, "data": cliente_payload()}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ObtenerDatosCliente(DummyRequest(), "78181331-1")
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data.razonSocial, "CHILESYSTEMS SPA")

    async def test_ObtenerDatosCliente_BadRequest(self):
        service, session, _ = make_service(ClientesService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad request"]}')
        )
        response = await service.ObtenerDatosCliente(DummyRequest(), "78181331-1")
        self.assertEqual(response.status, 400)

    async def test_ObtenerDatosCliente_ServerError(self):
        service, session, _ = make_service(ClientesService)
        session.post.side_effect = Exception("server error")
        response = await service.ObtenerDatosCliente(DummyRequest(), "78181331-1")
        self.assertEqual(response.status, 500)

    async def test_Actualizar_Clientes_Ok(self):
        service, session, _ = make_service(ClientesService)
        payload = {"status": 200, "data": [cliente_payload()]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.Actualizar_Clientes(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(len(response.data), 1)

    async def test_Actualizar_Clientes_BadRequest(self):
        service, session, _ = make_service(ClientesService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad request"]}')
        )
        response = await service.Actualizar_Clientes(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_Actualizar_Clientes_ServerError(self):
        service, session, _ = make_service(ClientesService)
        session.post.side_effect = Exception("server error")
        response = await service.Actualizar_Clientes(DummyRequest())
        self.assertEqual(response.status, 500)
