from ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
import json
import sys
import unittest
from models.ResponseDTE import Response
from models.GetFactura.Credenciales import Credenciales
from models.BoletaHonorarios.BHERequest import BHERequest
from models.BoletaHonorarios.ListaBHERequest import ListaBHERequest
from services.BoletaHonorarioService import BoletaHonorarioService
from datetime import datetime
from dotenv import load_dotenv
from unittest.mock import patch
import os
load_dotenv()

class TestBoletahonorarioService(unittest.TestCase):
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.BoletaHonorarioService


    def test_ObtenerPdf_ReturnOK(self):
        solicitud= BHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            Folio=15
        )
        response = self.service.ObtenerPdf(solicitud)
        self.assertTrue(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, bytes)

    def test_ObtenPdf_ReturnBadRequest(self):
        solicitud= BHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            Folio=0
        )
        response = self.service.ObtenerPdf(solicitud)
        self.assertTrue(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    def test_ObtenPdf_ReturnServeError(self):
        solicitud= BHERequest(
            credenciales=Credenciales(
                rut_emisor=""
            ),
            Folio=0
        )
        with patch('SimpleFacturaSDK.services.BoletaHonorarioService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"
            response = self.service.ObtenerPdf(solicitud)
            self.assertTrue(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)

    #Falta probarlo
    def test_ListadoBHEEmitidos_ReturnOK(self):
        fecha_desde = datetime.strptime("2024-09-03", "%Y-%m-%d").isoformat()
        fecha_hasta = datetime.strptime("2024-11-11", "%Y-%m-%d").isoformat()
        solicitud= ListaBHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Folio=None,
            Desde=fecha_desde,
            Hasta=fecha_hasta
        )

        response = self.service.ListadoBHEEmitidos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for i, bhe in enumerate(response.data):
            if i >= 3:
                break
            self.assertIsNotNone(bhe.folio)
            self.assertIsNotNone(bhe.fechaEmision)
            self.assertIsNotNone(bhe.codigoBarra)

    def test_ListadoBHEEmitidos_BadRequest(self):
        solicitud= ListaBHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Folio=None,
            Desde="",
            Hasta=""
        )
        response = self.service.ListadoBHEEmitidos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    def test_ListadoBHEEmitidos_ServerError(self):
        solicitud= ListaBHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Folio=None,
            Desde="",
            Hasta=""
        )
        with patch('SimpleFacturaSDK.services.BoletaHonorarioService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"
            response = self.service.ListadoBHEEmitidos(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
    #preguntar
    def test_ObtenerPdfBoletaRecibida_ReturnOK(self):
        solicitud= BHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente= "26429782-6"
            ),
            Folio=2
        )
        response = self.service.ObtenerPdfBoletaRecibida(solicitud)
        self.assertTrue(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, bytes)

    def test_ObtenerPdfBoletaRecibida_ReturnBadRequest(self):
        solicitud= BHERequest(
            credenciales=Credenciales(
                rut_emisor="",
                rut_contribuyente= "26429782-6"
            ),
            Folio=0
        )
        response = self.service.ObtenerPdfBoletaRecibida(solicitud)
        self.assertTrue(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    def test_ObtenerPdfBoletaRecibida_ReturnServerError(self):
        solicitud= BHERequest(
            credenciales=Credenciales(
                rut_emisor="",
                rut_contribuyente= "26429782-6"
            ),
            Folio=0
        )
        with patch('SimpleFacturaSDK.services.BoletaHonorarioService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"
            response = self.service.ObtenerPdfBoletaRecibida(solicitud)
            self.assertTrue(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)

    def test_ListadoBHERecibido_ReturnOK(self):
        fecha_desde = datetime.strptime("2024-09-03", "%Y-%m-%d").isoformat()
        fecha_hasta = datetime.strptime("2024-11-11", "%Y-%m-%d").isoformat()
        solicitud= ListaBHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Folio=None,
            Desde=fecha_desde,
            Hasta=fecha_hasta
        )

        response = self.service.ListadoBHERecibido(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for i, bhe in enumerate(response.data):
            if i >= 3:
                break
            self.assertIsNotNone(bhe.folio)
            self.assertIsNotNone(bhe.fechaEmision)

    def test_ListadoBHERecibido_BadRequest(self):
        solicitud= ListaBHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Folio=None,
            Desde="",
            Hasta=""
        )
        response = self.service.ListadoBHERecibido(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)

    def test_ListadoBHERecibido_ServerError(self):
        solicitud= ListaBHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Folio=None,
            Desde="",
            Hasta=""
        )
        with patch('SimpleFacturaSDK.services.BoletaHonorarioService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"
            response = self.service.ListadoBHERecibido(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)