
from SimpleFacturaSDK.Base import APIClient
import base64
import json
#from requests.auth import HTTPBasicAuth
#from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
#from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
#from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte

from SimpleFacturaSDK.models.GetFactura.Documento import Documento
from SimpleFacturaSDK.models.GetFactura.Encabezado import Encabezado
from SimpleFacturaSDK.models.GetFactura.IdentificacionDTE import IdDoc
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.models.GetFactura.Totales import Totales
from SimpleFacturaSDK.models.GetFactura.Detalle import Detalle
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CdgItem
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicioEnum
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response


username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)

solicitud = RequestDTE(
    Documento=Documento(
        Encabezado=Encabezado(
            IdDoc=IdDoc(
                TipoDTE=DTEType.BoletaElectronica,
                FchEmis="2024-09-03",
                IndServicio=IndicadorServicioEnum.BoletaVentasYServicios,
                FchVenc="2024-09-03"
            ),
            Emisor=Emisor(
                RUTEmisor="76269769-6",
                RznSocEmisro="Chilesystems",
                GiroEmisor="Desarrollo de software",
                DirOrigen="Calle 7 numero 3",
                CmnaOrigen="Santiago"
            ),
            Receptor=Receptor(
                RUTRecep="17096073-4",
                RznSocRecep="Proveedor Test",
                DirRecep="calle 12",
                CmnaRecep="Paine",
                CiudadRecep="Santiago",
                CorreoRecep="mvega@chilesystems.com"
            ),
            Totales=Totales(
                MntNeto="8320",
                IVA="1580",
                MntTotal="9900"
            )
        ),
        Detalle=[
            Detalle(
                NroLinDet="1",
                NmbItem="Alfajor",
                CdgItem=[
                    CdgItem(
                        TpoCodigo="ALFA",
                        VlrCodigo="123"
                    )
                ],
                QtyItem="1",
                UnmdItem="un",
                PrcItem="831.932773",
                MontoItem="832"
            )
        ]
    ),
    Observaciones="NOTA AL PIE DE PAGINA",
    Cajero="CAJERO",
    TipoPago="CONTADO"
)

try:
    
    
    # Obtener DTE
    dte_bytes = client_api.Facturacion.obtener_dte(solicitud)
    print(dte_bytes)
    print("El DTE se ha descargado correctamente.", dte_bytes.folio)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print("Detalle del error:", response.text)
except Exception as err:
    print(f"An error occurred: {err}")
