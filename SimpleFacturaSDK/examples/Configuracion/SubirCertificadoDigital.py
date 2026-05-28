import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.CertificadoDigitalRequest import CertificadoDigitalRequest
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = CertificadoDigitalRequest(
            Credenciales=Credenciales(
                rut_emisor="78181331-1"
            ),
            RutCertificado="17096073-4",
            Password="*******"
        )
        """ruta donde se encuentra el certificado digital, debe ser un archivo .pfx"""
        certificado = r"C:\Users\nombre\Downloads\NoBorar\Certificado.pfx"
        try:
            certificadoDigital = await client_api.ConfiguracionService.subir_Certificado_Digital(solicitud, certificado)
            print("\nDatos de la Respuesta:")
            print(certificadoDigital.data)
            print("Status Code:", certificadoDigital.status)
            print("Message:", certificadoDigital.message)
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())