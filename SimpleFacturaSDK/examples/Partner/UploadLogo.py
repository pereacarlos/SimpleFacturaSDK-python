import asyncio
import os

from dotenv import load_dotenv

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        credenciales = Credenciales(rut_emisor="78181331-1")
        path_logo = r"C:\ruta\tu-logo.png"
        try:
            respuesta = await client_api.PartnerService.upload_logo(credenciales, path_logo)
            print("\nDatos de la Respuesta:")
            print(f"Status: {respuesta.status}")
            print(f"Message: {respuesta.message}")
            print(f"Data: {respuesta.data}")
            print(f"Errors: {respuesta.errors}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())
