
from SimpleFacturaSDK.Base import APIClient
import base64
import json
#from requests.auth import HTTPBasicAuth
#from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
#from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
#from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
#from SimpleFacturaSDK.models.GetFactura.Documento import Documento
from SimpleFacturaSDK.models.GetFactura.Exportaciones import Exportaciones
from SimpleFacturaSDK.models.GetFactura.OtraMoneda import OtraMoneda
from SimpleFacturaSDK.models.GetFactura.Extranjero import Extranjero
from SimpleFacturaSDK.enumeracion.ReasonTypeEnum import ReasonTypeEnum
from SimpleFacturaSDK.models.GetFactura.Documento import Documento
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
from SimpleFacturaSDK.models.GetFactura.Referencia import Referencia
from datetime import datetime
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
fecha_referencia = datetime.strptime("2024-10-17", "%Y-%m-%d").date().isoformat()
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)
solicitud = RequestDTE(
    Documento=Documento(
        Encabezado=Encabezado(
            IdDoc=IdDoc(
                TipoDTE=DTEType.NotaDebitoElectronica,
                FchEmis="2024-08-13",
                FmaPago=2,
                FchVenc="2024-08-13"
            ),
            Emisor=Emisor(
                RUTEmisor="76269769-6",
                RznSoc="SERVICIOS INFORMATICOS CHILESYSTEMS EIRL",
                GiroEmis="Desarrollo de software",
                Telefono=["912345678"],
                CorreoEmisor="felipe.anzola@erke.cl",
                Acteco=[620900],
                DirOrigen="Chile",
                CmnaOrigen="Chile",
                CiudadOrigen="Chile"
            ),
            Receptor=Receptor(
                RUTRecep="77225200-5",
                RznSocRecep="ARRENDADORA DE VEHÍCULOS S.A.",
                GiroRecep="451001 - VENTA AL POR MAYOR DE VEHÍCULOS AUTOMOTORES",
                CorreoRecep="terceros-77225200@dte.iconstruye.com",
                DirRecep="Rondizzoni 2130",
                CmnaRecep="SANTIAGO",
                CiudadRecep="SANTIAGO"
            ),
            Totales=Totales(
                MntNeto=6930000.0,
                TasaIVA=19,
                IVA=1316700,
                MntTotal=8246700.0
            )
        ),
        Detalle=[
            Detalle(
                NroLinDet=1,
                NmbItem="CERRADURA DE SEGURIDAD (2PIEZA).SATURN EVO",
                CdgItem=[
                    CdgItem(
                        TpoCodigo="4",
                        VlrCodigo="EVO_2"
                    )
                ],
                QtyItem=42.0,
                UnmdItem="unid",
                PrcItem=319166.0,
                MontoItem=6930000
            )
        ],
        Referencia=[
            Referencia(
                NroLinRef=1,
                TpoDocRef="61",
                FolioRef="1268",
                FchRef=fecha_referencia,
                CodRef=1,
                RazonRef="Anular"
            )
        ]
    )
)
motivo = ReasonTypeEnum.Otros.value

try:
    Emision = client_api.Facturacion.EmisionNC_ND_V2(solicitud, "Casa Matriz", motivo)
    print("\nDatos de la Respuesta:")
    print(f"Status: {Emision.status}")
    print(f"Message: {Emision.message}")
    print(f"TipoDTE: {Emision.data.tipoDTE}")
    print(f"RUT Emisor: {Emision.data.rutEmisor}")
    print(f"RUT Receptor: {Emision.data.rutReceptor}")
    print(f"Folio: {Emision.data.folio}")
    print(f"Fecha Emision: {Emision.data.fechaEmision}")
    print(f"Total: {Emision.data.total}")
    print(Emision.data)
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")
