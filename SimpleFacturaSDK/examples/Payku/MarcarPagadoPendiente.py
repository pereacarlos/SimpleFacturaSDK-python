import asyncio
import os

from dotenv import load_dotenv

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.Payku.PaykuRequests import MarcarPagadoOPendienteRequest

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = MarcarPagadoOPendienteRequest(
            credenciales=Credenciales(rut_emisor="78181331-1"),
            dteReferenciadoExterno=DteReferenciadoExterno(
                folio=3591,
                codigoTipoDte=33,
                ambiente=0
            ),
            pagado=True
        )
        try:
            respuesta = await client_api.PaykuService.marcar_dte_pagado_o_pendiente(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {respuesta.status}")
            print(f"Message: {respuesta.message}")
            print(f"Data: {respuesta.data}")
            print(f"Errors: {respuesta.errors}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())
