import asyncio
import os
from datetime import datetime
from dotenv import load_dotenv
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.PlanUsuario import PlanUsuarioEnum
from SimpleFacturaSDK.models.Partner.WizardEmisorRequest import (
    EmisorReq,
    SucursalReq,
    WizardEmisorRequest,
)

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = WizardEmisorRequest(
            Emisor=EmisorReq(
                RutEmpresa="78181331-1",
                RazonSocial="CHILESYSTEMS SPA",
                RutRepresentanteLegal="17096073-4",
                Giro="Servicios",
                Email="demo@empresa.cl",
                DireccionFacturacion="Pasaje amancai 4642",
                Ciudad="Santiago",
                Comuna="Puente Alto",
                Telefono="56912345678",
                FechaResolucion=datetime.strptime("2025-02-05", "%Y-%m-%d"),
                NumeroResolucion=80,
                Ambiente=AmbienteEnum.Certificacion,
                PasswordSii=None,
                UnidadSii="Unidad SII",
            ),
            Sucursal=SucursalReq(
                Nombre="Casa Matriz",
                Direccion="Direccion 1",
            ),
            ActividadesEconomicas=[620100, 702000],
            Plan=PlanUsuarioEnum.Pyme,
        )
        try:
            respuesta = await client_api.PartnerService.enrolamiento_empresa(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {respuesta.status}")
            print(f"Message: {respuesta.message}")
            print(f"Data: {respuesta.data}")
            print(f"Errors: {respuesta.errors}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())

