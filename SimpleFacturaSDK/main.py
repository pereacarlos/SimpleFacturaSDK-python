
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura as APIClient
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.models.BoletaHonorarios.ListaBHERequest import ListaBHERequest
import json
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Sucursal import Sucursal
from datetime import datetime
fecha_desde = datetime.strptime("2024-09-03", "%Y-%m-%d").isoformat()
fecha_hasta = datetime.strptime("2024-11-11", "%Y-%m-%d").isoformat()
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)
solicitud= BHERequest(
    credenciales=Credenciales(
        rut_emisor="76269769-6",
        rut_contribuyente= "17096073-4"
    ),
    Folio=2
)
try:
    ObtenerPdfRecibida = client_api.BoletaHonorarioService.ObtenerPdfBoletaRecibida(solicitud)
    ruta = "BoletaHonorarioRecibida.pdf"
    with open(ruta, "wb") as archivo:
        archivo.write(ObtenerPdfRecibida)

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")
