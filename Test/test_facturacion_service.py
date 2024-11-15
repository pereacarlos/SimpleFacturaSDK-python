import unittest
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
import base64
import json
from requests.auth import HTTPBasicAuth
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
from SimpleFacturaSDK.models.GetFactura.InvoiceData import InvoiceData
from SimpleFacturaSDK.models.GetFactura.Documento import Documento
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


class TestFacturacionService(unittest.TestCase):
    def setUp(self):
        username = "demo@chilesystems.com"
        password = "Rv8Il4eV"
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.Facturacion

    def test_obtener_pdf_returnOK(self):
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

        response = self.service.obtener_pdf(solicitud)

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
        self.assertIsNotNone(response.errors)
        self.assertIn("validation errors", response.errors[0])

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
        self.assertIsNotNone(response.errors)
        self.assertIn("validation errors", response.errors[0])

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
        response = self.service.obtener_xml(solicitud, test=True)
        
        if response["status_code"] == 200:
            self.assertIsInstance(response["content"], bytes)
            self.assertGreater(len(response["content"]), 0, "El XML no debe estar vacío")
        else:
            self.assertIsNotNone(response["error"])
            self.fail(f"Solicitud fallida con código de estado {response['status_code']}")

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
        response = self.service.obtener_xml(solicitud, test=True)
        self.assertEqual(response["status_code"], 400)
        self.assertIsNotNone(response["error"])

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

        response = self.service.obtener_dte(solicitud, test=True)
        
        if response["status_code"] == 200:
            self.assertIsInstance(response["content"], bytes)
            self.assertGreater(len(response["content"]), 0, "El dte no debe estar vacío")

        else:
            self.assertIsNotNone(response["error"])
            self.fail(f"Solicitud fallida con código de estado {response['status_code']}")

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
        response = self.service.obtener_dte(solicitud, test=True)
        self.assertEqual(response["status_code"], 400)
        self.assertIsNotNone(response["error"])

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
        response = self.service.obtener_sobreXml(solicitud,0, test=True)
        
        if response["status_code"] == 200:
            self.assertIsInstance(response["content"], bytes)
            self.assertGreater(len(response["content"]), 0, "El sobre no debe estar vacío")
        else:
            self.assertIsNotNone(response["error"])
            self.fail(f"Solicitud fallida con código de estado {response['status_code']}")
    
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
        response = self.service.obtener_sobreXml(solicitud,0, test=True)
        self.assertEqual(response["status_code"], 400)
        self.assertIsNotNone(response["error"])

    def test_obtener_sobreXml_bad_request_WhenUrlIsInvalid(self):
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
        response = self.service.obtener_sobreXml(solicitud,"sdd", test=True)
        self.assertEqual(response["status_code"], 400)
        self.assertIsNotNone(response["error"])

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

        response = self.service.facturacion_individualV2_Dte(solicitud, "Casa Matriz", test=True)

        if response["status_code"] == 200:
            self.assertIsInstance(response["content"], InvoiceData)
            self.assertIsNotNone(response["content"].tipoDTE, "El tipoDTE no debe ser None")
            self.assertIsNotNone(response["content"].rutEmisor, "El rutEmisor no debe ser None")
            self.assertIsNotNone(response["content"].folio, "El folio no debe ser None")
        
        else:
            self.assertIsNotNone(response["error"])
            self.fail(f"Solicitud fallida con código de estado {response['status_code']}")




















if __name__ == '__main__':
    unittest.main()
