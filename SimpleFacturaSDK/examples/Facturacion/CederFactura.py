import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.CesionDteRequest import CesionDteRequest
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= CesionDteRequest(
            RutCesionario= "17432554-5",
            RutPersonaAutorizada= "17096073-4",
            RutEmpresa= "76269769-6",
            Folio= 2232,
            CorreoDeudor= "correoCesionario@gmail.cl",
            OtrasCondiciones= "otras"
        )

        try:
            response = await client_api.Facturacion.ceder_Factura(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {response.status}")
            print(f"Message: {response.message}")
            print(f"Data: {response.data}")
            
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
   