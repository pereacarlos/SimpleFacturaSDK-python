from ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
import json
import unittest
from models.ResponseDTE import Response
from models.GetFactura.Credenciales import Credenciales
from dotenv import load_dotenv
from unittest.mock import patch
import os
load_dotenv()

class TestConfiguracionService(unittest.TestCase):
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.ConfiguracionService

    def test_DatosEmpresa_ReturnOK(self):
        solicitud= Credenciales(
            rut_emisor="76269769-6"
        )
        response = self.service.datos_empresa(solicitud)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.data.rut)
        self.assertIsNotNone(response.data.razonSocial)
        self.assertIsNotNone(response.data.giro)

    def test_DatosEmpresa_ReturnServerError(self):
        solicitud= Credenciales(
            rut_emisor=""
        )
       
        response = self.service.datos_empresa(solicitud)
        self.assertEqual(response.status, 500)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)







