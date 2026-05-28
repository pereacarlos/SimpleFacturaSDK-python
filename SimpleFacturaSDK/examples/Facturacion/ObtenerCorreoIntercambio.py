from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
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
        solicitud= Credenciales(rut_emisor="78181331-1")
        try:
            correo = await client_api.Facturacion.obtener_correo_intercambio(solicitud, rut_header="78181331-1")
            print("\nDatos de la Respuesta:")
            print(f"Status: {correo.status}")
            print(f"Message: {correo.message}")
            print(f"Data: {correo.data}")
            print(f"Errors: {correo.errors}")
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())