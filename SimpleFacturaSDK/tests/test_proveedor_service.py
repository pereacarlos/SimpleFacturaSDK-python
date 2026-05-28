import json
import unittest

from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.services.ProveedorService import ProveedorService
from SimpleFacturaSDK.tests.mock_utils import (
    DummyRequest,
    MockAiohttpResponse,
    MockRequestContext,
    make_service,
)


def dte_item():
    return {
        "detalles": [],
        "referencias": [],
        "folio": 10,
        "tipoDte": "FacturaElectronica",
        "rutReceptor": "11111111-1",
        "razonSocialReceptor": "Cliente",
    }


class TestProveedorService(unittest.IsolatedAsyncioTestCase):
    async def test_Aceptar_RechazarDTE_Ok(self):
        service, session, client = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data='{"status":200}')
        )
        response = await service.Aceptar_RechazarDTE(DummyRequest())
        client.ensure_token_valid.assert_awaited_once()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertTrue(response.data)

    async def test_Aceptar_RechazarDTE_BadRequest(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.Aceptar_RechazarDTE(DummyRequest())
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_Aceptar_RechazarDTE_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")
        response = await service.Aceptar_RechazarDTE(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_listarDteRecibidos_Ok(self):
        service, session, _ = make_service(ProveedorService)
        payload = {"status": 200, "data": [dte_item()]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.listarDteRecibidos(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].folio, 10)

    async def test_listarDteRecibidos_BadRequest(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.listarDteRecibidos(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_listarDteRecibidos_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")
        response = await service.listarDteRecibidos(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_obtenerXml_Ok(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data="", read_data=b"<xml/>")
        )
        response = await service.obtenerXml(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, b"<xml/>")

    async def test_obtenerXml_BadRequest(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.obtenerXml(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_obtenerXml_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")
        response = await service.obtenerXml(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_obtener_pdf_Ok(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, read_data=b"%PDF-1.4")
        )
        response = await service.obtener_pdf(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, b"%PDF-1.4")

    async def test_obtener_pdf_BadRequest(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, read_data=b'{"errors":["bad"]}')
        )
        response = await service.obtener_pdf(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_obtener_pdf_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")
        response = await service.obtener_pdf(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_ConciliarRecibidos_Ok(self):
        service, session, _ = make_service(ProveedorService)
        payload = {"status": 200, "data": "Consolidado OK"}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ConciliarRecibidos(DummyRequest(), 5, 2026)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, "Consolidado OK")

    async def test_ConciliarRecibidos_BadRequest(self):
        service, _, _ = make_service(ProveedorService)
        response = await service.ConciliarRecibidos(DummyRequest(), "5", 2026)
        self.assertEqual(response.status, 400)

    async def test_ConciliarRecibidos_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")
        response = await service.ConciliarRecibidos(DummyRequest(), 5, 2026)
        self.assertEqual(response.status, 500)

    async def test_obtener_TrazasRecibidas_Ok(self):
        service, session, _ = make_service(ProveedorService)
        payload = {"status": 200, "data": [{"fecha": "2026-05-01", "descripcion": "Recibido"}]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.obtener_TrazasRecibidas(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].descripcion, "Recibido")

    async def test_obtener_TrazasRecibidas_BadRequest(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.obtener_TrazasRecibidas(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_obtener_TrazasRecibidas_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")
        response = await service.obtener_TrazasRecibidas(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_actualizar_Lista_Proveedor_Ok(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data='{"status":200}')
        )
        response = await service.actualizar_Lista_Proveedor(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertTrue(response.data)

    async def test_actualizar_Lista_Proveedor_BadRequest(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.actualizar_Lista_Proveedor(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_actualizar_Lista_Proveedor_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")
        response = await service.actualizar_Lista_Proveedor(DummyRequest())
        self.assertEqual(response.status, 500)
