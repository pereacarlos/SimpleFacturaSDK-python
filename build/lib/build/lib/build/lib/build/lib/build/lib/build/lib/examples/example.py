
#Obtener Pdf de una Factura

import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        pdf = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=4117,
                codigoTipoDte=33,
                ambiente=0
            )
        )
        try:
            pdf_response = await client_api.Facturacion.obtener_pdf(pdf)
            if pdf_response.status == 200:
                with open("factura.pdf", "wb") as file:
                    file.write(pdf_response.data)
                print("PDF guardado exitosamente")
            else:
                print(f"Error: {pdf_response.message}")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())


#Obtener timbre de una factura
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
import base64
import json
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=4117,
                codigoTipoDte=33,
                ambiente=0
            )
        )
        try:
            timbre_response = await client_api.Facturacion.obtener_timbre(solicitud)
            timbre_data = json.loads(timbre_response.data)
            with open("timbre.png", "wb") as f:
                f.write(base64.b64decode(timbre_data["data"]))
            print("Timbre guardado en timbre.png")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())


#Obtener XML de una factura

import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
import json
import base64
import requests
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
   async with ClientSimpleFactura(username, password) as client_api:
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=2393,
                codigoTipoDte=33,
                ambiente=0
            )
        )
        try:
        # Guardar PDF
            xml = await client_api.Facturacion.obtener_xml(solicitud)
            ruta = "xml.xml"
            with open(ruta, "wb") as file:
                file.write(xml.data)
            print("XML guardado en:", ruta)
        except requests.exceptions.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
            print("Detalle del error:", http_err.response.text)
        except Exception as err:
            print(f"Error: {err}")
    
if __name__ == "__main__":
    asyncio.run(main())


#Obtener DtE de una factura
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
import json
import base64
import requests
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=12553,
                codigoTipoDte=39,
                ambiente=0
            )
        )
        try:
            dte_bytes = await client_api.Facturacion.obtener_dte(solicitud)
            print(f"Status: {dte_bytes.status}")
            print(f"Message: {dte_bytes.message}")
            print(f"TipoDTE: {dte_bytes.data.tipoDte}")
            print(f"folioReutilizado: {dte_bytes.data.folioReutilizado}")
            print(f"fechaCreacionr: {dte_bytes.data.fechaCreacion}")
            print(f"Folio: {dte_bytes.data.folio}")
            print(f"razonSocialReceptor: {dte_bytes.data.razonSocialReceptor}")
            print(f"iva: {dte_bytes.data.iva}")
            print(dte_bytes.data)

        except requests.exceptions.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
            print("Detalle del error:", http_err.response.text)
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())


#Obtener SobreXml de una factura
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
import json
import base64
import requests
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=2393,
                codigoTipoDte=33,
                ambiente=0
            )
        )
        try:
            response = await client_api.Facturacion.obtener_sobreXml(solicitud, 0)
            ruta = "sobre.xml"
            with open(ruta, "wb") as f:
                f.write(response.data)
            print("El sobre XML se ha descargado correctamente.")
        except requests.exceptions.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
            print("Detalle del error:", http_err.response.text)
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())



#Facturacion individual DTE

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
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
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
            Factura = await client_api.Facturacion.facturacion_individualV2_Dte(solicitud, "Casa Matriz")
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
if __name__ == "__main__":
    asyncio.run(main())


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


#Facturacion individual Exportaciones
import asyncio
import base64
import json
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Exportaciones import Exportaciones
from SimpleFacturaSDK.models.GetFactura.OtraMoneda import OtraMoneda
from SimpleFacturaSDK.models.GetFactura.Extranjero import Extranjero
from SimpleFacturaSDK.models.GetFactura.Aduana import Aduana
from SimpleFacturaSDK.models.GetFactura.Transporte import Transporte
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
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
from datetime import datetime
import requests
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = RequestDTE(
            Exportaciones=Exportaciones(
                Encabezado=Encabezado(
                    IdDoc=IdDoc(
                        TipoDTE=DTEType.FacturaExportacionElectronica,
                        FchEmis="2024-08-17",
                        FmaPago=1,
                        FchVenc="2024-08-17"
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
if __name__ == "__main__":
    asyncio.run(main())



#Facturacion masiva 
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        credenciales = Credenciales(
            rut_emisor="76269769-6",
            nombre_sucursal="Casa Matriz"
        )
        path_csv = r"C:\Users\perea\Downloads\ejemplo_carga_masiva_nacional.csv"
        try:
            factura = await client_api.Facturacion.facturacion_Masiva(credenciales, path_csv)
            print("\nDatos de la Respuesta:")
            print(factura.data)
            print("Status Code:", factura.status)
            print("Message:", factura.message)
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())


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


#ListadoDTEEmitidos
import asyncio
import httpx
import requests
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
fecha_desde = datetime.strptime("2024-08-01", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2024-08-17", "%Y-%m-%d")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente="10422710-4",
                nombre_sucursal="Casa Matriz"
            ),
            ambiente=AmbienteEnum.Certificacion,
            folio=0,
            codigoTipoDte=DTEType.NotSet,
            desde=fecha_desde,
            hasta=fecha_hasta
        )
        try:
            Listado = await client_api.Facturacion.listadoDteEmitidos(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {Listado.status}")
            print(f"Message: {Listado.message}")
            for dte in Listado.data:
                print(f"ambiente: {dte.ambiente}")
                print(f"tipoDTE: {dte.tipoDte}")
                print(f"folioReutilizado: {dte.folioReutilizado}")
                print(f"fechaCreacion: {dte.fechaCreacion}")
                print(f"Folio: {dte.folio}")
                print(f"razonSocialReceptor: {dte.razonSocialReceptor}")
                print(f"Total: {dte.total}")
                print(dte)
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
	
if __name__ == "__main__":
    asyncio.run(main())


#EnviarCorreo
import asyncio
import httpx
import requests
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.EnvioMailRequest import EnvioMailRequest, DteClass, MailClass
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = EnvioMailRequest(
            RutEmpresa="76269769-6",
            Dte= DteClass(folio=2149, tipoDTE=33),
            Mail= MailClass(
                to=["contacto@chilesystems.com"],
                ccos=["correo@gmail.com"],
                ccs=["correo2@gmail.com"]
            ),
            Xml=True,
            Pdf=True,
            Comments="ESTO ES UN COMENTARIO"
        )

        try:
            enviarCorreo = await client_api.Facturacion.enviarCorreo(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {enviarCorreo.status}")
            print(f"Message: {enviarCorreo.message}")
            print(f"Data: {enviarCorreo.data}")
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())


#ConsolidadoVentas

import asyncio
import httpx
import requests
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
fecha_desde = datetime.strptime("2023-10-25", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2023-10-30", "%Y-%m-%d")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            ambiente=AmbienteEnum.Certificacion,
            desde=fecha_desde,
            hasta=fecha_hasta
        )
        try:
            Consolidado = await client_api.Facturacion.consolidadoVentas(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {Consolidado.status}")
            print(f"Message: {Consolidado.message}")
            for item in Consolidado.data:
                print(f"fecha: {item.fecha}")
                print(f"tipoDTE: {item.tiposDTE}")
                print(f"Emitidos: {item.emitidos}")
                print(f"anulados: {item.anulados}")
                print(f"total: {item.total}")
                print(f"totalNeto: {item.totalNeto}")
                print(f"totalIva: {item.totalIva}")
                print(item)
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
        
if __name__ == "__main__":
    asyncio.run(main())


#ConciliarEmitidoss
import asyncio
import httpx
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import requests
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud =Credenciales(
            rut_emisor="76269769-6"
        )
        try:
            Conciliar = await client_api.Facturacion.ConciliarEmitidos(solicitud,5,2024)
            print("\nDatos de la Respuesta:")
            print(f"Status: {Conciliar.status}")
            print(f"Message: {Conciliar.message}")
            print(f"Data: {Conciliar.data}")
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())



#Crear productos
import asyncio
import json
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Productos.DatoExternoRequest import DatoExternoRequest
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Productos=[
                NuevoProductoExternoRequest(
                    nombre="NOmGoma 26",
                    codigoBarra="NOMGoma 25",
                    unidadMedida="un",
                    precio=50,
                    exento=False,
                    tieneImpuestos=False,
                    impuestos=[0]
                ),
                NuevoProductoExternoRequest(
                    nombre="NOMGoma 2122",
                    codigoBarra="NOMGoma 2212",
                    unidadMedida="un",
                    precio=50,
                    exento=False,
                    tieneImpuestos=True,
                    impuestos=[ 271,23]
                
                )
            ]
        )
        try:
            addProducts = await client_api.Productos.CrearProducto(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {addProducts.status}")
            print(f"Message: {addProducts.message}")
            for productos in addProducts.data:
                print(f"ProductoId: {productos.productoId}")
                print(f"Nombre: {productos.nombre}")
                print(f"Precio: {productos.precio}")
                print(f"Exento: {productos.exento}")
                print(f"Activo: {productos.activo}")
                print(f"EmisorId: {productos.emisorId}")
                print(f"SucursalId: {productos.sucursalId}")
                print(f"Impuestos: {productos.impuestos}")
                print(f"CodigoBarra: {productos.codigoBarra}")
                print(f"UnidadMedida: {productos.unidadMedida}")
                print(f"NombreCategoria: {productos.NombreCategoria}")
                print(f"NombreMarca: {productos.NombreMarca}")
                print(f"Stock: {productos.Stock}")
                print("\n")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())



#Listar productos 
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= Credenciales(
            rut_emisor="76269769-6",
            nombre_sucursal="Casa Matriz"
        )
        try:
            ListProduct = await client_api.Productos.listarProductos(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListProduct.status}")
            print(f"Message: {ListProduct.message}")
            for i in ListProduct.data:
                print(f"productoId: {i.productoId}")
                print(f"nombre: {i.nombre}")
                print(f"precio: {i.precio}")
                print(f"exento: {i.exento}")
                for imp in i.impuestos:
                    print(f"codigoSii: {imp.codigoSii}")
                    print(f"nombreImp: {imp.nombreImp}")
                    print(f"tasa: {imp.tasa}")
    
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
    



#ListarDTERecibido Proveedores
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
fecha_desde = datetime.strptime("2024-04-01", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2024-04-30", "%Y-%m-%d")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= None,
            codigoTipoDte=None,
            desde=fecha_desde,
            hasta=fecha_hasta,
        )
        try:
            ListProveedores = await client_api.Proveedores.listarDteRecibidos(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListProveedores.status}")
            print(f"Message: {ListProveedores.message}")
            for lista in ListProveedores.data:
                print(f"Ambiente: {lista.ambiente}")
                print(f"codigoSii: {lista.codigoSii}")
                print(f"Tipo DTE: {lista.tipoDte}")
                print(f"estadoSII: {lista.estadoSII}")
                print(f"estado: {lista.estado}")
                print(f"folio: {lista.folio}")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())
  

#Obtener XML Proveedores
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente="96689310-9"
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= 7366834,
            codigoTipoDte=DTEType.NotaCreditoElectronica
        )
        try:
            Obtenerxml = await client_api.Proveedores.obtenerXml(solicitud)
            ruta = "xml2.xml"
            with open(ruta, "wb") as file:
                file.write(Obtenerxml.data)
            print(f"XML guardado en {ruta}")

        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())



#Obtener PDF Proveedores
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente="76269769-6"
            ),
            ambiente=AmbienteEnum.Certificacion,
            folio= 2232,
            codigoTipoDte=DTEType.FacturaElectronica
        )
        try:
            ObtenerPdf = await client_api.Proveedores.obtener_pdf(solicitud)
            ruta = "pdf.pdf"
            with open(ruta, "wb") as file:
                file.write(ObtenerPdf.data)
            print(f"PDF guardado en {ruta}")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())



#ConciliarRecibidos Proveedores
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud=Credenciales(rut_emisor="76269769-6")

        try:
            Obtener_pdf = await client_api.Proveedores.ConciliarRecibidos(solicitud,5,2024)
            print("\nDatos de la Respuesta:")
            print(f"Status: {Obtener_pdf.status}")
            print(f"Message: {Obtener_pdf.message}")
            print(f"Data: {Obtener_pdf.data}")

        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())
    

#Aceptar o Rechazar Acuse Proveedores
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Proveedores.AcuseReciboExternoRequest import AcuseReciboExternoRequest
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.enumeracion.ResponseType import ResponseType
from SimpleFacturaSDK.enumeracion.RejectionType import RejectionType
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= AcuseReciboExternoRequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente= "77720532-3",
                nombre_sucursal="Casa Matriz"
            ),
            dteReferenciadoExterno=DteReferenciadoExterno(
                folio=220,
                codigoTipoDte=33,
                ambiente=0
            ),
            respuesta=ResponseType.Rejected,
            tipo_rechazo=RejectionType.RCD,
            comentario="test"
        )
        try:
            AceptarRecchazarAcuse = await client_api.Proveedores.Aceptar_RechazarDTE(solicitud)
            print(AceptarRecchazarAcuse)
            print("\nDatos de la Respuesta:")
            print(f"Status: {AceptarRecchazarAcuse.status}")
            print(f"Message: {AceptarRecchazarAcuse.message}")
            print(f"Data: {AceptarRecchazarAcuse.data}")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
   

#CrearClientes
import asyncio
import base64
import requests
import json
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Productos.DatoExternoRequest import DatoExternoRequest
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from SimpleFacturaSDK.models.Clientes.NuevoReceptorExternoRequest import NuevoReceptorExternoRequest
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Clientes=[
                NuevoReceptorExternoRequest(
                    Rut="57681892-0",
                    RazonSocial="Cliente Test 1",
                    Giro="Giro 1",
                    DirPart="direccion 1",
                    DirFact="direccion 1",
                    CorreoPar="correo 1",
                    CorreoFact="correo 1",
                    Ciudad="Ciudad 1",
                    Comuna="Comuna 1"
                ),
                NuevoReceptorExternoRequest(
                    Rut="56516677-8",
                    RazonSocial="Cliente Test 2",
                    Giro="Giro 2",
                    DirPart="direccion 2",
                    DirFact="direccion 2",
                    CorreoPar="correo 2",
                    CorreoFact="correo 2",
                    Ciudad="Ciudad 2",
                    Comuna="Comuna 2"
                ),
                NuevoReceptorExternoRequest(
                    Rut="68959276-7",
                    RazonSocial="Cliente Test 3",
                    Giro="Giro 3",
                    DirPart="direccion 3",
                    DirFact="direccion 3",
                    CorreoPar="correo 3",
                    CorreoFact="correo 3",
                    Ciudad="Ciudad 3",
                    Comuna="Comuna 3"
                )
            ]
        )
        try:
            AddClient = await client_api.Clientes.CrearClientes(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {AddClient.status}")
            print(f"Message: {AddClient.message}")
            
            for cliente in AddClient.data:
                print(f"ReceptorId: {cliente.receptorId}")
                print(f"EmisorId: {cliente.emisorId}")
                print(f"RUT: {cliente.rut}")
                print(f"Dv: {cliente.dv}")
                print(f"RutFormateado: {cliente.rutFormateado}")
                print(f"RazonSocial: {cliente.razonSocial}")
                print(f"NombreFantasia: {cliente.nombreFantasia}")
                print(f"Giro: {cliente.giro}")
                print(f"DirPart: {cliente.dirPart}")
                print(f"DirFact: {cliente.dirFact}")
                print(f"CorreoPar: {cliente.correoPar}")
                print(f"CorreoFact: {cliente.correoFact}")
                print(f"Ciudad: {cliente.ciudad}")
                print(f"Comuna: {cliente.comuna}")
                print(f"Activo: {cliente.activo}")
                print("\n")
        except Exception as err:
            print(f"Error: {err}")
        finally:
            await client_api.Clientes.close()
       
if __name__ == "__main__":
    asyncio.run(main())
    

#Listar Clientes
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= Credenciales(rut_emisor="76269769-6")

        try:
            ListClient = await client_api.Clientes.ListarClientes(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListClient.status}")
            print(f"Message: {ListClient.message}")
            for cliente in ListClient.data:
                print(f"ReceptorId: {cliente.receptorId}")
                print(f"EmisorId: {cliente.emisorId}")
                print(f"RUT: {cliente.rut}")
                print(f"Dv: {cliente.dv}")
                print(f"RutFormateado: {cliente.rutFormateado}")
                print(f"RazonSocial: {cliente.razonSocial}")
                print(f"NombreFantasia: {cliente.nombreFantasia}")
                print(f"Giro: {cliente.giro}")
                print(f"DirPart: {cliente.dirPart}")
                print(f"DirFact: {cliente.dirFact}")
                print(f"CorreoPar: {cliente.correoPar}")
                print(f"CorreoFact: {cliente.correoFact}")
                print(f"Ciudad: {cliente.ciudad}")
                print(f"Comuna: {cliente.comuna}")
                print(f"Activo: {cliente.activo}")
                print("\n")
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
   


#Listar sucursales
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= Credenciales(rut_emisor="76269769-6")

        try:
            ListSucursal = await client_api.Sucursales.ListarSucursales(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListSucursal.status}")
            print(f"Message: {ListSucursal.message}")
            for cliente in ListSucursal.data:
                print(f"Nombre: {cliente.nombre}")
                print(f"Direccion: {cliente.direccion}")
                print("\n")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
    



#ConsultarFoliosDisponibles
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Folios.SolicitudFolios import SolicitudFolios
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= SolicitudFolios(
            RutEmpresa="76269769-6",
            TipoDTE=33,
            Ambiente=0
        )


        try:
            ConsultaFolio = await client_api.Folios.ConsultaFoliosDisponibles(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ConsultaFolio.status}")
            print(f"Message: {ConsultaFolio.message}")
            print(f"Data: {ConsultaFolio.data}")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())


#SolicitarFolios
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            Cantidad= 3,
            CodigoTipoDte= DTEType.FacturaElectronica
        )
        try:
            SolicitarFolio = await client_api.Folios.SolicitarFolios(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {SolicitarFolio.status}")
            print(f"Message: {SolicitarFolio.message}")
            print(f"Data: {SolicitarFolio.data}")
            print(f"codigoSii: {SolicitarFolio.data.codigoSii}")
            print(f"fechaIngreso: {SolicitarFolio.data.fechaIngreso}")
            print(f"desde: {SolicitarFolio.data.desde}")
            print(f"hasta: {SolicitarFolio.data.hasta}")
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())



#ConsultarFolios
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            CodigoTipoDte= None,
            Ambiente=0
        )
        try:
            ConsultarFolios = await client_api.Folios.ConsultarFolios(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ConsultarFolios.status}")
            print(f"Message: {ConsultarFolios.message}")
            print(f"Data: {ConsultarFolios.data}")
            for folio in ConsultarFolios.data:
                print(f"folio: {folio.foliosDisponibles}")
                print(f"codigoSii: {folio.codigoSii}")
                print(f"fechaIngreso: {folio.fechaIngreso}")
                print(f"desde: {folio.desde}")
                print(f"hasta: {folio.hasta}")

        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())




#FoliosSin Uso
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Folios.SolicitudFolios import SolicitudFolios
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= SolicitudFolios(
            RutEmpresa = "76269769-6",
            TipoDTE = 33,
            Ambiente = 0
        )
        try:
            FolioSinUsar = await client_api.Folios.Folios_Sin_Uso(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {FolioSinUsar.status}")
            print(f"Message: {FolioSinUsar.message}")
            print(f"Data: {FolioSinUsar.data}")
            for data in FolioSinUsar.data:
                print(f"desde: {data.desde}")
                print(f"hasta: {data.hasta}")
                print(f"Cantidad: {data.cantidad}")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())



#Datos Empresas
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= Credenciales(
            rut_emisor="76269769-6"
        )
        try:
            DatosEmpresa = await client_api.ConfiguracionService.datos_empresa(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {DatosEmpresa.status}")
            print(f"Message: {DatosEmpresa.message}")
            print(f"Data: {DatosEmpresa.data}")
            print(f"rut: {DatosEmpresa.data.rut}")
            print(f"razonSocial: {DatosEmpresa.data.razonSocial}")
            print(f"giro: {DatosEmpresa.data.giro}")
    
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())
    

    

#Obtener PDF Recibidas Boleta de Honorarios
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= BHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente= "26429782-6"
            ),
            Folio=2
        )
        try:
            ObtenerPdfRecibida = await client_api.BoletaHonorarioService.ObtenerPdfBoletaRecibida(solicitud)
            ruta = "BoletaHonorarioRecibida.pdf"
            with open(ruta, "wb") as archivo:
                archivo.write(ObtenerPdfRecibida.data)
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
    

    

#Obtener PDF Emitidas Boleta de Honorarios
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= BHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            Folio=15
        )
        try:
            ObtenerPdf = await client_api.BoletaHonorarioService.ObtenerPdf(solicitud)
            ruta = "BoletaHonorario.pdf"
            with open(ruta, "wb") as archivo:
                archivo.write(ObtenerPdf.data)
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())


#ListadoBHEEmitidas Boleta de Honorarios
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.BoletaHonorarios.ListaBHERequest import ListaBHERequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
import json
from datetime import datetime
fecha_desde = datetime.strptime("2024-09-03", "%Y-%m-%d").isoformat()
fecha_hasta = datetime.strptime("2024-11-11", "%Y-%m-%d").isoformat()
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= ListaBHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Folio=None,
            Desde=fecha_desde,
            Hasta=fecha_hasta
        )
        try:
            ListadoBHEEmitidos = await client_api.BoletaHonorarioService.ListadoBHEEmitidos(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListadoBHEEmitidos.status}")
            print(f"Message: {ListadoBHEEmitidos.message}")
            for cliente in ListadoBHEEmitidos.data:
                print(f"fOLIO: {cliente.folio}")
                print(f"FECHAEMISION: {cliente.fechaEmision}")
                print(f"codigoBarra: {cliente.codigoBarra}")
                print("\n")     

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())


#Listado de Boletas de Honorarios Recibidas
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.BoletaHonorarios.ListaBHERequest import ListaBHERequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime
fecha_desde = datetime.strptime("2024-09-03", "%Y-%m-%d").isoformat()
fecha_hasta = datetime.strptime("2024-11-11", "%Y-%m-%d").isoformat()
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= ListaBHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Folio=None,
            Desde=fecha_desde,
            Hasta=fecha_hasta
        )


        try:
            ListadoBHERecibido = await client_api.BoletaHonorarioService.ListadoBHERecibido(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListadoBHERecibido.status}")
            print(f"Message: {ListadoBHERecibido.message}")
            for cliente in ListadoBHERecibido.data:
                print(f"fOLIO: {cliente.folio}")
                print(f"FECHAEMISION: {cliente.fechaEmision}")
                print("\n")  
    
        except Exception as err:
            print(f"Error: {err}")

if __name__ == "__main__":
    asyncio.run(main())