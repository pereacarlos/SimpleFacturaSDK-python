import json
import unittest

from SimpleFacturaSDK.enumeracion.ListaProveedorEnum import ListaProveedorEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Proveedores.AgregarProveedorExternoRequest import AgregarProveedorExternoRequest
from SimpleFacturaSDK.models.Proveedores.EditarProveedorRequest import EditarProveedorRequest
from SimpleFacturaSDK.models.Proveedores.ListarProveedoresRequest import ListarProveedoresRequest
from SimpleFacturaSDK.models.Proveedores.ProveedorExternoEnt import (
    EditarProveedorExternoEnt,
    NuevoProveedorExternoEnt,
)
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


def proveedor_payload():
    return {
        "rut": "12345678-9",
        "razonSocial": "Empresa Proveedor SpA",
        "giro": "Servicios de Tecnología",
        "dirFact": "Av. Providencia 1234, Of. 5",
        "correoPar": "contacto@proveedor.cl",
        "ciudad": "Santiago",
        "comuna": "Providencia",
        "correoFact": "dte@proveedor.cl",
        "listaProveedor": "ListaBlanca",
        "activo": True,
    }


class TestProveedorService(unittest.IsolatedAsyncioTestCase):
    async def test_ListarProveedores_Ok(self):
        service, session, client = make_service(ProveedorService)
        payload = {"status": 200, "message": "ok", "data": [proveedor_payload()]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )

        solicitud = ListarProveedoresRequest(RutEmisor="76354771-K")
        response = await service.ListarProveedores(solicitud)

        client.ensure_token_valid.assert_awaited_once()
        session.post.assert_called_once_with(
            "https://api.test/list/proveedores",
            json={"RutEmisor": "76354771-K"},
        )
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].rut, "12345678-9")
        self.assertEqual(response.data[0].listaProveedor, "ListaBlanca")

    async def test_ListarProveedores_BadRequest(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=400, text_data='{"errors":["rut invalido"]}')
        )

        response = await service.ListarProveedores(ListarProveedoresRequest(RutEmisor="76354771-K"))

        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    async def test_ListarProveedores_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")

        response = await service.ListarProveedores(ListarProveedoresRequest(RutEmisor="76354771-K"))

        self.assertEqual(response.status, 500)

    async def test_AgregarProveedores_Ok(self):
        service, session, client = make_service(ProveedorService)
        payload = {"status": 200, "message": "creado", "data": [proveedor_payload()]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        solicitud = AgregarProveedorExternoRequest(
            Credenciales=Credenciales(rut_emisor="76354771-K"),
            Proveedores=[
                NuevoProveedorExternoEnt(
                    Rut="12345678-9",
                    RazonSocial="Empresa Proveedor SpA",
                    Giro="Servicios de Tecnología",
                    DirFact="Av. Providencia 1234, Of. 5",
                    CorreoPar="contacto@proveedor.cl",
                    Ciudad="Santiago",
                    Comuna="Providencia",
                    CorreoFact="dte@proveedor.cl",
                    ListaProveedor=ListaProveedorEnum.ListaBlanca,
                )
            ],
        )

        response = await service.AgregarProveedores(solicitud)

        client.ensure_token_valid.assert_awaited_once()
        session.post.assert_called_once_with(
            "https://api.test/addProveedores",
            json={
                "Credenciales": {"RutEmisor": "76354771-K"},
                "Proveedores": [
                    {
                        "Rut": "12345678-9",
                        "RazonSocial": "Empresa Proveedor SpA",
                        "Giro": "Servicios de Tecnología",
                        "DirFact": "Av. Providencia 1234, Of. 5",
                        "CorreoPar": "contacto@proveedor.cl",
                        "Ciudad": "Santiago",
                        "Comuna": "Providencia",
                        "CorreoFact": "dte@proveedor.cl",
                        "ListaProveedor": 2,
                    }
                ],
            },
        )
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].razonSocial, "Empresa Proveedor SpA")

    async def test_AgregarProveedores_Conflict(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=409, text_data='{"errors":["proveedor ya existe"]}')
        )

        response = await service.AgregarProveedores(DummyRequest())

        self.assertEqual(response.status, 409)
        self.assertIsNone(response.data)

    async def test_AgregarProveedores_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")

        response = await service.AgregarProveedores(DummyRequest())

        self.assertEqual(response.status, 500)

    async def test_EditarProveedores_Ok(self):
        service, session, client = make_service(ProveedorService)
        payload = {"status": 200, "message": "actualizado", "data": [proveedor_payload()]}
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=200, text_data=json.dumps(payload))
        )
        solicitud = EditarProveedorRequest(
            Credenciales=Credenciales(
                rut_emisor="76354771-K",
                email_usuario="usuario@empresa.cl",
            ),
            Proveedores=[
                EditarProveedorExternoEnt(
                    Rut="12345678-9",
                    RazonSocial="Empresa Proveedor SpA Actualizada",
                    Giro="Consultoría TI",
                    DirFact=None,
                    CorreoPar="nuevo@proveedor.cl",
                    Ciudad=None,
                    Comuna=None,
                    CorreoFact=None,
                    ListaProveedor=ListaProveedorEnum.ListaNegra,
                )
            ],
        )

        response = await service.EditarProveedores(solicitud)

        client.ensure_token_valid.assert_awaited_once()
        session.post.assert_called_once_with(
            "https://api.test/editProveedores",
            json={
                "Credenciales": {
                    "RutEmisor": "76354771-K",
                    "EmailUsuario": "usuario@empresa.cl",
                },
                "Proveedores": [
                    {
                        "Rut": "12345678-9",
                        "RazonSocial": "Empresa Proveedor SpA Actualizada",
                        "Giro": "Consultoría TI",
                        "DirFact": None,
                        "CorreoPar": "nuevo@proveedor.cl",
                        "Ciudad": None,
                        "Comuna": None,
                        "CorreoFact": None,
                        "ListaProveedor": 1,
                    }
                ],
            },
        )
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data[0].correoPar, "contacto@proveedor.cl")

    async def test_EditarProveedores_Unauthorized(self):
        service, session, _ = make_service(ProveedorService)
        session.post.return_value = MockRequestContext(
            MockAiohttpResponse(status=401, text_data='{"errors":["credenciales incorrectas"]}')
        )

        response = await service.EditarProveedores(DummyRequest())

        self.assertEqual(response.status, 401)
        self.assertIsNone(response.data)

    async def test_EditarProveedores_ServerError(self):
        service, session, _ = make_service(ProveedorService)
        session.post.side_effect = Exception("server error")

        response = await service.EditarProveedores(DummyRequest())

        self.assertEqual(response.status, 500)

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
