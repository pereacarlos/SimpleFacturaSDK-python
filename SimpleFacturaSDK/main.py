
from SimpleFacturaSDK.Base import APIClient
import base64
import json
from dataclasses import asdict
#from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
#from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
#from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
from SimpleFacturaSDK.models.GetFactura.Dte import Dte
from SimpleFacturaSDK.models.GetFactura.Documento import Documento  
from SimpleFacturaSDK.models.GetFactura.Encabezado import Encabezado
from SimpleFacturaSDK.models.GetFactura.IdentificacionDTE import IdentificacionDTE
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.models.GetFactura.Totales import Totales
from SimpleFacturaSDK.models.GetFactura.Detalle import Detalle
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CodigoItem
from datetime import datetime
from dateutil.relativedelta import relativedelta
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
from SimpleFacturaSDK.enumeracion.FormaPago import FormaPagoEnum

    # Datos de autenticación
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
# Crear instancia del cliente API
client_api = APIClient(username, password)
solicitud = RequestDTE(
    Documento=Documento(
        Encabezado=Encabezado(
            IdDoc=IdentificacionDTE(
                TipoDTE=33,
                FchEmis="2024-09-05",
                FmaPago=1,
                FchVenc="2024-09-05"
            ),
            Emisor=Emisor(
                RUTEmisor="76269769-6",
                RznSoc="SERVICIOS INFORMATICOS CHILESYSTEMS EIRL",
                GiroEmis="Desarrollo de software",
                Telefono=["912345678"],
                CorreoEmisor="mvega@chilesystems.com",
                Acteco=[620200],
                DirOrigen="Calle 7 numero 3",
                CmnaOrigen="Santiago",
                CiudadOrigen="Santiago"
            ),
            Receptor=Receptor(
                RUTRecep="17096073-4",
                RznSocRecep="Hotel Iquique",
                GiroRecep="test",
                CorreoRecep="mvega@chilesystems.com",
                DirRecep="calle 12",
                CmnaRecep="Paine",
                CiudadRecep="Santiago"
            ),
            Totales=Totales(
                MntNeto=832.0,
                TasaIVA=19.0,
                IVA=158.0,
                MntTotal=990.0
            )
        ),
        Detalle=[
            Detalle(
                NroLinDet=1,
                NmbItem="Alfajor",
                CdgItem=[
                    CodigoItem(
                        TpoCodigo="ALFA",
                        VlrCodigo="123"
                    )
                ],
                QtyItem=1,
                UnmdItem="un",
                PrcItem=831.932773,
                MontoItem=832
            )
        ]
    ),
    Observaciones="NOTA AL PIE DE PAGINA",
    TipoPago="30 dias"
)
try: 
    # Obtener la factura
    solicitud_dict = solicitud.to_dict()
    
    Factura = client_api.Facturacion.facturacion_individualV2_Dte(solicitud_dict, "Casa_Matriz")
    # Imprimir el resultado de la factura
    print(Factura.folio)

except Exception as ex:
    print(f"Error: {str(ex)}")
