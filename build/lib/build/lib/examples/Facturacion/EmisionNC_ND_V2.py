#EmisionNC_ND_V2

import asyncio
import base64
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.ReasonTypeEnum import ReasonTypeEnum
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
from SimpleFacturaSDK.models.GetFactura.Referencia import Referencia
from SimpleFacturaSDK.models.ResponseDTE import Response
import requests
from datetime import datetime
fecha_referencia = datetime.strptime("2024-10-17", "%Y-%m-%d").date().isoformat()
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
                        TipoDTE=DTEType.NotaCreditoElectronica,
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
            Emision = await client_api.Facturacion.EmisionNC_ND_V2(solicitud, "Casa Matriz", motivo)
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
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())