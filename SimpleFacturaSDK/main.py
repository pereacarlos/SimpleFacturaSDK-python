
from SimpleFacturaSDK.Base import APIClient
import base64
import json
from dataclasses import asdict
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
#from SimpleFacturaSDK.models.GetFactura.Dte import Dte
#from SimpleFacturaSDK.models.GetFactura.Documento import Documento  
#from SimpleFacturaSDK.models.GetFactura.Encabezado import Encabezado
#from SimpleFacturaSDK.models.GetFactura.IdentificacionDTE import IdentificacionDTE
#from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
#from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
#from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
#from SimpleFacturaSDK.models.GetFactura.Totales import Totales
#from SimpleFacturaSDK.models.GetFactura.Detalle import Detalle
#from SimpleFacturaSDK.models.GetFactura.CodigoItem import CodigoItem
#from datetime import datetime
#from dateutil.relativedelta import relativedelta
#from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
#from SimpleFacturaSDK.enumeracion.FormaPago import FormaPagoEnum

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
        folio=12553,
        codigo_tipo_dte=39,
        ambiente=0
    )
)
try: 
    sobre_xml_bytes = client_api.Facturacion.obtener_sobreXml(solicitud, 0)
    ruta = "sobre.xml"  # Ruta donde se guardará el sobre XML
    with open(ruta, "wb") as f:
        f.write(sobre_xml_bytes)
    print("El sobre XML se ha descargado correctamente.")




except Exception as ex:
    print(f"Error: {str(ex)}")
