from SimpleFacturaSDK.Base import APIClient
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
import json
#from requests.auth import HTTPBasicAuth
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Productos.DatoExternoRequest import DatoExternoRequest
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from datetime import datetime
fecha_desde = datetime.strptime("2024-04-01", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2024-04-30", "%Y-%m-%d")
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)
solicitud=Credenciales(rut_emisor="76269769-6")
try:
    Obtener_pdf = client_api.Proveedores.ConciliarRecibidos(solicitud,5,2024)
    print("\nDatos de la Respuesta:")
    print(f"Status: {Obtener_pdf.status}")
    print(f"Message: {Obtener_pdf.message}")
    print(f"Data: {Obtener_pdf.data}")
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")
