import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import MagicMock, patch
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
from SimpleFacturaSDK.services.FacturaService import FacturacionService

class TestFacturacionService(unittest.TestCase):
    def setUp(self):
        self.session = MagicMock()
        self.base_url = "https://api.simplefactura.cl"
        self.service = FacturacionService(self.session, self.base_url)

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
        self.session.post.return_value.status_code = 200
        self.session.post.return_value.content = b'PDF_CONTENT'
        pdf = self.service.obtener_pdf(solicitud)

        self.session.post.assert_called_once_with(
            f"{self.base_url}/dte/pdf",
            json={
                "credenciales": {
                    "rutEmisor": "76269769-6",
                    "nombreSucursal": "Casa Matriz",
                    "emailUsuario": None,
                    "rutContribuyente": None
                },
                "dteReferenciadoExterno": {
                    "folio": 4117,
                    "codigoTipoDte": 33,
                    "ambiente": 0
                }
            }
        )
        self.assertEqual(pdf, b'PDF_CONTENT')

    def test_obtener_pdf_error(self):
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

        self.session.post.return_value.status_code = 400
        self.session.post.return_value.text = "Error al obtener PDF"

        with self.assertRaises(Exception) as context:
            self.service.obtener_pdf(solicitud)

        self.assertEqual(str(context.exception), "Error en la petición: Error al obtener PDF")

if __name__ == '__main__':
    unittest.main()