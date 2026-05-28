import json
import os
import tempfile
import unittest

from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Partner.PartnerDteResumenRequest import PartnerDteResumenRequest
from SimpleFacturaSDK.services.PartnerServices import PartnerService
from SimpleFacturaSDK.tests.mock_utils import DummyRequest, MockAiohttpResponse, MockRequestContext, make_service


class TestPartnerService(unittest.IsolatedAsyncioTestCase):
    def _set_post_json(self, session, status, payload):
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=json.dumps(payload))
        )

    def _set_post_text(self, session, status, text):
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=text)
        )

    def _set_get_json(self, session, status, payload):
        session.get.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=json.dumps(payload))
        )

    def _set_get_text(self, session, status, text):
        session.get.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=text)
        )

    async def test_enrolamiento_empresa_ok_bad_server(self):
        service, session, _ = make_service(PartnerService)

        self._set_post_json(session, 200, {"status": 200, "message": "ok", "data": "Empresa enrolada"})
        ok = await service.enrolamiento_empresa(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data, "Empresa enrolada")

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.enrolamiento_empresa(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.enrolamiento_empresa(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_obtener_actividades_economicas_ok_bad_server(self):
        service, session, _ = make_service(PartnerService)

        self._set_get_json(
            session,
            200,
            {"status": 200, "message": "ok", "data": [{"codigo": 620100, "descripcion": "Software"}]},
        )
        ok = await service.obtener_actividades_economicas()
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data[0].codigo, 620100)

        self._set_get_text(session, 400, '{"errors":["bad"]}')
        bad = await service.obtener_actividades_economicas()
        self.assertEqual(bad.status, 400)

        session.get.side_effect = Exception("server error")
        err = await service.obtener_actividades_economicas()
        self.assertEqual(err.status, 500)

    async def test_upload_logo_ok_bad_server(self):
        service, session, _ = make_service(PartnerService)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            tmp.write(b"fake")
            logo_path = tmp.name

        try:
            self._set_post_json(session, 200, {"status": 200, "message": "ok", "data": True})
            ok = await service.upload_logo(Credenciales(rut_emisor="78181331-1"), logo_path)
            self.assertEqual(ok.status, 200)
            self.assertTrue(ok.data)

            self._set_post_text(session, 400, '{"errors":["bad"]}')
            bad = await service.upload_logo(Credenciales(rut_emisor="78181331-1"), logo_path)
            self.assertEqual(bad.status, 400)
            self.assertFalse(bad.data)

            session.post.side_effect = Exception("server error")
            err = await service.upload_logo(Credenciales(rut_emisor="78181331-1"), logo_path)
            self.assertEqual(err.status, 500)
            self.assertFalse(err.data)
        finally:
            if os.path.exists(logo_path):
                os.remove(logo_path)

    async def test_obtener_resumen_dtes_ok_bad_server(self):
        service, session, _ = make_service(PartnerService)
        request = PartnerDteResumenRequest(
            Credenciales=Credenciales(rut_emisor="78181331-1"),
            Anio=2026,
            Mes=5,
        )

        self._set_post_json(
            session,
            200,
            {"status": 200, "message": "ok", "data": {"dtes": 10, "nombrePlan": "Pro", "dtesAdicionales": 2}},
        )
        ok = await service.obtener_resumen_dtes(request)
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data.dtes, 10)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.obtener_resumen_dtes(request)
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.obtener_resumen_dtes(request)
        self.assertEqual(err.status, 500)
