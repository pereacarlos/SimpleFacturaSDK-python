import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.BoletaHonorarios import BHData
from SimpleFacturaSDK.models.BoletaHonorarios.BHData import Emisor, Receptor, Detalle
from SimpleFacturaSDK.enumeracion.TipoRetencion import TipoRetencion
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = BHData(
            RutEmisor="78181331-1",
            Retencion=TipoRetencion.Contribuyente,
            FechaEmision="28-05-2026",
            Emisor=Emisor(Rut="17096073-4", Direccion="0"),
            Receptor=Receptor(
                Rut="76269769-6",
                Nombre="servicios",
                Direccion="Pasaje amancai 4642",
                Comuna="Puente Alto",
                Region=13
            ),
            Detalles=[
                Detalle(
                    Nombre="servicios",
                    Valor=500
                )
            ]
        )
        try:
            EmitirBHE = await client_api.BoletaHonorarioService.EmitirBHETerceros(solicitud)
            print("\nDatos de la Respuesta:")
            print(EmitirBHE.data)
            print("Status Code:", EmitirBHE.status)
            print("Message:", EmitirBHE.message)
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())