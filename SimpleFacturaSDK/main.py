from SimpleFacturaSDK.Base import APIClient
import base64
import json
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte

#import sys
#import os
#sys.path.append(os.path.abspath("c:/SimpleFacturaSDK-python/SimpleFacturaSDK"))

    # Datos de autenticación
username = "demo@chilesystems.com"
password = "Rv8Il4eV"

# Crear instancia del cliente API
client_api = APIClient(username, password)

solicitud = SolicitudPdfDte(
    credenciales=Credenciales(
        rut_emisor="76269769-6",
        nombre_sucursal="Casa Matriz"
    ),
    dte_referenciado_externo=DteReferenciadoExterno(
        folio=4117,
        codigo_tipo_dte=33,
        ambiente=0
    )
)
try: 
    # Obtener PDF
    pdf = client_api.Facturacion.obtener_pdf(solicitud)
    # Guardar PDF
    with open("factura.pdf", "wb") as file:
        file.write(pdf)
    print("PDF guardado exitosamente", pdf)
except Exception as ex:
    print(f"Error: {str(ex)}")



