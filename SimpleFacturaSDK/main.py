
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
        rut_emisor="76269769-6"
    ),
    dte_referenciado_externo=DteReferenciadoExterno(
        folio=2393,
        codigoTipoDte=33,
        ambiente=0
    )
)
try:
    sobre_xml_bytes = client_api.Facturacion.obtener_sobreXml(solicitud, "dsd")
    ruta = "sobre.xml"  # Ruta donde se guardará el sobre XML
    with open(ruta, "wb") as f:
        f.write(sobre_xml_bytes)
    print("El sobre XML se ha descargado correctamente.")


except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")

