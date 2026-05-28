import json
import unittest

from SimpleFacturaSDK.services.CesionServices import CesionService
from SimpleFacturaSDK.tests.mock_utils import DummyRequest, MockAiohttpResponse, MockRequestContext, make_service


class TestCesionService(unittest.IsolatedAsyncioTestCase):
    def _set_post_json(self, session, status, payload):
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=json.dumps(payload))
        )

    def _set_post_text(self, session, status, text):
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=text)
        )

    async def test_obtener_trazas_cesion_emitida_ok_bad_server(self):
        service, session, _ = make_service(CesionService)

        self._set_post_json(
            session,
            200,
            {"status": 200, "data": [{"fecha": "2026-05-01", "descripcion": "Creada"}]},
        )
        ok = await service.obtener_TrazasCesionEmitida(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data[0].descripcion, "Creada")

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.obtener_TrazasCesionEmitida(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.obtener_TrazasCesionEmitida(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_ceder_factura_ok_bad_server(self):
        service, session, _ = make_service(CesionService)

        self._set_post_text(session, 200, "Cesion creada")
        ok = await service.ceder_Factura(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data, "Cesion creada")

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.ceder_Factura(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.ceder_Factura(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_listado_cesiones_emitidas_ok_bad_server(self):
        service, session, _ = make_service(CesionService)

        self._set_post_json(
            session,
            200,
            {"status": 200, "message": "ok", "data": [{"folio": 100}]},
        )
        ok = await service.listado_CesionesEmitidas(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(len(ok.data), 1)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.listado_CesionesEmitidas(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.listado_CesionesEmitidas(DummyRequest())
        self.assertEqual(err.status, 500)
