import unittest
from ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
from models.ResponseDTE import Response
import json
import aiohttp
from unittest.mock import AsyncMock, patch
from typing import List
from datetime import datetime
import requests_mock
from models.Productos.ProductoEnt import ProductoEnt
from models.GetFactura.Credenciales import Credenciales
from models.Productos.DatoExternoRequest import DatoExternoRequest
from models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from dotenv import load_dotenv
import os
import random

load_dotenv()

class TestProductoService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        username = os.getenv("SF_USERNAME")
        password = os.getenv("SF_PASSWORD")
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.Productos

    async def test_CrearProducto(self):
        producto_1_nombre = f"NomGoma_{random.randint(1, 1000)}"
        producto_1_codigo_barra = f"NomCB_{random.randint(1, 1000)}"
        
        producto_2_nombre = f"NomGoma2_{random.randint(1, 1000)}"
        producto_2_codigo_barra = f"NomCB2_{random.randint(1, 1000)}"

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

        response = await self.service.CrearProducto(solicitud)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)

    async def test_CrearProducto_BadRequest_WhenProductoExist(self):
        nombre_producto_1 = "Goma 785"
        nombre_producto_2 = "Goma 84"

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

        response = await self.service.CrearProducto(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)
        self.assertEqual(f"Ya existe un producto con el nombre {nombre_producto_1}", response.message)

    async def test_CrearProducto_ServerError(self):
        solicitud = DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="",
                nombre_sucursal=""
            )
        )
        with patch('aiohttp.ClientSession.post', new_callable=AsyncMock) as mock_post:
            mock_post.side_effect = Exception("Error al Crear Producto")

            response = await self.service.CrearProducto(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNotNone(response.message)
            self.assertEqual("Error al Crear Producto", response.message)

    async def test_listarProductos_ReturnOK(self):       
        solicitud= Credenciales(
            rut_emisor="76269769-6",
            nombre_sucursal="Casa Matriz"
        )

        response = await self.service.listarProductos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, list)
        for i, producto in enumerate(response.data):
            if i >= 5:
                break
            self.assertIsNotNone(producto.nombre)

    async def test_listarProductos_BadRequest(self):
        solicitud = Credenciales(
            rut_emisor="",
            nombre_sucursal=""
        )

        response = await self.service.listarProductos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNone(response.data)
        self.assertIsNotNone(response.message)     

    async def test_listarProductos_ServerError(self):
        solicitud = Credenciales(
            rut_emisor="",
            nombre_sucursal=""
        )
        with patch('aiohttp.ClientSession.post', new_callable=AsyncMock) as mock_post:
            mock_post.side_effect = Exception("Error al listar Productos")

            response = await self.service.listarProductos(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNotNone(response.message)
            self.assertEqual("Error al listar Productos", response.message)