from ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
from unittest.mock import patch
import unittest
from dotenv import load_dotenv
import os
import random
from enumeracion.TipoDTE import DTEType
from models.ResponseDTE import Response
from models.GetFactura.ListadoRequest import ListaDteRequestEnt
from enumeracion.Ambiente import AmbienteEnum
import json
from models.GetFactura.Credenciales import Credenciales
from models.Productos.DatoExternoRequest import DatoExternoRequest
from models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from datetime import datetime
load_dotenv()
fecha_desde = datetime.strptime("2024-04-01", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2024-04-30", "%Y-%m-%d")

class TestProveedorService(unittest.TestCase):
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.Proveedores

    def test_listarDteRecibidos(self):
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= None,
            codigoTipoDte=None,
            desde=fecha_desde,
            hasta=fecha_hasta,
        )

        response = self.service.listarDteRecibidos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        self.assertTrue(len(response.data) > 0)

    def test_listarDteRecibidos_BadRequest_WhenDataISInvalid(self):
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor=""
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= None,
            codigoTipoDte=None,
            desde=fecha_desde,
            hasta=fecha_hasta,
        )

        response = self.service.listarDteRecibidos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)

    def test_listarDteRecibidos_ServerError(self):
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= None,
            codigoTipoDte=None,
            desde=fecha_desde,
            hasta=fecha_hasta,
        )

        with patch('SimpleFacturaSDK.services.ProveedorService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"

            response = self.service.listarDteRecibidos(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
            self.assertIsNotNone(response.message)

    def test_obtenerXml_ReturnOK(self):
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente="96689310-9"
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= 7366834,
            codigoTipoDte=DTEType.NotaCreditoElectronica
        )
        response = self.service.obtenerXml(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        self.assertIsInstance(response.data, bytes)

    def test_obtenerXml_BadRequest_WhenDataISInvalid(self):
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente="96689310-9"
            )
        )
        response = self.service.obtenerXml(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)

    def test_obtenerXml_ServerError(self):
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="",
                rut_contribuyente=""
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= 0,
            codigoTipoDte=None
        )
        response = self.service.obtenerXml(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)

    def test_obtener_pdf_ReturnOK(self):
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente="76269769-6"
            ),
            ambiente=AmbienteEnum.Certificacion,
            folio= 2232,
            codigoTipoDte=DTEType.FacturaElectronica
        )
        response = self.service.obtener_pdf(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        self.assertIsInstance(response.data, bytes)

    def test_obtener_pdf_BadRequest_WhenDataISInvalid(self):
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente="76269769-6"
            )
        )
        response = self.service.obtener_pdf(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)

    def test_obtener_pdf_ServerError(self):
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="",
                rut_contribuyente=""
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= 0,
            codigoTipoDte=None
        )
        response = self.service.obtener_pdf(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)

    #pREGUNTAR
    def test_ConciliarRecibidos_ReturnOK(self):
        solicitud=Credenciales(rut_emisor="76269769-6")

        response = self.service.ConciliarRecibidos(solicitud,5,2024)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        self.assertIsInstance(response.data, str)
        
    def test_ConciliarRecibidos_BadRequest_WhenMesISInvalid(self):
        solicitud=Credenciales(rut_emisor="76269769-6")

        response = self.service.ConciliarRecibidos(solicitud,"5",2024)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)

    def test_ConciliarRecibidos_BadRequest_WhenAnioISInvalid(self):
        solicitud=Credenciales(rut_emisor="76269769-6")

        response = self.service.ConciliarRecibidos(solicitud,5,"2024")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)

    def test_ConciliarRecibidos_ServerError(self):
        solicitud=Credenciales(rut_emisor="76269769-k")

        response = self.service.ConciliarRecibidos(solicitud,5,2024)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)









