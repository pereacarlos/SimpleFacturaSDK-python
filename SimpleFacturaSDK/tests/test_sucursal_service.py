import unittest
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import requests
import base64
from dotenv import load_dotenv
import aiohttp
from unittest.mock import AsyncMock, patch
import os
load_dotenv()

class TestSucursalService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        username = os.getenv("SF_USERNAME")
        password = os.getenv("SF_PASSWORD")
        self.client_api = await ClientSimpleFactura(username, password).__aenter__()
        self.service = self.client_api.Sucursales

    async def test_ListarSucursales_ReturnOK(self):
        solicitud= Credenciales(
            rut_emisor="76269769-6"
        )
        response = await self.service.ListarSucursales(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for i, sucursal in enumerate(response.data):
            if i >= 2:
                break
            self.assertIsNotNone(sucursal.nombre)
            self.assertIsNotNone(sucursal.direccion)

    async def test_ListarSucursales_BadRequest(self):
        solicitud= Credenciales(
            rut_emisor=""
        )
        response = await self.service.ListarSucursales(solicitud)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    async def test_ListarSucursales_ServeError(self):
        solicitud= Credenciales(
            rut_emisor="76269769-6"
        )
        with patch('aiohttp.ClientSession.post', new_callable=AsyncMock) as mock_post:
            mock_post.side_effect = Exception("Error al ListarSucursales")

            response = await self.service.ListarSucursales(solicitud)

            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500) 
            self.assertIsNone(response.data) 
            self.assertIsNotNone(response.message)
