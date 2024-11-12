
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

solicitud= Credenciales(
    rut_emisor="76269769-6",
    nombre_sucursal="Casa Matriz"
)

try:

    ListProduct = client_api.Productos.listarProductos(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {ListProduct.status}")
    print(f"Message: {ListProduct.message}")
    for i in ListProduct.data:
        print(f"productoId: {i.productoId}")
        print(f"nombre: {i.nombre}")
        print(f"precio: {i.precio}")
        print(f"exento: {i.exento}")
        for imp in i.impuestos:
            print(f"codigoSii: {imp.codigoSii}")
            print(f"nombreImp: {imp.nombreImp}")
            print(f"tasa: {imp.tasa}")
 
    




except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")