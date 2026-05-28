import asyncio
import os

from dotenv import load_dotenv

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Cesiones.CesionTrazaRequest import CesionTrazaRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = CesionTrazaRequest(
            credenciales=Credenciales(rut_emisor="78181331-1"),
            folio=6627,
            ambiente=0
        )
        try:
            respuesta = await client_api.CesionService.obtener_TrazasCesionEmitida(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {respuesta.status}")
            print(f"Message: {respuesta.message}")
            print(f"Data: {respuesta.data}")
            print(f"Errors: {respuesta.errors}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())
