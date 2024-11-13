
from SimpleFacturaSDK.Base import APIClient
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.Folios.SolicitudFolios import SolicitudFolios
from SimpleFacturaSDK.models.Folios.TimbrajeEnt import TimbrajeEnt
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
import json
#from requests.auth import HTTPBasicAuth
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Sucursal import Sucursal
from datetime import datetime
fecha_desde = datetime.strptime("2024-04-01", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2024-04-30", "%Y-%m-%d")
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)

solicitud= Credenciales(
    rut_emisor="76269769-6"
)
try:
    DatosEmpresa = client_api.ConfiguracionService.datos_empresa(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {DatosEmpresa.status}")
    print(f"Message: {DatosEmpresa.message}")
    print(f"Data: {DatosEmpresa.data}")
    print(f"rut: {DatosEmpresa.data.rut}")
    print(f"razonSocial: {DatosEmpresa.data.razonSocial}")
    print(f"giro: {DatosEmpresa.data.giro}")
   

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")