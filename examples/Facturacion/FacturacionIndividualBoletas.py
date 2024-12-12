#Facturacion individual Boleta
import asyncio
import base64
import json
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
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
from SimpleFacturaSDK.models.ResponseDTE import Response
import requests
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
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
if __name__ == "__main__":
    asyncio.run(main())
