import unittest
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
import base64
import json
from requests.auth import HTTPBasicAuth
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
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
        
        # Usa `ClientSimpleFactura` para configurar la autenticación correctamente
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.Facturacion

    def test_obtener_pdf(self):
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
        response = self.service.obtener_pdf(solicitud, test=True)
        
        if response["status_code"] == 200:
            self.assertIsInstance(response["content"], bytes)
            self.assertGreater(len(response["content"]), 0, "El PDF no debe estar vacío")
        else:
            self.assertIsNotNone(response["error"])
            self.fail(f"Solicitud fallida con código de estado {response['status_code']}")

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
        response = self.service.obtener_pdf(solicitud, test=True)
        self.assertEqual(response["status_code"], 400)
        self.assertIsNotNone(response["error"])

    def test_obtener_timbre(self):
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
        response = self.service.obtener_timbre(solicitud, test=True)
        
        if response["status_code"] == 200:
            self.assertIsInstance(response["content"], bytes)
            self.assertGreater(len(response["content"]), 0, "El Timbre no debe estar vacío")
        else:
            self.assertIsNotNone(response["error"])
            self.fail(f"Solicitud fallida con código de estado {response['status_code']}")

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
        response = self.service.obtener_timbre(solicitud, test=True)
        self.assertEqual(response["status_code"], 400)
        self.assertIsNotNone(response["error"])

    def test_obtener_xml(self):
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

    def test_obtener_dte(self):
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
if __name__ == '__main__':
    unittest.main()
