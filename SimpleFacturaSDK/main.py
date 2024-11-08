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
        rut_emisor="76269769-6"
    ),
    dte_referenciado_externo=DteReferenciadoExterno(
        folio=2963,
        codigo_tipo_dte=33,
        ambiente=0
    )
)
try: 
 
    #OBTENER SOBREXML
    xml = client_api.Facturacion.obtener_sobreXml(solicitud, sobre=0)
    ruta = "sobre.xml"
    with open(ruta, "wb") as file:
        file.write(xml)
    print(f"Archivo guardado en {ruta}")

except Exception as ex:
    print(f"Error: {str(ex)}")



