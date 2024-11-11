
from SimpleFacturaSDK.Base import APIClient
import base64
import json
from SimpleFacturaSDK.models.GetFactura.Documento import Documento
from SimpleFacturaSDK.models.GetFactura.Encabezado import Encabezado
from SimpleFacturaSDK.models.GetFactura.IdentificacionDTE import IdDoc
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.models.GetFactura.Totales import Totales
from SimpleFacturaSDK.models.GetFactura.Detalle import Detalle
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CdgItem
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
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
    solicitud_dict = dataclass_to_dict(solicitud)
    Factura = client_api.Facturacion.facturacion_individualV2_Dte(solicitud_dict, "Casa_Matriz")
    solicitud_json = json.dumps(solicitud_dict, ensure_ascii=False, indent=4)
    print("Solicitud:", solicitud_json)
    print(Factura)
    ruta = "Factura.json"
    with open(ruta, 'w') as file:
        json.dump(Factura, file)
    print("Factura guardada en:",ruta)



except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print("Detalle del error:", response.text)
except Exception as err:
    print(f"An error occurred: {err}")
