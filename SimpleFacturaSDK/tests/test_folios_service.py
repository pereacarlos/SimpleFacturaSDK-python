import json
import unittest

from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.services.FolioService import FolioService
from SimpleFacturaSDK.tests.mock_utils import (
    DummyRequest,
    MockAiohttpResponse,
    MockRequestContext,
    make_service,
)


class TestFoliosService(unittest.IsolatedAsyncioTestCase):
    async def test_ConsultaFoliosDisponibles_Ok(self):
        service, session, client = make_service(FolioService)
        payload = {"status": 200, "data": 15}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ConsultaFoliosDisponibles(DummyRequest())
        client.ensure_token_valid.assert_awaited_once()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, 15)

    async def test_ConsultaFoliosDisponibles_BadRequest(self):
        service, session, _ = make_service(FolioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.ConsultaFoliosDisponibles(DummyRequest())
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_ConsultaFoliosDisponibles_ServerError(self):
        service, session, _ = make_service(FolioService)
        session.post.side_effect = Exception("server error")
        response = await service.ConsultaFoliosDisponibles(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_SolicitarFolios_Ok(self):
        service, session, _ = make_service(FolioService)
        payload = {"status": 200, "data": {"codigoSii": 33, "desde": 1, "hasta": 10}}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.SolicitarFolios(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data.desde, 1)

    async def test_SolicitarFolios_BadRequest(self):
        service, session, _ = make_service(FolioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.SolicitarFolios(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_SolicitarFolios_ServerError(self):
        service, session, _ = make_service(FolioService)
        session.post.side_effect = Exception("server error")
        response = await service.SolicitarFolios(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_ConsultarFolios_Ok(self):
        service, session, _ = make_service(FolioService)
        payload = {
            "status": 200,
            "data": [{"codigoSii": 33, "desde": 1, "hasta": 10, "foliosDisponibles": 10}],
        }
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ConsultarFolios(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(len(response.data), 1)

    async def test_ConsultarFolios_BadRequest(self):
        service, session, _ = make_service(FolioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.ConsultarFolios(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_ConsultarFolios_ServerError(self):
        service, session, _ = make_service(FolioService)
        session.post.side_effect = Exception("server error")
        response = await service.ConsultarFolios(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_Folios_Sin_Uso_Ok(self):
        service, session, _ = make_service(FolioService)
        payload = {"status": 200, "data": [{"desde": 1, "hasta": 10}]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.Folios_Sin_Uso(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].cantidad, 10)

    async def test_Folios_Sin_Uso_BadRequest(self):
        service, session, _ = make_service(FolioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.Folios_Sin_Uso(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_Folios_Sin_Uso_ServerError(self):
        service, session, _ = make_service(FolioService)
        session.post.side_effect = Exception("server error")
        response = await service.Folios_Sin_Uso(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_anular_Folio_Ok(self):
        service, session, _ = make_service(FolioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data='{"status":200}')
        )
        response = await service.anular_Folio(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertTrue(response.data)

    async def test_anular_Folio_BadRequest(self):
        service, session, _ = make_service(FolioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.anular_Folio(DummyRequest())
        self.assertEqual(response.status, 400)
        self.assertFalse(response.data)

    async def test_anular_Folio_ServerError(self):
        service, session, _ = make_service(FolioService)
        session.post.side_effect = Exception("server error")
        response = await service.anular_Folio(DummyRequest())
        self.assertEqual(response.status, 500)
