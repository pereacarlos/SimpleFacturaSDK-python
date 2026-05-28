import json
import unittest
from uuid import uuid4

from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.services.ProductoService import ProductoService
from SimpleFacturaSDK.tests.mock_utils import (
    DummyRequest,
    MockAiohttpResponse,
    MockRequestContext,
    make_service,
)


class TestProductoService(unittest.IsolatedAsyncioTestCase):
    async def test_CrearProducto_Ok(self):
        service, session, client = make_service(ProductoService)
        payload = {
            "status": 200,
            "data": [
                {
                    "productoId": str(uuid4()),
                    "nombre": "Producto A",
                    "precio": 1000.0,
                    "exento": False,
                    "activo": True,
                    "impuestos": [],
                }
            ],
        }
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )

        response = await service.CrearProducto(DummyRequest())

        client.ensure_token_valid.assert_awaited_once()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].nombre, "Producto A")

    async def test_CrearProducto_BadRequest(self):
        service, session, _ = make_service(ProductoService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad request"]}')
        )

        response = await service.CrearProducto(DummyRequest())

        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_CrearProducto_ServerError(self):
        service, session, _ = make_service(ProductoService)
        session.post.side_effect = Exception("server error")

        response = await service.CrearProducto(DummyRequest())

        self.assertEqual(response.status, 500)
        self.assertEqual(response.message, "server error")

    async def test_listarProductos_Ok(self):
        service, session, client = make_service(ProductoService)
        payload = {
            "status": 200,
            "data": [
                {
                    "productoId": str(uuid4()),
                    "nombre": "Producto B",
                    "precio": 500.0,
                    "exento": False,
                    "impuestos": [],
                }
            ],
        }
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )

        response = await service.listarProductos(DummyRequest())

        client.ensure_token_valid.assert_awaited_once()
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].nombre, "Producto B")

    async def test_listarProductos_BadRequest(self):
        service, session, _ = make_service(ProductoService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad request"]}')
        )

        response = await service.listarProductos(DummyRequest())

        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_listarProductos_ServerError(self):
        service, session, _ = make_service(ProductoService)
        session.post.side_effect = Exception("server error")

        response = await service.listarProductos(DummyRequest())

        self.assertEqual(response.status, 500)
        self.assertEqual(response.message, "server error")
