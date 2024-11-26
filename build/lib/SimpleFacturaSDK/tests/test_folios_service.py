
from client_simple_factura import ClientSimpleFactura
import base64
import requests
from models.ResponseDTE import Response
from models.GetFactura.ListadoRequest import ListaDteRequestEnt
from enumeracion.Ambiente import AmbienteEnum
from enumeracion.TipoDTE import DTEType
from models.Folios.TimbrajeEnt import TimbrajeEnt
from models.Folios.Foliorequest import FolioRequest
from models.Folios.SolicitudFolios import SolicitudFolios
import json
import unittest
from models.GetFactura.Credenciales import Credenciales
from models.Sucursal import Sucursal
from dotenv import load_dotenv
import aiohttp
from unittest.mock import AsyncMock, patch
import os
load_dotenv()

class TestFoliosService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        username = os.getenv("SF_USERNAME")
        password = os.getenv("SF_PASSWORD")
        self.client_api = await ClientSimpleFactura(username, password).__aenter__()
        self.service = self.client_api.Folios


    async def test_ConsultaFoliosDisponibles_ReturnOK(self):
        solicitud= SolicitudFolios(
            RutEmpresa="76269769-6",
            TipoDTE=33,
            Ambiente=0
        )
        response = await self.service.ConsultaFoliosDisponibles(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)

    async def test_ConsultarFoliosDisponibles_ReturnBadRequest(self):
        solicitud= SolicitudFolios(
            RutEmpresa="",
            TipoDTE=33,
            Ambiente=0
        )
        response = await self.service.ConsultaFoliosDisponibles(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    async def test_ConsultarFoliosDisponible_ReturnServerError(self):
        solicitud= SolicitudFolios(
            RutEmpresa="",
            TipoDTE=None,
            Ambiente=0
        )
        with patch('aiohttp.ClientSession.post', new_callable=AsyncMock) as mock_post:
            mock_post.side_effect = Exception("Error al ConsultarFoliosDisponibles")

            response = await self.service.ConsultaFoliosDisponibles(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
            self.assertIsNotNone(response.message)
            self.assertEqual("Error al ConsultarFoliosDisponibles", response.message)

    async def test_SolicitarFolios_ReturnOK(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            Cantidad= 3,
            CodigoTipoDte= DTEType.BoletaElectronica
        )
        response = await self.service.SolicitarFolios(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)

    async def test_SolicitarFolios_ReturnBadRequest(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "",
                nombre_sucursal = ""
            ),
            Cantidad= 3,
            CodigoTipoDte= DTEType.FacturaElectronica
        )
        response = await self.service.SolicitarFolios(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    async def test_SolicitarFolios_ReturnServerError(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            Cantidad= 3,
            CodigoTipoDte= DTEType.FacturaElectronica
        )
        with patch('aiohttp.ClientSession.post', new_callable=AsyncMock) as mock_post:
            mock_post.side_effect = Exception("Error al SolicitarFolios")

            response = await self.service.SolicitarFolios(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
            self.assertIsNotNone(response.message)
            self.assertEqual("Error al SolicitarFolios", response.message)

    async def test_ConsultarFolios_ReturnOK(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            CodigoTipoDte= None,
            Ambiente=0
        )

        response = await self.service.ConsultarFolios(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        for i, folio in enumerate(response.data):
            if i >= 3:
                break
            self.assertIsNotNone(folio.foliosDisponibles)
            self.assertIsNotNone(folio.codigoSii)
            self.assertIsNotNone(folio.fechaIngreso)
            self.assertIsNotNone(folio.desde)
            self.assertIsNotNone(folio.hasta)

    async def test_ConsultarFolios_ReturnBadRequest(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "",
                nombre_sucursal = ""
            ),
            CodigoTipoDte= None,
            Ambiente=0
        )
        response = await self.service.ConsultarFolios(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    async def test_ConsultarFolios_ReturnServerError(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            CodigoTipoDte= None,
            Ambiente=0
        )
        with patch('aiohttp.ClientSession.post', new_callable=AsyncMock) as mock_post:
            mock_post.side_effect = Exception("Error al ConsultarFolios")

            response = await self.service.ConsultarFolios(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
            self.assertIsNotNone(response.message)
            self.assertEqual("Error al ConsultarFolios", response.message)

    async def test_Folios_Sin_Uso_ReturnOK(self):
        solicitud= SolicitudFolios(
            RutEmpresa = "76269769-6",
            TipoDTE = 33,
            Ambiente = 0
        )
        response = await self.service.Folios_Sin_Uso(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        for i, folio in enumerate(response.data):
            if i >= 3:
                break
            self.assertIsNotNone(folio.desde)
            self.assertIsNotNone(folio.hasta)
            self.assertIsNotNone(folio.cantidad)

    async def test_Folios_Sin_Uso_ReturnBadRequest(self):
        solicitud= SolicitudFolios(
            RutEmpresa = "",
            TipoDTE = 33,
            Ambiente = 0
        )
        response = await self.service.Folios_Sin_Uso(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    async def test_Folios_Sin_Uso_ReturnServerError(self):
        solicitud= SolicitudFolios(
            RutEmpresa = "76269769-6",
            TipoDTE = 33,
            Ambiente = 0
        )
        with patch('aiohttp.ClientSession.post', new_callable=AsyncMock) as mock_post:
            mock_post.side_effect = Exception("Error al ConsultarFoliosSinUso")
            response = await self.service.Folios_Sin_Uso(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
            self.assertIsNotNone(response.message)
            self.assertEqual("Error al ConsultarFoliosSinUso", response.message)



