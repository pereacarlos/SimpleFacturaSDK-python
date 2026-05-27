
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.AnularGuiaRequest import AnularGuiaRequest
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= AnularGuiaRequest(RutEmpresa="78181331-1", Folio=568, Ambiente=0)

        try:
            anularGuiaRequest = await client_api.Facturacion.anular_guia(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {anularGuiaRequest.status}")
            print(f"Message: {anularGuiaRequest.message}")
            print(f"Data: {anularGuiaRequest.data}")
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())