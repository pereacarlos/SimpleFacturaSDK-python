import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.ReenvioSiiRequest import ReenvioSiiRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = ReenvioSiiRequest(
            Credenciales=Credenciales(
                rut_emisor="78181331-1"
            ),
            ambiente=AmbienteEnum.Certificacion,
            folio=9078,
            codigoTipoDte=DTEType.FacturaElectronica,
        )

        try:
            reenvioSii = await client_api.Facturacion.reenvio_Sii(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {reenvioSii.status}")
            print(f"Message: {reenvioSii.message}")
            print(f"Data: {reenvioSii.data}")
            print(f"Errors: {reenvioSii.errors}")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())