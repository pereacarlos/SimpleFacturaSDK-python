import unittest
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
import requests
import base64
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from dotenv import load_dotenv
from unittest.mock import patch
import os
load_dotenv()

class TestSucursalService(unittest.TestCase):
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.Sucursales

    def test_ListarSucursales_ReturnOK(self):
        solicitud= Credenciales(
            rut_emisor="76269769-6"
        )
        response = self.service.ListarSucursales(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for i, sucursal in enumerate(response.data):
            if i >= 2:
                break
            self.assertIsNotNone(sucursal.nombre)
            self.assertIsNotNone(sucursal.direccion)

    def test_ListarSucursales_BadRequest(self):
        solicitud= Credenciales(
            rut_emisor=""
        )
        response = self.service.ListarSucursales(solicitud)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    def test_ListarSucursales_ServeError(self):
        solicitud= Credenciales(
            rut_emisor="76269769-6"
        )
        with patch('SimpleFacturaSDK.services.SucursalService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"

            response = self.service.ListarSucursales(solicitud)

            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500) 
            self.assertIsNone(response.data) 
            self.assertIsNotNone(response.message)
