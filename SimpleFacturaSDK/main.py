
from SimpleFacturaSDK.Base import APIClient
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
import json
from datetime import datetime
fecha_desde = datetime.strptime("2024-09-03", "%Y-%m-%d").isoformat()
fecha_hasta = datetime.strptime("2024-11-11", "%Y-%m-%d").isoformat()
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)

solicitud= SolicitudPdfDte(
    credenciales=Credenciales(
        rut_emisor="76269769-6",
        nombre_sucursal="Casa Matriz"
    ),
    dte_referenciado_externo=DteReferenciadoExterno(
        Folio=4117,
        CodigoTipoDte=33,
        Ambiente=0
    )
)

try:
    # Guardar PDF
    Timbre = client_api.Facturacion.obtener_timbre(solicitud)
    Timbre_data = json.loads(Timbre)
    if 'data' in Timbre_data:
        timbre_base64 = Timbre_data['data']
        timbre = base64.b64decode(timbre_base64)
        with open("timbre.png", "wb") as file:
            file.write(timbre)
        print("Timbre obtenido correctamente", timbre_base64)   
    else:
        print("Error al obtener timbre")


except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")