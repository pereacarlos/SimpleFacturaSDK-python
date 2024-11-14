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
        rut_emisor="",
        nombre_sucursal="Casa Matriz"
    ),
    dte_referenciado_externo=DteReferenciadoExterno(
        folio=None,
        codigoTipoDte=33,
        ambiente=0
    )
)
try:
    
    pdf = client_api.Facturacion.obtener_pdf(solicitud)
    # Guardar PDF
    with open("factura.pdf", "wb") as file:
        file.write(pdf)
    print("PDF guardado exitosamente", pdf)

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")
