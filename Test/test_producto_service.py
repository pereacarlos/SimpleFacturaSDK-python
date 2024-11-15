import unittest
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
import json
from typing import List
from unittest.mock import patch
from datetime import datetime
import requests_mock
from SimpleFacturaSDK.models.Productos.ProductoEnt import ProductoEnt
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Productos.DatoExternoRequest import DatoExternoRequest
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from dotenv import load_dotenv
import os
import random

load_dotenv()

class TestProductoService(unittest.TestCase):
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.Productos
        self.service_folios = self.client_api.Folios

    def test_CrearProducto(self):
        producto_1_nombre = f"NombreGoma_{random.randint(1, 1000)}"
        producto_1_codigo_barra = f"NombreCB_{random.randint(1, 1000)}"
        
        producto_2_nombre = f"NombreGoma2_{random.randint(1, 1000)}"
        producto_2_codigo_barra = f"NombreCB2_{random.randint(1, 1000)}"

        solicitud = DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Productos=[
                NuevoProductoExternoRequest(
                    nombre=producto_1_nombre,
                    codigoBarra=producto_1_codigo_barra,
                    unidadMedida="un",
                    precio=50,
                    exento=False,
                    tieneImpuestos=False,
                    impuestos=[0]
                ),
                NuevoProductoExternoRequest(
                    nombre=producto_2_nombre,
                    codigoBarra=producto_2_codigo_barra,
                    unidadMedida="un",
                    precio=50,
                    exento=False,
                    tieneImpuestos=True,
                    impuestos=[271, 23]
                )
            ]
        )

        response = self.service.CrearProducto(solicitud)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for producto in response.data:
            self.assertIsNotNone(producto.nombre)
            self.assertIsNotNone(producto.codigoBarra)
            self.assertIsNotNone(producto.unidadMedida)
            self.assertIsNotNone(producto.productoId)

    def test_CrearProducto_BadRequest_WhenProductoExist(self):
        nombre_producto_1 = "Goma 500000"
        nombre_producto_2 = "Goma 500001"

        solicitud = DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Productos=[
                NuevoProductoExternoRequest(
                    nombre=nombre_producto_1,
                    codigoBarra=nombre_producto_1,
                    unidadMedida="un",
                    precio=50,
                    exento=False,
                    tieneImpuestos=False,
                    impuestos=[0]
                ),
                NuevoProductoExternoRequest(
                    nombre=nombre_producto_2,
                    codigoBarra=nombre_producto_2,
                    unidadMedida="un",
                    precio=50,
                    exento=False,
                    tieneImpuestos=True,
                    impuestos=[271, 23]
                )
            ]
        )

        response = self.service.CrearProducto(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)
        self.assertIn(f"Ya existe un producto con el nombre {nombre_producto_1}", response.message)

    def test_CrearProducto_ServerError(self):
        solicitud = DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="",
                nombre_sucursal=""
            )
        )
        with patch('SimpleFacturaSDK.services.ProductoService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"

            response = self.service.CrearProducto(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNotNone(response.message)
            self.assertIn("Internal Server Error", response.message)

    def test_listarProductos_ReturnOK(self):       
        solicitud= Credenciales(
            rut_emisor="76269769-6",
            nombre_sucursal="Casa Matriz"
        )

        response = self.service.listarProductos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for i, producto in enumerate(response.data):
            if i >= 5:
                break
            self.assertIsNotNone(producto.nombre)

    def test_listarProductos_BadRequest(self):
        solicitud = Credenciales(
            rut_emisor="",
            nombre_sucursal=""
        )

        response = self.service.listarProductos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)     

    def test_listarProductos_ServerError(self):
        solicitud = Credenciales(
            rut_emisor="",
            nombre_sucursal=""
        )
        with patch('SimpleFacturaSDK.services.ProductoService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Internal Server Error"

            response = self.service.listarProductos(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNotNone(response.message)
            self.assertIn("Internal Server Error", response.message)