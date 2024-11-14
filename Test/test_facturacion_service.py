import unittest
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte

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
            print("Prueba exitosa, el PDF fue obtenido correctamente.")
        else:
            print(f"Error en la petición: {response['error']}")
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
        print("Prueba para código 400: Prueba exitosa, se obtuvo el error 400 esperado.")

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
            self.assertGreater(len(response["content"]), 0, "El PDF no debe estar vacío")
            print("Prueba exitosa, el timbre fue obtenido correctamente.")
        else:
            print(f"Error en la petición: {response['error']}")
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
        print("Prueba para código 400: Prueba exitosa, se obtuvo el error 400 esperado.")

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
            self.assertGreater(len(response["content"]), 0, "El PDF no debe estar vacío")
            print("Prueba exitosa, el XML fue obtenido correctamente.")
        else:
            print(f"Error en la petición: {response['error']}")
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
        print("Prueba para código 400: Prueba exitosa, se obtuvo el error 400 esperado.")



if __name__ == '__main__':
    unittest.main()
