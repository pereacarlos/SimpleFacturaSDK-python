import asyncio
import os

from dotenv import load_dotenv

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.AnulacionBoletaHonorario import AnulacionBoletaHonorario
from SimpleFacturaSDK.models.BoletaHonorarios.AnularBheEnt import AnularBheEnt

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = AnularBheEnt(
            RutEmpresa="78181331-1",
            Folio=96,
            Motivo=AnulacionBoletaHonorario.ServicioNoPagado
        )
        try:
            respuesta = await client_api.BoletaHonorarioService.AnularBHE(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {respuesta.status}")
            print(f"Message: {respuesta.message}")
            print(f"Data: {respuesta.data}")
            print(f"Errors: {respuesta.errors}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())
