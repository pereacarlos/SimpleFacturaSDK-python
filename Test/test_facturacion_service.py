import unittest
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte

class TestFacturacionService(unittest.TestCase):
    def setUp(self):
        # Credenciales para autenticación
        username = "demo@chilesystems.com"
        password = "Rv8Il4eV"
    
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
        try:
            pdf = self.service.obtener_pdf(solicitud)
            
            self.assertIsInstance(pdf, bytes)
            print("Prueba exitosa, el PDF fue obtenido correctamente.")
        
        except Exception as e:
            print(f"Error en la petición: {e}")
            self.fail("La solicitud no devolvió un status 200 como se esperaba.")

if __name__ == '__main__':
    unittest.main()
