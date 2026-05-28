import asyncio
import os
from datetime import datetime

from dotenv import load_dotenv

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Cesiones.ListaCesionRequest import ListaCesionRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = ListaCesionRequest(
            credenciales=Credenciales(rut_emisor="78181331-1",nombre_sucursal ="Cas Matriz"),
            ambiente=0,
            desde=datetime.strptime("2025-07-01", "%Y-%m-%d"),
            hasta=datetime.strptime("2025-07-31", "%Y-%m-%d"),
        )
        try:
            respuesta = await client_api.CesionService.listado_CesionesEmitidas(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {respuesta.status}")
            print(f"Message: {respuesta.message}")
            print(f"Data: {respuesta.data}")
            print(f"Errors: {respuesta.errors}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())
