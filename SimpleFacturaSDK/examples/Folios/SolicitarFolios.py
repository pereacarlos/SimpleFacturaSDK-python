#SolicitarFolios
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
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
            Cantidad= 3,
            CodigoTipoDte= DTEType.FacturaElectronica
        )
        try:
            SolicitarFolio = await client_api.Folios.SolicitarFolios(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {SolicitarFolio.status}")
            print(f"Message: {SolicitarFolio.message}")
            print(f"Data: {SolicitarFolio.data}")
            print(f"codigoSii: {SolicitarFolio.data.codigoSii}")
            print(f"fechaIngreso: {SolicitarFolio.data.fechaIngreso}")
            print(f"desde: {SolicitarFolio.data.desde}")
            print(f"hasta: {SolicitarFolio.data.hasta}")
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())