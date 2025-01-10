
#ConciliarEmitidoss
import asyncio
import httpx
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import requests
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud =Credenciales(
            rut_emisor="76269769-6"
        )
        try:
            Conciliar = await client_api.Facturacion.ConciliarEmitidos(solicitud,5,2024)
            print("\nDatos de la Respuesta:")
            print(f"Status: {Conciliar.status}")
            print(f"Message: {Conciliar.message}")
            print(f"Data: {Conciliar.data}")
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())