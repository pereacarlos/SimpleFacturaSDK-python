import json
import os
import tempfile
import unittest

from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.services.ConfiguracionService import ConfiguracionService
from SimpleFacturaSDK.tests.mock_utils import (
    DummyRequest,
    MockAiohttpResponse,
    MockRequestContext,
    make_service,
)


class TestConfiguracionService(unittest.IsolatedAsyncioTestCase):
    async def test_datos_empresa_Ok(self):
        service, session, client = make_service(ConfiguracionService)
        payload = {
            "status": 200,
            "data": {
                "rut": "78181331-1",
                "razonSocial": "CHILESYSTEMS SPA",
                "giro": "Servicios TI",
                "correoFact": "facturacion@chilesystems.cl",
                "comuna": "Santiago",
                "nroResol": 1,
                "fechaResol": "2026-01-01",
                "ambiente": 0,
                "telefono": 12345678,
                "rutRepresentanteLegal": "11111111-1",
                "actividadesEconomicas": [],
            },
        }
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )

        response = await service.datos_empresa(DummyRequest())

        client.ensure_token_valid.assert_awaited_once()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data.rut, "78181331-1")

    async def test_datos_empresa_BadRequest(self):
        service, session, _ = make_service(ConfiguracionService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["bad request"]}')
        )
        response = await service.datos_empresa(DummyRequest())
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_datos_empresa_ServerError(self):
        service, session, _ = make_service(ConfiguracionService)
        session.post.side_effect = Exception("server error")
        response = await service.datos_empresa(DummyRequest())
        self.assertEqual(response.status, 500)

    async def test_subir_certificado_digital_Ok(self):
        service, session, _ = make_service(ConfiguracionService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data='{"status":200}')
        )
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pfx") as tmp:
            tmp.write(b"binary")
            cert_path = tmp.name
        try:
            response = await service.subir_Certificado_Digital(
                Credenciales(rut_emisor="78181331-1"), cert_path
            )
        finally:
            os.remove(cert_path)
        self.assertEqual(response.status, 200)
        self.assertTrue(response.data)

    async def test_subir_certificado_digital_BadRequest(self):
        service, _, _ = make_service(ConfiguracionService)
        response = await service.subir_Certificado_Digital(
            Credenciales(rut_emisor="78181331-1"), "no-existe.pfx"
        )
        self.assertEqual(response.status, 400)
        self.assertFalse(response.data)

    async def test_subir_certificado_digital_ServerError(self):
        service, session, _ = make_service(ConfiguracionService)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pfx") as tmp:
            tmp.write(b"binary")
            cert_path = tmp.name
        try:
            session.post.side_effect = Exception("server error")
            response = await service.subir_Certificado_Digital(
                Credenciales(rut_emisor="78181331-1"), cert_path
            )
        finally:
            os.remove(cert_path)
        self.assertEqual(response.status, 500)
        self.assertFalse(response.data)
