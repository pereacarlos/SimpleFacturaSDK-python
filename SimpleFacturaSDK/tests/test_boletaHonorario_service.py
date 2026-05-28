import json
import unittest

from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.services.BoletaHonorarioService import BoletaHonorarioService
from SimpleFacturaSDK.tests.mock_utils import (
    DummyRequest,
    MockAiohttpResponse,
    MockRequestContext,
    make_service,
)


def bhe_item():
    return {
        "folio": 15,
        "fechaEmision": "2026-05-01",
        "codigoBarra": "ABC123",
        "estado": "Emitida",
    }


class TestBoletaHonorarioService(unittest.IsolatedAsyncioTestCase):
    async def test_ObtenerPdf_Ok(self):
        service, session, client = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, read_data=b"%PDF-1.4")
        )
        response = await service.ObtenerPdf(DummyRequest())
        client.ensure_token_valid.assert_awaited_once()
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, b"%PDF-1.4")

    async def test_ObtenerPdf_BadRequest(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, read_data=b'{"errors":["bad"]}')
        )
        response = await service.ObtenerPdf(DummyRequest())
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_ObtenerPdf_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.ObtenerPdf(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_ListadoBHEEmitidos_Ok(self):
        service, session, _ = make_service(BoletaHonorarioService)
        payload = {"status": 200, "data": [bhe_item()]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ListadoBHEEmitidos(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].folio, 15)

    async def test_ListadoBHEEmitidos_BadRequest(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.ListadoBHEEmitidos(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_ListadoBHEEmitidos_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.ListadoBHEEmitidos(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_ObtenerPdfBoletaRecibida_Ok(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, read_data=b"%PDF-1.4")
        )
        response = await service.ObtenerPdfBoletaRecibida(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, b"%PDF-1.4")

    async def test_ObtenerPdfBoletaRecibida_BadRequest(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, read_data=b'{"errors":["bad"]}')
        )
        response = await service.ObtenerPdfBoletaRecibida(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_ObtenerPdfBoletaRecibida_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.ObtenerPdfBoletaRecibida(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_ListadoBHERecibido_Ok(self):
        service, session, _ = make_service(BoletaHonorarioService)
        payload = {"status": 200, "data": [bhe_item()]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ListadoBHERecibido(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].folio, 15)

    async def test_ListadoBHERecibido_BadRequest(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.ListadoBHERecibido(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_ListadoBHERecibido_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.ListadoBHERecibido(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_EmitirBHE_Ok(self):
        service, session, _ = make_service(BoletaHonorarioService)
        payload = {"status": 200, "data": {"folio": 123}, "message": "ok"}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.EmitirBHE(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["folio"], 123)

    async def test_EmitirBHE_BadRequest(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.EmitirBHE(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_EmitirBHE_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.EmitirBHE(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_EmitirBHETerceros_Ok(self):
        service, session, _ = make_service(BoletaHonorarioService)
        payload = {"status": 200, "data": {"folio": 124}, "message": "ok"}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.EmitirBHETerceros(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data["folio"], 124)

    async def test_EmitirBHETerceros_BadRequest(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.EmitirBHETerceros(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_EmitirBHETerceros_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.EmitirBHETerceros(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_AnularBHE_Ok(self):
        service, session, _ = make_service(BoletaHonorarioService)
        payload = {"status": 200, "data": "BHE anulada", "message": "ok"}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.AnularBHE(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, "BHE anulada")

    async def test_AnularBHE_BadRequest(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.AnularBHE(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_AnularBHE_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.AnularBHE(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_ObservarBHE_Ok(self):
        service, session, _ = make_service(BoletaHonorarioService)
        payload = {"status": 200, "data": "BHE observada", "message": "ok"}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ObservarBHE(DummyRequest())
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, "BHE observada")

    async def test_ObservarBHE_BadRequest(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad"]}')
        )
        response = await service.ObservarBHE(DummyRequest())
        self.assertEqual(response.status, 400)

    async def test_ObservarBHE_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.ObservarBHE(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_ConciliarBHEEmitidas_Ok(self):
        service, session, _ = make_service(BoletaHonorarioService)
        payload = {"status": 200, "data": "OK", "message": "ok"}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ConciliarBHEEmitidas(DummyRequest(), 5, 2026)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, "OK")

    async def test_ConciliarBHEEmitidas_BadRequest(self):
        service, _, _ = make_service(BoletaHonorarioService)
        response = await service.ConciliarBHEEmitidas(DummyRequest(), "5", 2026)
        self.assertEqual(response.status, 400)

    async def test_ConciliarBHEEmitidas_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.ConciliarBHEEmitidas(DummyRequest(), 5, 2026)
        self.assertEqual(response.status, 500)

    async def test_ConciliarBHERecibidas_Ok(self):
        service, session, _ = make_service(BoletaHonorarioService)
        payload = {"status": 200, "data": "OK", "message": "ok"}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        response = await service.ConciliarBHERecibidas(DummyRequest(), 5, 2026)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data, "OK")

    async def test_ConciliarBHERecibidas_BadRequest(self):
        service, _, _ = make_service(BoletaHonorarioService)
        response = await service.ConciliarBHERecibidas(DummyRequest(), 5, "2026")
        self.assertEqual(response.status, 400)

    async def test_ConciliarBHERecibidas_ServerError(self):
        service, session, _ = make_service(BoletaHonorarioService)
        session.post.side_effect = Exception("server error")
        response = await service.ConciliarBHERecibidas(DummyRequest(), 5, 2026)
        self.assertEqual(response.status, 500)
