
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.models.BoletaHonorarios.ListaBHERequest import ListaBHERequest
import json
#from requests.auth import HTTPBasicAuth
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Sucursal import Sucursal
from datetime import datetime
fecha_desde = datetime.strptime("2024-09-03", "%Y-%m-%d").isoformat()
fecha_hasta = datetime.strptime("2024-11-11", "%Y-%m-%d").isoformat()
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = ClientSimpleFactura(username, password)
solicitud= ListaBHERequest(
    credenciales=Credenciales(
        rut_emisor="76269769-6",
        nombre_sucursal="Casa Matriz"
    ),
    Folio=None,
    Desde=fecha_desde,
    Hasta=fecha_hasta
)
try:
    ListadoBHERecibido = client_api.BoletaHonorarioService.ListadoBHERecibido(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {ListadoBHERecibido.status}")
    print(f"Message: {ListadoBHERecibido.message}")
    for cliente in ListadoBHERecibido.data:
        print(f"fOLIO: {cliente.folio}")
        print(f"FECHAEMISION: {cliente.fechaEmision}")
        print("\n")     

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")
