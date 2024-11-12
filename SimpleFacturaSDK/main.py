
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
            nombre="Goma 998",
            codigoBarra="Goma 998",
            unidadMedida="un",
            precio=50,
            exento=False,
            tieneImpuestos=False,
            impuestos=[ 271,23]
        ),
        NuevoProductoExternoRequest(
            nombre="Goma 999",
            codigoBarra="Goma 999",
            unidadMedida="un",
            precio=50,
            exento=False,
            tieneImpuestos=True,
            impuestos=[0]
        )
    ]

)

try:

    addProducts = client_api.Productos.CrearProducto(solicitud)

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")