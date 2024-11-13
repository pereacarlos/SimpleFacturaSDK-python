
from SimpleFacturaSDK.Base import APIClient
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
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

solicitud= BHERequest(
    credenciales=Credenciales(
        rut_emisor="76269769-6"
    ),
    Folio=15
)
try:
    ObtenerPdf = client_api.BoletaHonorarioService.ObtenerPdf(solicitud)
    ruta = "BoletaHonorario.pdf"
    with open(ruta, "wb") as archivo:
        archivo.write(ObtenerPdf)


except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")