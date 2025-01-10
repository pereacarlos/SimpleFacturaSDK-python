#FoliosSin Uso
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Folios.SolicitudFolios import SolicitudFolios
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= SolicitudFolios(
            RutEmpresa = "76269769-6",
            TipoDTE = 33,
            Ambiente = 0
        )
        try:
            FolioSinUsar = await client_api.Folios.Folios_Sin_Uso(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {FolioSinUsar.status}")
            print(f"Message: {FolioSinUsar.message}")
            print(f"Data: {FolioSinUsar.data}")
            for data in FolioSinUsar.data:
                print(f"desde: {data.desde}")
                print(f"hasta: {data.hasta}")
                print(f"Cantidad: {data.cantidad}")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
