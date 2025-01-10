#ConsultarFolios
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= FolioRequest(
            credenciales=Credenciales(
                rut_emisor = "76269769-6",
                nombre_sucursal = "Casa Matriz"
            ),
            CodigoTipoDte= None,
            Ambiente=0
        )
        try:
            ConsultarFolios = await client_api.Folios.ConsultarFolios(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ConsultarFolios.status}")
            print(f"Message: {ConsultarFolios.message}")
            print(f"Data: {ConsultarFolios.data}")
            for folio in ConsultarFolios.data:
                print(f"folio: {folio.foliosDisponibles}")
                print(f"codigoSii: {folio.codigoSii}")
                print(f"fechaIngreso: {folio.fechaIngreso}")
                print(f"desde: {folio.desde}")
                print(f"hasta: {folio.hasta}")

        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())
