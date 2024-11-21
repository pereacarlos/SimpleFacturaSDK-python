import unittest
from ClientSimpleFactura import ClientSimpleFactura
import base64
import json
from dotenv import load_dotenv
import os
from unittest.mock import AsyncMock, patch
from requests.auth import HTTPBasicAuth
from models.GetFactura.Credenciales import Credenciales
from models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
from models.GetFactura.InvoiceData import InvoiceData
from models.GetFactura.Documento import Documento
from models.GetFactura.Exportaciones import Exportaciones
from models.GetFactura.OtraMoneda import OtraMoneda
from models.GetFactura.Extranjero import Extranjero
from enumeracion.ReasonTypeEnum import ReasonTypeEnum
from models.GetFactura.Documento import Documento
from models.GetFactura.Aduana import Aduana
from models.GetFactura.Transporte import Transporte
from models.GetFactura.Chofer import Chofer
from models.GetFactura.TipoBulto import TipoBulto
from enumeracion.CodigosAduana import Paises,Moneda, ModalidadVenta, ClausulaCompraVenta, ViasdeTransporte, Puertos, UnidadMedida, TipoBultoEnum
from models.GetFactura.Encabezado import Encabezado
from models.GetFactura.IdentificacionDTE import IdDoc
from models.GetFactura.Emisor import Emisor
from models.GetFactura.Receptor import Receptor
from models.GetFactura.Totales import Totales
from models.GetFactura.Detalle import Detalle
from models.GetFactura.CodigoItem import CdgItem
from models.GetFactura.Dte import Dte
from enumeracion.TipoDTE import DTEType
from models.GetFactura.EnvioMailRequest import EnvioMailRequest, DteClass, MailClass
from enumeracion.IndicadorServicio import IndicadorServicioEnum
from models.GetFactura.RequestDTE import RequestDTE
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from models.GetFactura.Credenciales import Credenciales
from models.GetFactura.Referencia import Referencia
from enumeracion.Ambiente import AmbienteEnum
from models.GetFactura.ListadoRequest import ListaDteRequestEnt
from models.Folios.SolicitudFolios import SolicitudFolios
from models.Folios.TimbrajeEnt import TimbrajeEnt
from models.Folios.Foliorequest import FolioRequest
from datetime import datetime
import requests
from models.ResponseDTE import Response
fecha_referencia = datetime.strptime("2024-10-17", "%Y-%m-%d").date().isoformat()

load_dotenv()
class TestFacturacionService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.Facturacion
        self.service_folios = self.client_api.Folios

    async def asyncTearDown(self):
        await self.client_api.Facturacion.close()

    async  def test_obtener_pdf_returnOK(self):
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

        response = await  self.service.obtener_pdf(solicitud)

        self.assertIsNotNone(response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, bytes)
        self.assertGreater(len(response.data), 0)

    def test_obtener_pdf_bad_request(self):
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="",
                nombre_sucursal="Casa Matriz"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=None, 
                codigoTipoDte=33,
                ambiente=0
            )
        )
        response = self.service.obtener_pdf(solicitud)
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_obtener_pdf_bad_request(self):
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="",
                nombre_sucursal="Casa Matriz"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=None, 
                codigoTipoDte=33,
                ambiente=0
            )
        )
        response = self.service.obtener_pdf(solicitud)
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_obtener_timbre_returnOK(self):
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=2963,
                codigoTipoDte=33,
                ambiente=0
            )
        )
        response = self.service.obtener_timbre(solicitud)
        
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, bytes)
        self.assertGreater(len(response.data), 0)
        self.assertIsNotNone(response.data)

    def test_obtener_timbre_bad_request(self):
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="",
                nombre_sucursal="Casa Matriz"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=None, 
                codigoTipoDte=33,
                ambiente=0
            )
        )
        response = self.service.obtener_timbre(solicitud)

        self.assertIsNotNone(response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_obtener_xml_returnOK(self):
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
        response = self.service.obtener_xml(solicitud)
        
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, bytes)
        self.assertGreater(len(response.data), 0)

    def test_obtener_xml_bad_request(self):
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor=""
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=None, 
                codigoTipoDte=39,
                ambiente=0
            )
        )
        response = self.service.obtener_xml(solicitud)
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_obtener_dte_returnOK(self):
        solicitud= SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=12553,
                codigoTipoDte=39,
                ambiente=0
            )
        )

        response = self.service.obtener_dte(solicitud)
        
        # Verifica que la respuesta es correcta
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, Dte)
        dte_data = response.data
        self.assertIsNotNone(dte_data.folio)

    def test_obtener_dte_bad_request(self):
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor=""
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=None, 
                codigoTipoDte=39,
                ambiente=0
            )
        )
        response = self.service.obtener_dte(solicitud)

        self.assertIsNotNone(response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)
        self.assertIn("data", response.message) 

    def test_obtener_sobreXml_returnOK(self):
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
        response = self.service.obtener_sobreXml(solicitud,0)
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, bytes)
        self.assertGreater(len(response.data), 0)
        
    def test_obtener_sobreXml_bad_request_WhenSolicitudIsFalse(self):
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor=""
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=None, 
                codigoTipoDte=33,
                ambiente=0
            )
        )
        response = self.service.obtener_sobreXml(solicitud,0)
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)
        self.assertIn("archivoExternoEnt", response.message)

    def test_obtener_sobreXml_bad_request_WhenSobreIsInvalid(self):
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
        response = self.service.obtener_sobreXml(solicitud,"sdd")
        self.assertIsNotNone(response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_facturacion_individualV2_dte_returnOK(self):
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

        response = self.service.facturacion_individualV2_Dte(solicitud, "Casa Matriz")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsInstance(response.data, InvoiceData)
        self.assertIsNotNone(response.data.folio) 

    def test_facturacion_individualV2_dte_bad_request_WhenSucursalInvalid(self):
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

        response = self.service.facturacion_individualV2_Dte(solicitud, 1)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)  
       
    def test_facturacion_individualV2_dte_bad_request_WhenSDatosInvalid(self):
        solicitud = RequestDTE(
            Documento=Documento(
                Encabezado=Encabezado(
                    IdDoc=IdDoc(
                        TipoDTE=None, 
                        FchEmis="2024-09-05",
                        FmaPago=None,
                        FchVenc=None
                    ),
                    Emisor=Emisor(
                        RUTEmisor="",
                        RznSoc="",
                        GiroEmis="",
                        Telefono=[],
                        CorreoEmisor="",
                        Acteco=[],
                        DirOrigen="",
                        CmnaOrigen="",
                        CiudadOrigen=""
                    ),
                    Receptor=Receptor(
                        RUTRecep="",
                        RznSocRecep="",
                        GiroRecep="",
                        CorreoRecep="",
                        DirRecep="",
                        CmnaRecep="",
                        CiudadRecep=""
                    ),
                    Totales=Totales(
                        MntNeto=None,
                        TasaIVA=None,
                        IVA=None,
                        MntTotal=None
                    )
                ),
                Detalle=[]
            ),
            Observaciones="",
            TipoPago=""
        )
        response = self.service.facturacion_individualV2_Dte(solicitud, "Casa Matriz")

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)    
    
    def test_facturacion_individualV2_dte_serverError(self):
        solicitud = RequestDTE(
        )

        response = self.service.facturacion_individualV2_Dte(solicitud, "Casa Matriz")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNotNone(response.message)

    def test_facturacion_individualV2_Boleta_ReturnOK(self):
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

        response = self.service.facturacion_individualV2_Boletas(solicitud, "Casa Matriz")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.data.folio)
        
    def test_facturacion_individualV2_Boleta_bad_request_WhenSucursalInvalid(self):
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

        response = self.service.facturacion_individualV2_Boletas(solicitud, 1)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_facturacion_individualV2_Boleta_bad_request_WhenSDatosInvalid(self):
        solicitud = RequestDTE(
            Documento=Documento(
                Encabezado=Encabezado(
                    IdDoc=IdDoc(
                        TipoDTE=None, 
                        FchEmis="2024-09-05",
                        FmaPago=None,
                        FchVenc=None
                    ),
                    Emisor=Emisor(
                        RUTEmisor="",
                        RznSoc="",
                        GiroEmis="",
                        Telefono=[],
                        CorreoEmisor="",
                        Acteco=[],
                        DirOrigen="",
                        CmnaOrigen="",
                        CiudadOrigen=""
                    ),
                    Receptor=Receptor(
                        RUTRecep="",
                        RznSocRecep="",
                        GiroRecep="",
                        CorreoRecep="",
                        DirRecep="",
                        CmnaRecep="",
                        CiudadRecep=""
                    ),
                    Totales=Totales(
                        MntNeto=None,
                        TasaIVA=None,
                        IVA=None,
                        MntTotal=None
                    )
                ),
                Detalle=[]
            ),
            Observaciones="",
            TipoPago=""
        )

        response = self.service.facturacion_individualV2_Boletas(solicitud, "Casa Matriz")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_facturacion_individualV2_Boleta_serverError(self):
        solicitud = RequestDTE(
        )

        response = self.service.facturacion_individualV2_Boletas(solicitud, "Casa Matriz")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNotNone(response.message)

    def test_facturacion_individualV2_Exportacion_ReturnOK(self):
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

        response = self.service.facturacion_individualV2_Exportacion(solicitud, "Casa Matriz")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.data.folio)

    def test_facturacion_individualV2_Exportacion_badRequest_WhenSucursalInvalid(self):
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

        response = self.service.facturacion_individualV2_Exportacion(solicitud, 1)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_facturacion_individualV2_Exportacion_badRequest_WhenDatosInvalid(self):
        solicitud = RequestDTE(
            Exportaciones=Exportaciones(
                Encabezado=Encabezado(
                    IdDoc=IdDoc(
                        TipoDTE=None,
                        FchEmis="",
                        FmaPago=1,
                        FchVenc="",
                    ),
                    Emisor=Emisor(
                        RUTEmisor="",
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

        response = self.service.facturacion_individualV2_Exportacion(solicitud, "Casa Matriz")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)
        
    def test_facturacion_individualV2_Exportacion_ServerError(self):
        solicitud = RequestDTE(
        )

        response = self.service.facturacion_individualV2_Exportacion(solicitud, "Casa Matriz")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNotNone(response.message)

    def test_facturacion_masiva_ReturnOK(self):
        credenciales = Credenciales(
            rut_emisor="76269769-6",
            nombre_sucursal="Casa Matriz"
        )
        path_csv = r"C:\Users\perea\Downloads\ejemplo_carga_masiva_nacional.csv"
        
        response = self.service.facturacion_Masiva(credenciales, path_csv)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)

    def test_facturacion_masiva_BadRequest_WhenCsvIsInvalid(self):
        credenciales = Credenciales(
            rut_emisor="76269769-6",
            nombre_sucursal="Casa Matriz"
        )
        path_csv = r"C:\Users\perea\Downloads\ejemplo_carga_masiva_nacional52.csv"
        
        response = self.service.facturacion_Masiva(credenciales, path_csv)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)
    
    def test_facturacion_masiva_ServerError(self):
        credenciales = Credenciales(
            rut_emisor="",
            nombre_sucursal=""
        )
        path_csv = r"C:\Users\perea\Downloads\SinDatos.csv"

        response = self.service.facturacion_Masiva(credenciales, path_csv)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNotNone(response.message)

    def test_EmisionNC_ND_V2_ReturnOK(self):

        #solicitudFolio= FolioRequest(
        #    credenciales=Credenciales(
        #        rut_emisor = "76269769-6",
        #        nombre_sucursal = "Casa Matriz"
        #    ),
        #    Cantidad= 1,
        #    CodigoTipoDte=61
        #)
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
        

        #responseFolio = self.service_folios.SolicitarFolios(solicitudFolio)
        response = self.service.EmisionNC_ND_V2(solicitud, "Casa Matriz", motivo)
        print(response.message)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        self.assertIsNotNone(response.data.folio)

        self.assertIsNotNone(responseFolio)
        self.assertIsInstance(responseFolio, Response)
        self.assertEqual(responseFolio.status, 200)
        self.assertIsNotNone(responseFolio.data)

    def test_EmisionNC_ND_V2_BadRequest_WhenSucursalIsInavlid(self):
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

        response = self.service.EmisionNC_ND_V2(solicitud, 1, motivo)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_EmisionNC_ND_V2_BadRequest_WhenMotivoIsInvalid(self):
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

        response = self.service.EmisionNC_ND_V2(solicitud, "Casa Matriz", "Motivo")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_EmisionNC_ND_V2_BadRequest_WhenDataIsInvalid(self):
        solicitud = RequestDTE(
            Documento=Documento(
                Encabezado=Encabezado(
                    IdDoc=IdDoc(
                        TipoDTE=None,
                        FchEmis="",
                        FmaPago=2,
                        FchVenc=""
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

        response = self.service.EmisionNC_ND_V2(solicitud, "Casa Matriz", motivo)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_EmisionNC_ND_V2_ServerError(self):
        solicitud = RequestDTE(
        )
        motivo = ReasonTypeEnum.Otros.value

        response = self.service.EmisionNC_ND_V2(solicitud, "Casa Matriz", motivo)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNotNone(response.message)

    def test_ListadoDteEmitidos_ReturnOK(self):
        fecha_desde = datetime.strptime("2024-08-01", "%Y-%m-%d")
        fecha_hasta = datetime.strptime("2024-08-17", "%Y-%m-%d")
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

        response = self.service.listadoDteEmitidos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        for dte in response.data:
            self.assertIsNotNone(dte.folio)
            self.assertIsNotNone(dte.ambiente)
            self.assertIsNotNone(dte.folioReutilizado)

    def test_ListadoDteEmitidos_BadRequest_WhenDataIsInvalid(self):
        fecha_desde = datetime.strptime("2024-08-01", "%Y-%m-%d")
        fecha_hasta = datetime.strptime("2024-08-17", "%Y-%m-%d")
        solicitud = ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="",
                rut_contribuyente="",
                nombre_sucursal=""
            ),
            ambiente=AmbienteEnum.Certificacion,
            folio=0,
            codigoTipoDte=DTEType.NotSet,
            desde=fecha_desde,
            hasta=fecha_hasta
        )

        response = self.service.listadoDteEmitidos(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_enviarCorreo_ReturnOK(self):
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

        response = self.service.enviarCorreo(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)

    def test_enviarCorreo_BadRequest_WhenDataIsInvalid(self):
        solicitud = EnvioMailRequest(
                RutEmpresa="",
                Dte= DteClass(folio=None, tipoDTE=None),
                Mail= MailClass(
                    to=["contacto@chilesystems.com"],
                    ccos=["correo@gmail.com"],
                    ccs=["correo2@gmail.com"]
                ),
                Xml=True,
                Pdf=True,
                Comments="ESTO ES UN COMENTARIO"
            )

        response = self.service.enviarCorreo(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_enviarCorreo_ServerError(self):
        # Mock de solicitud vacía
        solicitud = EnvioMailRequest(
            RutEmpresa="",
            Dte=DteClass(folio=None, tipoDTE=None),
            Mail=MailClass(
                to=[],
                ccos=[],
                ccs=[]
            ),
            Xml=False,
            Pdf=False,
            Comments=""
        )

        with patch('SimpleFacturaSDK.services.FacturaService.requests.Session.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.text = "Error interno del servidor"
            response = self.service.enviarCorreo(solicitud)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, Response)
            self.assertEqual(response.status, 500)
            self.assertIsNotNone(response.message)
            self.assertIn("Error interno del servidor", response.message)

    def test_consolidadoVentas_ReturnOK(self):
        fecha_desde = datetime.strptime("2023-10-25", "%Y-%m-%d")
        fecha_hasta = datetime.strptime("2023-10-30", "%Y-%m-%d")
        solicitud = ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            ambiente=AmbienteEnum.Certificacion,
            desde=fecha_desde,
            hasta=fecha_hasta
        )

        response = self.service.consolidadoVentas(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)
        for dte in response.data:
            self.assertIsNotNone(dte.total)
            self.assertIsNotNone(dte.anulados)
    
    def test_consolidadoVentas_ServerError(self):
        fecha_desde = datetime.strptime("2023-10-25", "%Y-%m-%d")
        fecha_hasta = datetime.strptime("2023-10-30", "%Y-%m-%d")
        solicitud = ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor=""
            ),
            ambiente=AmbienteEnum.Certificacion,
            desde=fecha_desde,
            hasta=fecha_hasta
        )

        response = self.service.consolidadoVentas(solicitud)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNotNone(response.message)

    def test_conciliarEmitidos_ReturnOK(self):
        solicitud =Credenciales(
            rut_emisor="76269769-6"
        )

        response = self.service.ConciliarEmitidos(solicitud,5, 2024)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 200)
        self.assertIsNotNone(response.data)

    def test_conciliarEmitidos_BadRequest_WhenMesIsInvalid(self):
        solicitud = Credenciales(
            rut_emisor="76269769-6"
        )

        response = self.service.ConciliarEmitidos(solicitud, "5", 2024)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)

    def test_conciliarEmitidos_BadRequest_WhenAnioIsInvalid(self):
        solicitud = Credenciales(
            rut_emisor="76269769-6"
        )

        response = self.service.ConciliarEmitidos(solicitud, 5, "2024")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 400)
        self.assertIsNotNone(response.message)
        
    def test_conciliarEmitidos_ServerError(self):
        solicitud = Credenciales(
            rut_emisor=""
        )

        response = self.service.ConciliarEmitidos(solicitud, 5, 2024)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, 500)
        self.assertIsNotNone(response.message)
