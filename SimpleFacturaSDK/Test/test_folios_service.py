
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.Folios.TimbrajeEnt import TimbrajeEnt
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
from SimpleFacturaSDK.models.Folios.SolicitudFolios import SolicitudFolios
import json
import unittest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Sucursal import Sucursal
from dotenv import load_dotenv
from unittest.mock import patch
import os
load_dotenv()

class TestFoliosService(unittest.TestCase):
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.Folios


    def test_ConsultaFoliosDisponibles_ReturnOK(self):
        solicitud= SolicitudFolios(
            RutEmpresa="76269769-6",
            TipoDTE=33,
            Ambiente=0
        )
        response = self.service.ConsultaFoliosDisponibles(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)

    def test_ConsultarFoliosDisponibles_ReturnBadRequest(self):
        solicitud= SolicitudFolios(
            RutEmpresa="",
            TipoDTE=33,
            Ambiente=0
        )
        response = self.service.ConsultaFoliosDisponibles(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    def test_ConsultarFoliosDisponible_ReturnServerError(self):
        solicitud= SolicitudFolios(
            RutEmpresa="",
            TipoDTE=None,
            Ambiente=0
        )
        with patch('SimpleFacturaSDK.services.FolioService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"
            response = self.service.ConsultaFoliosDisponibles(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
            self.assertIsNotNone(response.message)

    def test_SolicitarFolios_ReturnOK(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            Cantidad= 3,
            CodigoTipoDte= DTEType.FacturaElectronica
        )
        response = self.service.SolicitarFolios(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)

    def test_SolicitarFolios_ReturnBadRequest(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "",
                nombre_sucursal = ""
            ),
            Cantidad= 3,
            CodigoTipoDte= DTEType.FacturaElectronica
        )
        response = self.service.SolicitarFolios(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    def test_SolicitarFolios_ReturnServerError(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            Cantidad= 3,
            CodigoTipoDte= DTEType.FacturaElectronica
        )
        with patch('SimpleFacturaSDK.services.FolioService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"
            response = self.service.SolicitarFolios(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
            self.assertIsNotNone(response.message)

    def test_ConsultarFolios_ReturnOK(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            CodigoTipoDte= None,
            Ambiente=0
        )

        response = self.service.ConsultarFolios(solicitud)
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

    def test_ConsultarFolios_ReturnBadRequest(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "",
                nombre_sucursal = ""
            ),
            CodigoTipoDte= None,
            Ambiente=0
        )
        response = self.service.ConsultarFolios(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    def test_ConsultarFolios_ReturnServerError(self):
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            CodigoTipoDte= None,
            Ambiente=0
        )
        with patch('SimpleFacturaSDK.services.FolioService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"
            response = self.service.ConsultarFolios(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
            self.assertIsNotNone(response.message)

    def test_Folios_Sin_Uso_ReturnOK(self):
        solicitud= SolicitudFolios(
            RutEmpresa = "76269769-6",
            TipoDTE = 33,
            Ambiente = 0
        )
        response = self.service.Folios_Sin_Uso(solicitud)
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

    def test_Folios_Sin_Uso_ReturnBadRequest(self):
        solicitud= SolicitudFolios(
            RutEmpresa = "",
            TipoDTE = 33,
            Ambiente = 0
        )
        response = self.service.Folios_Sin_Uso(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    def test_Folios_Sin_Uso_ReturnServerError(self):
        solicitud= SolicitudFolios(
            RutEmpresa = "76269769-6",
            TipoDTE = 33,
            Ambiente = 0
        )
        with patch('SimpleFacturaSDK.services.FolioService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"
            response = self.service.Folios_Sin_Uso(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNone(response.data)
            self.assertIsNotNone(response.message)



