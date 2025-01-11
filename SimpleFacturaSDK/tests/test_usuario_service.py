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

class TestUsuarioService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        username = os.getenv("SF_USERNAME")
        password = os.getenv("SF_PASSWORD")
        self.client_api = await ClientSimpleFactura(username, password).__aenter__()
        self.service = self.client_api.Usuarios

    async def test_ListarUsuarios_ReturnOK(self):
        solicitud= Credenciales(
            rut_emisor="76269769-6"
        )
        response = await self.service.ListarUsuario(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for i, usuario in enumerate(response.data):
            if i >= 2:
                break
            self.assertIsNotNone(usuario.rut)
            self.assertIsNotNone(usuario.nombre)
            self.assertIsNotNone(usuario.apellidos)
            self.assertIsNotNone(usuario.email)
           
    async def test_ListarUsuarios_BadRequest(self):
        solicitud= Credenciales(
            rut_emisor=""
        )
        response = await self.service.ListarUsuario(solicitud)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    async def test_ListarUsuarios_ServeError(self):
        solicitud= Credenciales(
            rut_emisor="76269769-6"
        )
        with patch('aiohttp.ClientSession.post', new_callable=AsyncMock) as mock_post:
            mock_post.side_effect = Exception("Error al ListarUsuarios")

            response = await self.service.ListarUsuario(solicitud)

            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500) 
            self.assertIsNone(response.data) 
            self.assertIsNotNone(response.message)
