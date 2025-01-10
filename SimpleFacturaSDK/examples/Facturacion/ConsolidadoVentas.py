#ConsolidadoVentas

import asyncio
import httpx
import requests
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
fecha_desde = datetime.strptime("2023-10-25", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2023-10-30", "%Y-%m-%d")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            ambiente=AmbienteEnum.Certificacion,
            desde=fecha_desde,
            hasta=fecha_hasta
        )
        try:
            Consolidado = await client_api.Facturacion.consolidadoVentas(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {Consolidado.status}")
            print(f"Message: {Consolidado.message}")
            for item in Consolidado.data:
                print(f"fecha: {item.fecha}")
                print(f"tipoDTE: {item.tiposDTE}")
                print(f"Emitidos: {item.emitidos}")
                print(f"anulados: {item.anulados}")
                print(f"total: {item.total}")
                print(f"totalNeto: {item.totalNeto}")
                print(f"totalIva: {item.totalIva}")
                print(item)
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
        
if __name__ == "__main__":
    asyncio.run(main())