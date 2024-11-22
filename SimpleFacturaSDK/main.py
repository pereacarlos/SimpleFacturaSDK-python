
import asyncio
from ClientSimpleFactura import ClientSimpleFactura
import base64
import json
from models.GetFactura.Exportaciones import Exportaciones
from models.GetFactura.OtraMoneda import OtraMoneda
from models.GetFactura.Extranjero import Extranjero
from models.GetFactura.Aduana import Aduana
from models.GetFactura.Transporte import Transporte
from models.GetFactura.TipoBulto import TipoBulto
from enumeracion.CodigosAduana import Paises,Moneda, ModalidadVenta, ClausulaCompraVenta, ViasdeTransporte, Puertos, UnidadMedida, TipoBultoEnum
from models.GetFactura.Encabezado import Encabezado
from models.GetFactura.IdentificacionDTE import IdDoc
from models.GetFactura.Emisor import Emisor
from models.GetFactura.Receptor import Receptor
from models.GetFactura.Totales import Totales
from models.GetFactura.Detalle import Detalle
from models.GetFactura.CodigoItem import CdgItem
from enumeracion.TipoDTE import DTEType
from models.GetFactura.RequestDTE import RequestDTE
from datetime import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    client_api = ClientSimpleFactura(username, password)
    solicitud = RequestDTE(
        Exportaciones=Exportaciones(
            Encabezado=Encabezado(
                IdDoc=IdDoc(
                    TipoDTE=DTEType.FacturaExportacionElectronica,
                    FchEmis="2024-08-17",
                    FmaPago=1,
                    FchVenc="2024-08-17",
                    Folio=1105,
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
                        TipoBultos=[
                            TipoBulto(
                                CodTpoBultos=TipoBultoEnum.CONTENEDOR_REFRIGERADO,
                                CantBultos=30,
                                IdContainer="1-2",
                                Sello="1-3",
                                EmisorSello="CONTENEDOR"
                                
                            )
                        ],
                        MntFlete=965.1,
                        MntSeguro=10.25,
                        CodPaisRecep=Paises.ARGENTINA,
                        CodPaisDestin=Paises.ARGENTINA
                    ),
                    
                ),
                Totales=Totales(
                        TpoMoneda=Moneda.DOLAR_ESTADOUNIDENSE,
                        MntExe=1000,
                        MntTotal=1000
                    ),
                OtraMoneda= OtraMoneda(
                        TpoMoneda=Moneda.PESO_CHILENO,
                        TpoCambio=800.36,
                        MntNetoOtrMnda=45454.36,
                        MntExeOtrMnda=45454.36,
                    ),
            ),
            Detalle=[
                    Detalle(
                    NroLinDet= 1,
                    CdgItem=[
                        CdgItem(
                            TpoCodigo="INT1",
                            VlrCodigo="39"
                        )
                    ],
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
        Exportacion = await client_api.Facturacion.facturacion_individualV2_Exportacion(solicitud, "Casa Matriz")
        print("\nDatos de la Respuesta:")
        print(f"Status: {Exportacion.status}")
        print(f"Message: {Exportacion.message}")
        print(f"TipoDTE: {Exportacion.data.tipoDTE}")
        print(f"RUT Emisor: {Exportacion.data.rutEmisor}")
        print(f"RUT Receptor: {Exportacion.data.rutReceptor}")
        print(f"Folio: {Exportacion.data.folio}")
        print(f"Fecha Emision: {Exportacion.data.fechaEmision}")
        print(f"Total: {Exportacion.data.total}")
        print(Exportacion.data)

    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
        print("Detalle del error:", http_err.response.text)
    except Exception as err:
        print(f"Error: {err}")
    finally:
        await client_api.Facturacion.close()
if __name__ == "__main__":
    asyncio.run(main())
