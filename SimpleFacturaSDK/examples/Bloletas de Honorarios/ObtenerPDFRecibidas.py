#Obtener PDF Recibidas Boleta de Honorarios
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= BHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente= "26429782-6"
            ),
            Folio=2
        )
        try:
            ObtenerPdfRecibida = await client_api.BoletaHonorarioService.ObtenerPdfBoletaRecibida(solicitud)
            ruta = "BoletaHonorarioRecibida.pdf"
            with open(ruta, "wb") as archivo:
                archivo.write(ObtenerPdfRecibida.data)
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
    