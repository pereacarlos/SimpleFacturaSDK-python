#Obtener PDF Emitidas Boleta de Honorarios
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
                rut_emisor="76269769-6"
            ),
            Folio=15
        )
        try:
            ObtenerPdf = await client_api.BoletaHonorarioService.ObtenerPdf(solicitud)
            ruta = "BoletaHonorario.pdf"
            with open(ruta, "wb") as archivo:
                archivo.write(ObtenerPdf.data)
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())