#ConciliarRecibidos Proveedores
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud=Credenciales(rut_emisor="76269769-6")

        try:
            Obtener_pdf = await client_api.Proveedores.ConciliarRecibidos(solicitud,5,2024)
            print("\nDatos de la Respuesta:")
            print(f"Status: {Obtener_pdf.status}")
            print(f"Message: {Obtener_pdf.message}")
            print(f"Data: {Obtener_pdf.data}")

        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())