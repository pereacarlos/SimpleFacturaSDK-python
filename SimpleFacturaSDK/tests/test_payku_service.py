import json
import unittest
from datetime import datetime

from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.Payku.PaykuRequests import (
    MarcarPagadoOPendienteRequest,
    PaykuReenviarLinkRequest,
    PaykuToggleRequest,
    PaykuTransaccionesRequest,
)
from SimpleFacturaSDK.services.PaykuService import PaykuService
from SimpleFacturaSDK.tests.mock_utils import MockAiohttpResponse, MockRequestContext, make_service


def payku_transacciones_request():
    return PaykuTransaccionesRequest(
        credenciales=Credenciales(rut_emisor="78181331-1"),
        desde=datetime(2026, 5, 1),
        hasta=datetime(2026, 5, 13),
    )


def payku_toggle_request():
    return PaykuToggleRequest(
        credenciales=Credenciales(rut_emisor="78181331-1"),
        activo=True,
    )


def payku_link_request():
    return PaykuReenviarLinkRequest(
        credenciales=Credenciales(rut_emisor="78181331-1"),
        dte=DteReferenciadoExterno(folio=3591, codigoTipoDte=33, ambiente=0),
    )


def payku_estado_request():
    return MarcarPagadoOPendienteRequest(
        credenciales=Credenciales(rut_emisor="78181331-1"),
        dteReferenciadoExterno=DteReferenciadoExterno(folio=3591, codigoTipoDte=33, ambiente=0),
        pagado=True,
    )


class TestPaykuService(unittest.IsolatedAsyncioTestCase):
    def _set_post_json(self, session, status, payload):
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=json.dumps(payload))
        )

    def _set_post_text(self, session, status, text):
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=text)
        )

    async def test_transacciones_ok_bad_server(self):
        service, session, _ = make_service(PaykuService)

        self._set_post_json(
            session,
            200,
            {
                "status": 200,
                "message": "ok",
                "data": [
                    {
                        "fecha": "2026-05-01",
                        "monto": 10000,
                        "estado": "pendiente",
                        "receptorRut": "11111111-1",
                        "receptorRazonSocial": "Cliente",
                        "porcentaje": 0,
                        "montoNeto": 10000,
                        "dteFolio": 3591,
                        "tipo": "33",
                    }
                ],
            },
        )
        ok = await service.transacciones(payku_transacciones_request())
        self.assertEqual(ok.status, 200)
        self.assertEqual(len(ok.data), 1)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.transacciones(payku_transacciones_request())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.transacciones(payku_transacciones_request())
        self.assertEqual(err.status, 500)

    async def test_activar_desactivar_ok_bad_server(self):
        service, session, _ = make_service(PaykuService)

        self._set_post_json(session, 200, {"status": 200, "message": "ok", "data": True})
        ok = await service.activar_desactivar(payku_toggle_request())
        self.assertEqual(ok.status, 200)
        self.assertTrue(ok.data)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.activar_desactivar(payku_toggle_request())
        self.assertEqual(bad.status, 400)
        self.assertFalse(bad.data)

        session.post.side_effect = Exception("server error")
        err = await service.activar_desactivar(payku_toggle_request())
        self.assertEqual(err.status, 500)
        self.assertFalse(err.data)

    async def test_generar_url_ok_bad_server(self):
        service, session, _ = make_service(PaykuService)

        self._set_post_json(
            session,
            200,
            {"status": 200, "message": "ok", "data": "https://payku.test/pago/123"},
        )
        ok = await service.generar_url(payku_link_request())
        self.assertEqual(ok.status, 200)
        self.assertTrue(ok.data.startswith("https://payku.test"))

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.generar_url(payku_link_request())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.generar_url(payku_link_request())
        self.assertEqual(err.status, 500)

    async def test_reenviar_link_qr_ok_bad_server(self):
        service, session, _ = make_service(PaykuService)

        self._set_post_json(session, 200, {"status": 200, "message": "ok", "data": True})
        ok = await service.reenviar_link_qr(payku_link_request())
        self.assertEqual(ok.status, 200)
        self.assertTrue(ok.data)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.reenviar_link_qr(payku_link_request())
        self.assertEqual(bad.status, 400)
        self.assertFalse(bad.data)

        session.post.side_effect = Exception("server error")
        err = await service.reenviar_link_qr(payku_link_request())
        self.assertEqual(err.status, 500)
        self.assertFalse(err.data)

    async def test_marcar_dte_pagado_o_pendiente_ok_bad_server(self):
        service, session, _ = make_service(PaykuService)

        self._set_post_json(session, 200, {"status": 200, "message": "ok", "data": True})
        ok = await service.marcar_dte_pagado_o_pendiente(payku_estado_request())
        self.assertEqual(ok.status, 200)
        self.assertTrue(ok.data)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.marcar_dte_pagado_o_pendiente(payku_estado_request())
        self.assertEqual(bad.status, 400)
        self.assertFalse(bad.data)

        session.post.side_effect = Exception("server error")
        err = await service.marcar_dte_pagado_o_pendiente(payku_estado_request())
        self.assertEqual(err.status, 500)
        self.assertFalse(err.data)
