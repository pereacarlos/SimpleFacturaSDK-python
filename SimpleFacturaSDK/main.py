
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
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response


username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)

solicitud = RequestDTE(
    Exportaciones=Exportaciones(
        Encabezado=Encabezado(
            IdDoc=IdDoc(
                TipoDTE=DTEType.FacturaExportacionElectronica,
                FchEmis="2024-08-17",
                FmaPago=1,
                FchVenc="2024-08-17",
            ),
            Emisor=Emisor(
                RUTEmisor="76269769-6",
                RznSoc="Chilesystems",
                GiroEmis="Desarrollo de software",
                Telefono=["912345678"],
                CorreoEmisor="mvega@chilesystems.com",
                Acteco=[620200],
                DirOrigen="Calle 7 numero 3",
                CmnaOrigen="Santiago",
                CiudadOrigen="Santiago"
            ),
            Receptor=Receptor(
                RUTRecep="55555555-5",
                RznSocRecep="CLIENTE INTERNACIONAL EXP IMP",
                Extranjero=Extranjero(
                    NumId="331-555555",
                    Nacionalidad= 331
                ),
                GiroRecep="Giro de Cliente",
                CorreoRecep="amamani@chilesystems.com",
                DirRecep="Dirección de Cliente",
                CmnaRecep="Comuna de Cliente",
                CiudadRecep="Ciudad de Cliente"
            ),
            Transporte=Transporte(
                Aduana=Aduana(
                    CodModVenta=ModalidadVenta.A_FIRME,
                    CodClauVenta=ClausulaCompraVenta.FOB,
                    TotClauVenta=1984.65,
                    CodViaTransp=ViasdeTransporte.AEREO,
                    CodPtoEmbarque= 901,
                    CodPtoDesemb=262,
                    Tara=1,
                    CodUnidMedTara=UnidadMedida.U,
                    PesoBruto=10.65,
                    CodUnidPesoBruto=UnidadMedida.KN,
                    PesoNeto=9.56,
                    CodUnidPesoNeto=UnidadMedida.KN,
                    TotBultos=30,
                    TipoBultos=TipoBulto(
                        CodTpoBultos=75,
                        CantBultos=30,
                        IdContainer="1-2",
                        Sello="1-3",
                        EmisorSello="CONTENEDOR"
                        
                    ),
                    MntFlete=965.1,
                    MntSeguro=10.25,
                    CodPaisRecep=Paises.ARGENTINA,
                    CodPaisDestin=Paises.ARGENTINA
                ),
                
            ),
            Totales=Totales(
                    TpoMoneda=13,
                    MntExe=1000,
                    MntTotal=1000
                ),
            OtraMoneda= OtraMoneda(
                    TpoMoneda=200,
                    TpoCambio=800.36,
                    MntNetoOtrMnda=45454.36,
                    MntExeOtrMnda=45454.36,
                ),
        ),
        Detalle=[
                Detalle(
                NroLinDet= 1,
                CdgItem=CdgItem(
                    TpoCodigo="INT1",
                    VlrCodigo="39"
                ),
                IndExe=1,
                NmbItem="CHATARRA DE ALUMINIO",
                DscItem="OPCIONAL",
                QtyItem=1,
                UnmdItem="U",
                PrcItem=100,
                MontoItem=100
            )
        
        ]
    ),
    Observaciones="NOTA AL PIE DE PAGINA"
)


try:
    
    
    Factura = client_api.Facturacion.facturacion_individualV2_Exportacion(solicitud, "Casa_Matriz")
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
    print(f"HTTP error occurred: {http_err}")
    print("Detalle del error:", response.text)
except Exception as err:
    print(f"An error occurred: {err}")
