
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

solicitud= FolioRequest(
    credenciales=Credenciales(
        rut_emisor = "76269769-6",
        nombre_sucursal = "Casa Matriz"
    ),
    CodigoTipoDte= 33,
    Ambiente= 0

)
try:
    consultarFolio = client_api.Folios.ConsultarFolios(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {consultarFolio.status}")
    print(f"Message: {consultarFolio.message}")
    print(f"Data: {consultarFolio.data}")
    for data in consultarFolio.data:
        print(f"codigoSii: {data.codigoSii}")
        print(f"fechaIngreso: {data.fechaIngreso}")
        print(f"desde: {data.desde}")
        print(f"hasta: {data.hasta}")
   

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")