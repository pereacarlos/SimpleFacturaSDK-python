import asyncio
import os

from dotenv import load_dotenv

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Partner.PartnerDteResumenRequest import PartnerDteResumenRequest

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = PartnerDteResumenRequest(
            Credenciales=Credenciales(rut_emisor="78181331-1"),
            Anio=2025,
            Mes=10
        )
        try:
            respuesta = await client_api.PartnerService.obtener_resumen_dtes(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {respuesta.status}")
            print(f"Message: {respuesta.message}")
            print(f"Data: {respuesta.data}")
            print(f"Errors: {respuesta.errors}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())

