import unittest
from ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
from models.ResponseDTE import Response
from models.GetFactura.ListadoRequest import ListaDteRequestEnt
from enumeracion.Ambiente import AmbienteEnum
from enumeracion.TipoDTE import DTEType
import json
from dotenv import load_dotenv
from unittest.mock import patch
import os
from models.GetFactura.Credenciales import Credenciales
from models.Productos.DatoExternoRequest import DatoExternoRequest
from models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from models.Clientes.NuevoReceptorExternoRequest import NuevoReceptorExternoRequest
load_dotenv()

class TestClientesService(unittest.TestCase):
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.Clientes

    def test_CrearClientes_ReturnOK(self):
        solicitud= DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Clientes=[
                NuevoReceptorExternoRequest(
                    Rut="57681892-0",
                    RazonSocial="Cliente Test 1",
                    Giro="Giro 1",
                    DirPart="direccion 1",
                    DirFact="direccion 1",
                    CorreoPar="correo 1",
                    CorreoFact="correo 1",
                    Ciudad="Ciudad 1",
                    Comuna="Comuna 1"
                ),
                NuevoReceptorExternoRequest(
                    Rut="56516677-8",
                    RazonSocial="Cliente Test 2",
                    Giro="Giro 2",
                    DirPart="direccion 2",
                    DirFact="direccion 2",
                    CorreoPar="correo 2",
                    CorreoFact="correo 2",
                    Ciudad="Ciudad 2",
                    Comuna="Comuna 2"
                ),
                NuevoReceptorExternoRequest(
                    Rut="68959276-7",
                    RazonSocial="Cliente Test 3",
                    Giro="Giro 3",
                    DirPart="direccion 3",
                    DirFact="direccion 3",
                    CorreoPar="correo 3",
                    CorreoFact="correo 3",
                    Ciudad="Ciudad 3",
                    Comuna="Comuna 3"
                )
            ]
        )
        response = self.service.CrearClientes(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for i, cliente in enumerate(response.data):
            if i >= 3:
                break
            formatted_rut = f"{cliente.rut}-{cliente.dv}"
            self.assertEqual(formatted_rut, solicitud.Clientes[i].Rut)
            self.assertIsNotNone(cliente.receptorId)
            self.assertIsNotNone(cliente.giro)
            self.assertIsNotNone(cliente.emisorId)

    def test_CrearClientes_BadRequest(self):

        solicitud = DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="",
                nombre_sucursal="Casa Matriz"
            ),
            Clientes=[
                NuevoReceptorExternoRequest(
                    Rut="", 
                    RazonSocial="", 
                    Giro="",
                    DirPart="",
                    DirFact="",
                    CorreoPar="", 
                    CorreoFact="",
                    Ciudad="",
                    Comuna="" 
                )
            ]
        )

        response = self.service.CrearClientes(solicitud)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    def test_CrearClientes_ServerError(self):

        solicitud = DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor= "76269769-6",
                nombre_sucursal= "Matriz"
            )
        )
        with patch('SimpleFacturaSDK.services.ClientesService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"

            response = self.service.CrearClientes(solicitud)

            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500) 
            self.assertIsNone(response.data) 
            self.assertIsNotNone(response.message)

    def test_ListarClientes_ReturnOK(self):
        solicitud= Credenciales(rut_emisor="76269769-6")

        response = self.service.ListarClientes(solicitud)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for i, cliente in enumerate(response.data):
            if i >= 3:
                break
            self.assertIsNotNone(cliente.receptorId)
            self.assertIsNotNone(cliente.giro)
            self.assertIsNotNone(cliente.emisorId)

    def test_ListarClientes_BadRequest(self):
            
        solicitud = Credenciales(rut_emisor="")

        response = self.service.ListarClientes(solicitud)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400) 
        self.assertIsNone(response.data) 
        self.assertIsNotNone(response.message)

    def test_ListarClientes_ServerError(self):
            
        solicitud = Credenciales(rut_emisor="76269769-6")

        with patch('SimpleFacturaSDK.services.ClientesService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"

            response = self.service.ListarClientes(solicitud)

            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500) 
            self.assertIsNone(response.data) 
            self.assertIsNotNone(response.message)



