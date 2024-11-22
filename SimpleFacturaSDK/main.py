
import asyncio
from ClientSimpleFactura import ClientSimpleFactura
import base64
import json
from models.GetFactura.Documento import Documento
from models.GetFactura.Encabezado import Encabezado
from models.GetFactura.IdentificacionDTE import IdDoc
from models.GetFactura.Emisor import Emisor
from models.GetFactura.Receptor import Receptor
from models.GetFactura.Totales import Totales
from models.GetFactura.Detalle import Detalle
from models.GetFactura.CodigoItem import CdgItem
from enumeracion.TipoDTE import DTEType
from enumeracion.IndicadorServicio import IndicadorServicioEnum
from models.GetFactura.RequestDTE import RequestDTE
import requests
from models.ResponseDTE import Response
async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
    solicitud = RequestDTE(
        Documento=Documento(
            Encabezado=Encabezado(
                IdDoc=IdDoc(
                    TipoDTE=DTEType.BoletaElectronica,
                    FchEmis="2024-09-03",
                    FchVenc="2024-09-03",
                    IndServicio=IndicadorServicioEnum.BoletaVentasYServicios,
                ),
                Emisor=Emisor(
                    RUTEmisor="76269769-6",
                    RznSocEmisor="Chilesystems",
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
                    CorreoRecep="mercocha13@gmail.com",
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
                    DscItem="Desc1",
                    NmbItem="Producto Test",
                    QtyItem="1",
                    UnmdItem="un",
                    PrcItem="100",
                    MontoItem="100",
                    CdgItem=[]
                ),
                Detalle(
                    NroLinDet="2",
                    CdgItem=[
                        CdgItem(
                            TpoCodigo="ALFA",
                            VlrCodigo="123"
                        )
                    ],
                    DscItem="Desc2",
                    NmbItem="Producto Test",
                    QtyItem="1",
                    UnmdItem="un",
                    PrcItem="100",
                    MontoItem="100"
                    
                )
            ]
        ),
        Observaciones="NOTA AL PIE DE PAGINA",
        Cajero="CAJERO",
        TipoPago="CONTADO"
    )
    try:
        Boleta = await client_api.Facturacion.facturacion_individualV2_Boletas(solicitud, "Casa Matriz")
        print("\nDatos de la Respuesta:")
        print(f"Status: {Boleta.status}")
        print(f"Message: {Boleta.message}")
        print(f"TipoDTE: {Boleta.data.tipoDTE}")
        print(f"RUT Emisor: {Boleta.data.rutEmisor}")
        print(f"RUT Receptor: {Boleta.data.rutReceptor}")
        print(f"Folio: {Boleta.data.folio}")
        print(f"Fecha Emision: {Boleta.data.fechaEmision}")
        print(f"Total: {Boleta.data.total}")
        print(Boleta.data)
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
        print("Detalle del error:", http_err.response.text)
    except Exception as err:
        print(f"Error: {err}")
    finally:
        await client_api.Facturacion.close()
if __name__ == "__main__":
    asyncio.run(main())
