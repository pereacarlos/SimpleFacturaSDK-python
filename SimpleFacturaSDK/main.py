
from SimpleFacturaSDK.Base import APIClient
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response

import json
#from requests.auth import HTTPBasicAuth
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Productos.DatoExternoRequest import DatoExternoRequest
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest


username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)

solicitud= DatoExternoRequest(
    Credenciales=Credenciales(
        rut_emisor="76269769-6",
        nombre_sucursal="Casa Matriz"
    ),
    Productos=[
        NuevoProductoExternoRequest(
            nombre="Goma 808",
            codigoBarra="Goma 808",
            unidadMedida="un",
            precio=50,
            exento=False,
            tieneImpuestos=False,
            impuestos=[ ]
        ),
        NuevoProductoExternoRequest(
            nombre="Goma 8009",
            codigoBarra="Goma 8009",
            unidadMedida="un",
            precio=50,
            exento=False,
            tieneImpuestos=True,
            impuestos=[ 271,23]
         
        )
    ]

)

try:

    addProducts = client_api.Productos.CrearProducto(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {addProducts.status}")
    print(f"Message: {addProducts.message}")
    for productos in addProducts.data:
        print(f"ProductoId: {productos.productoId}")
        print(f"Nombre: {productos.nombre}")
        print(f"Precio: {productos.precio}")
        print(f"Exento: {productos.exento}")
        print(f"Activo: {productos.activo}")
        print(f"EmisorId: {productos.emisorId}")
        print(f"SucursalId: {productos.sucursalId}")
        print(f"Impuestos: {productos.impuestos}")
        print(f"CodigoBarra: {productos.codigoBarra}")
        print(f"UnidadMedida: {productos.unidadMedida}")
        print(f"NombreCategoria: {productos.NombreCategoria}")
        print(f"NombreMarca: {productos.NombreMarca}")
        print(f"Stock: {productos.Stock}")
        print("\n")




except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")