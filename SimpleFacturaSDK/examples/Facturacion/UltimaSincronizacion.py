from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.SyncTypeEnum import SyncTypeEnum
from SimpleFacturaSDK.models.GetFactura.UltimaSyncRequest import UltimaSyncRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import asyncio
import httpx
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = UltimaSyncRequest(
            Credenciales=Credenciales(
                rut_emisor="78181331-1"
            ),
            Tipo=SyncTypeEnum.Ventas
        )

        try:
            ultimaSync = await client_api.Facturacion.ultima_sincronizacion(solicitud, mes=10, anio=2025)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ultimaSync.status}")
            print(f"Message: {ultimaSync.message}")
            print(f"Data: {ultimaSync.data}")
            print(f"Errors: {ultimaSync.errors}")
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())