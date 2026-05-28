import json
import os
import tempfile
import unittest

import SimpleFacturaSDK.services.FacturaService as factura_module
from SimpleFacturaSDK.services.FacturaService import FacturacionService
from SimpleFacturaSDK.tests.mock_utils import (
    DummyRequest,
    MockAiohttpResponse,
    MockRequestContext,
    make_service,
)


def invoice_payload():
    return {
        "tipoDTE": 33,
        "rutEmisor": "78181331-1",
        "rutReceptor": "11111111-1",
        "folio": 10,
        "fechaEmision": "2026-05-01",
        "total": 1190.0,
    }


def dte_payload():
    return {
        "detalles": [],
        "referencias": [],
        "folio": 10,
        "tipoDte": "FacturaElectronica",
        "rutReceptor": "11111111-1",
        "razonSocialReceptor": "Cliente",
    }


def reporte_payload():
    return {
        "fecha": "2026-05-01T00:00:00",
        "tiposDTE": "Factura",
        "emitidos": 1,
        "anulados": 0,
        "totalNeto": 1000.0,
        "totalExento": 0.0,
        "totalIva": 190.0,
        "total": 1190.0,
        "detalle": [],
    }


def contribuyente_payload():
    return {
        "rut": "78181331-1",
        "razonSocial": "CHILESYSTEMS SPA",
        "correoIntercambio": "dte@chilesystems.cl",
        "fechaActualizacion": None,
    }


class TestFacturacionService(unittest.IsolatedAsyncioTestCase):
    def _set_post_json(self, session, status, payload):
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=json.dumps(payload))
        )

    def _set_post_text(self, session, status, text):
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, text_data=text)
        )

    def _set_post_bytes(self, session, status, data):
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=status, read_data=data)
        )

    async def test_anular_guia_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_text(session, 200, '{"status":200}')
        ok = await service.anular_guia(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertTrue(ok.data)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.anular_guia(DummyRequest())
        self.assertEqual(bad.status, 400)
        self.assertFalse(bad.data)

        session.post.side_effect = Exception("server error")
        err = await service.anular_guia(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_obtener_pdf_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_bytes(session, 200, b"%PDF")
        ok = await service.obtener_pdf(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data, b"%PDF")

        self._set_post_bytes(session, 400, b'{"errors":["bad"]}')
        bad = await service.obtener_pdf(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.obtener_pdf(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_obtener_timbre_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_bytes(session, 200, b"PNG")
        ok = await service.obtener_timbre(DummyRequest())
        self.assertEqual(ok.status, 200)

        self._set_post_bytes(session, 400, b'{"errors":["bad"]}')
        bad = await service.obtener_timbre(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.obtener_timbre(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_obtener_xml_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_bytes(session, 200, b"<xml/>")
        ok = await service.obtener_xml(DummyRequest())
        self.assertEqual(ok.status, 200)

        self._set_post_bytes(session, 400, b'{"errors":["bad"]}')
        bad = await service.obtener_xml(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.obtener_xml(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_obtener_dte_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(session, 200, {"status": 200, "data": dte_payload()})
        ok = await service.obtener_dte(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data.folio, 10)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.obtener_dte(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.obtener_dte(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_obtener_sobre_xml_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_bytes(session, 200, b"<sobre/>")
        ok = await service.obtener_sobreXml(DummyRequest(), 0)
        self.assertEqual(ok.status, 200)

        self._set_post_bytes(session, 400, b'{"errors":["bad"]}')
        bad = await service.obtener_sobreXml(DummyRequest(), 0)
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.obtener_sobreXml(DummyRequest(), 0)
        self.assertEqual(err.status, 500)

    async def test_facturacion_individual_v2_dte_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(session, 200, {"status": 200, "data": invoice_payload()})
        ok = await service.facturacion_individualV2_Dte(DummyRequest(), "Casa Matriz")
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data.folio, 10)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.facturacion_individualV2_Dte(DummyRequest(), "Casa Matriz")
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.facturacion_individualV2_Dte(DummyRequest(), "Casa Matriz")
        self.assertEqual(err.status, 500)

    async def test_facturacion_individual_v2_boletas_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(session, 200, {"status": 200, "data": invoice_payload()})
        ok = await service.facturacion_individualV2_Boletas(DummyRequest(), "Casa Matriz")
        self.assertEqual(ok.status, 200)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.facturacion_individualV2_Boletas(DummyRequest(), "Casa Matriz")
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.facturacion_individualV2_Boletas(DummyRequest(), "Casa Matriz")
        self.assertEqual(err.status, 500)

    async def test_facturacion_individual_v2_exportacion_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(session, 200, {"status": 200, "data": invoice_payload()})
        ok = await service.facturacion_individualV2_Exportacion(DummyRequest(), "Casa Matriz")
        self.assertEqual(ok.status, 200)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.facturacion_individualV2_Exportacion(DummyRequest(), "Casa Matriz")
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.facturacion_individualV2_Exportacion(DummyRequest(), "Casa Matriz")
        self.assertEqual(err.status, 500)

    async def test_facturacion_masiva_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            tmp.write(b"col1\nvalue")
            path = tmp.name

        try:
            self._set_post_text(session, 200, "OK")
            ok = await service.facturacion_Masiva(DummyRequest(), path)
            self.assertEqual(ok.status, 200)

            self._set_post_text(session, 400, '{"errors":["bad"]}')
            bad = await service.facturacion_Masiva(DummyRequest(), path)
            self.assertEqual(bad.status, 400)

            session.post.side_effect = Exception("server error")
            err = await service.facturacion_Masiva(DummyRequest(), path)
            self.assertEqual(err.status, 500)
        finally:
            if os.path.exists(path):
                os.remove(path)

    async def test_emision_nc_nd_v2_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(session, 200, {"status": 200, "data": invoice_payload()})
        ok = await service.EmisionNC_ND_V2(DummyRequest(), "Casa Matriz", 1)
        self.assertEqual(ok.status, 200)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.EmisionNC_ND_V2(DummyRequest(), "Casa Matriz", 1)
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.EmisionNC_ND_V2(DummyRequest(), "Casa Matriz", 1)
        self.assertEqual(err.status, 500)

    async def test_listado_dte_emitidos_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(session, 200, {"status": 200, "data": [dte_payload()]})
        ok = await service.listadoDteEmitidos(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(len(ok.data), 1)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.listadoDteEmitidos(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.listadoDteEmitidos(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_enviar_correo_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_text(session, 200, '{"status":200}')
        ok = await service.enviarCorreo(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertTrue(ok.data)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.enviarCorreo(DummyRequest())
        self.assertEqual(bad.status, 400)
        self.assertFalse(bad.data)

        session.post.side_effect = Exception("server error")
        err = await service.enviarCorreo(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_consolidado_ventas_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(session, 200, {"status": 200, "data": [reporte_payload()]})
        ok = await service.consolidadoVentas(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(len(ok.data), 1)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.consolidadoVentas(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.consolidadoVentas(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_conciliar_emitidos_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(session, 200, {"status": 200, "data": "ok"})
        ok = await service.ConciliarEmitidos(DummyRequest(), 5, 2026)
        self.assertEqual(ok.status, 200)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.ConciliarEmitidos(DummyRequest(), 5, 2026)
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.ConciliarEmitidos(DummyRequest(), 5, 2026)
        self.assertEqual(err.status, 500)

    async def test_obtener_trazas_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(
            session,
            200,
            {"status": 200, "data": [{"fecha": "2026-05-01", "descripcion": "Emitido"}]},
        )
        ok = await service.obtener_Trazas(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data[0].descripcion, "Emitido")

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.obtener_Trazas(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.obtener_Trazas(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_ceder_factura_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_text(session, 200, "Cedida")
        ok = await service.ceder_Factura(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data, "Cedida")

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.ceder_Factura(DummyRequest())
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.ceder_Factura(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_preview_dte_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_bytes(session, 200, b"%PDF")
        ok = await service.preview_Dte(DummyRequest(), "Casa Matriz")
        self.assertEqual(ok.status, 200)

        self._set_post_bytes(session, 400, b'{"errors":["bad"]}')
        bad = await service.preview_Dte(DummyRequest(), "Casa Matriz")
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.preview_Dte(DummyRequest(), "Casa Matriz")
        self.assertEqual(err.status, 500)

    async def test_reenvio_sii_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_text(session, 200, '{"status":200}')
        ok = await service.reenvio_Sii(DummyRequest())
        self.assertEqual(ok.status, 200)
        self.assertTrue(ok.data)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.reenvio_Sii(DummyRequest())
        self.assertEqual(bad.status, 400)
        self.assertFalse(bad.data)

        session.post.side_effect = Exception("server error")
        err = await service.reenvio_Sii(DummyRequest())
        self.assertEqual(err.status, 500)

    async def test_ultima_sincronizacion_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)

        setattr(factura_module, "mes", 5)
        setattr(factura_module, "anio", 2026)

        self._set_post_json(session, 200, {"status": 200, "data": "2026-05-01T00:00:00"})
        ok = await service.ultima_sincronizacion(DummyRequest(), "78181331-1")
        self.assertEqual(ok.status, 200)

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.ultima_sincronizacion(DummyRequest(), "78181331-1")
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.ultima_sincronizacion(DummyRequest(), "78181331-1")
        self.assertEqual(err.status, 500)

    async def test_obtener_correo_intercambio_ok_bad_server(self):
        service, session, _ = make_service(FacturacionService)
        self._set_post_json(session, 200, {"status": 200, "data": contribuyente_payload()})
        ok = await service.obtener_correo_intercambio(DummyRequest(), "78181331-1")
        self.assertEqual(ok.status, 200)
        self.assertEqual(ok.data.rut, "78181331-1")

        self._set_post_text(session, 400, '{"errors":["bad"]}')
        bad = await service.obtener_correo_intercambio(DummyRequest(), "78181331-1")
        self.assertEqual(bad.status, 400)

        session.post.side_effect = Exception("server error")
        err = await service.obtener_correo_intercambio(DummyRequest(), "78181331-1")
        self.assertEqual(err.status, 500)
