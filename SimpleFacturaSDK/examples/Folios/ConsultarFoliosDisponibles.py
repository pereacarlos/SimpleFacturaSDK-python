#ConsultarFoliosDisponibles
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
            RutEmpresa="76269769-6",
            TipoDTE=33,
            Ambiente=0
        )


        try:
            ConsultaFolio = await client_api.Folios.ConsultaFoliosDisponibles(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ConsultaFolio.status}")
            print(f"Message: {ConsultaFolio.message}")
            print(f"Data: {ConsultaFolio.data}")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())