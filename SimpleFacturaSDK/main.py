
from SimpleFacturaSDK.Base import APIClient
import base64
import json
#from requests.auth import HTTPBasicAuth
#from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
#from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
#from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte

from SimpleFacturaSDK.models.GetFactura.Documento import Documento
from SimpleFacturaSDK.models.GetFactura.Exportaciones import Exportaciones
from SimpleFacturaSDK.models.GetFactura.OtraMoneda import OtraMoneda
from SimpleFacturaSDK.models.GetFactura.Extranjero import Extranjero
from SimpleFacturaSDK.models.GetFactura.Aduana import Aduana
from SimpleFacturaSDK.models.GetFactura.Transporte import Transporte
from SimpleFacturaSDK.models.GetFactura.Chofer import Chofer
from SimpleFacturaSDK.models.GetFactura.TipoBulto import TipoBulto
from SimpleFacturaSDK.enumeracion.CodigosAduana import Paises,Moneda, ModalidadVenta, ClausulaCompraVenta, ViasdeTransporte, Puertos, UnidadMedida, TipoBultoEnum
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
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response


username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)

solicitud = RequestDTE(
    Documento=Documento(
        Encabezado=Encabezado(
            IdDoc=IdDoc(
                TipoDTE=DTEType.FacturaElectronica,
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
                MntNeto="832",
                TasaIVA="19",
                IVA="158",
                MntTotal="990"
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
    TipoPago="30 dias"
)

try:
    Factura = client_api.Facturacion.facturacion_individualV2_Dte(solicitud, "Casa Matriz")
    print("\nDatos de la Respuesta:")
    print(f"Status: {Factura.status}")
    print(f"Message: {Factura.message}")
    print(f"TipoDTE: {Factura.data.tipoDTE}")
    print(f"RUT Emisor: {Factura.data.rutEmisor}")
    print(f"RUT Receptor: {Factura.data.rutReceptor}")
    print(f"Folio: {Factura.data.folio}")
    print(f"Fecha Emision: {Factura.data.fechaEmision}")
    print(f"Total: {Factura.data.total}")
    print(Factura.data)

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")