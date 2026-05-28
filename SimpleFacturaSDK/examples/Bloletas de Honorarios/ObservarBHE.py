import asyncio
import os

from dotenv import load_dotenv

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.ObservacionBoletaHonorario import ObservacionBoletaHonorario
from SimpleFacturaSDK.models.BoletaHonorarios.BheObservacionEnt import BheObservacionEnt

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = BheObservacionEnt(
            RutEmpresa="78181331-1",
            rutContribuyente="17096073-4",
            Folio=268,
            Observacion=ObservacionBoletaHonorario.NoReconoceRelacion
        )
        try:
            respuesta = await client_api.BoletaHonorarioService.ObservarBHE(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {respuesta.status}")
            print(f"Message: {respuesta.message}")
            print(f"Data: {respuesta.data}")
            print(f"Errors: {respuesta.errors}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())
