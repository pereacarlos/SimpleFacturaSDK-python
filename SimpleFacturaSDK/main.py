from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
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
client_api = ClientSimpleFactura(username, password)
solicitud= SolicitudPdfDte(
    credenciales=Credenciales(
        rut_emisor="76269769-6",
        nombre_sucursal="Casa Matriz"
    ),
    dte_referenciado_externo=DteReferenciadoExterno(
        folio=4117,
        codigoTipoDte=33,
        ambiente=0
    )
)
try:
    # Guardar PDF
    # Guardar Timbre como imagen PNG
    timbre_response = client_api.Facturacion.obtener_timbre(solicitud)
    timbre_data = json.loads(timbre_response.data)
    with open("timbre.png", "wb") as f:
        f.write(base64.b64decode(timbre_data["data"]))


except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")