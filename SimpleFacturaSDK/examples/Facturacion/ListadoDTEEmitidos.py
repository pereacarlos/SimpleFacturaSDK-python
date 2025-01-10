#ListadoDTEEmitidos
import asyncio
import httpx
import requests
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
fecha_desde = datetime.strptime("2024-08-01", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2024-08-17", "%Y-%m-%d")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente="10422710-4",
                nombre_sucursal="Casa Matriz"
            ),
            ambiente=AmbienteEnum.Certificacion,
            folio=0,
            codigoTipoDte=DTEType.NotSet,
            desde=fecha_desde,
            hasta=fecha_hasta
        )
        try:
            Listado = await client_api.Facturacion.listadoDteEmitidos(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {Listado.status}")
            print(f"Message: {Listado.message}")
            for dte in Listado.data:
                print(f"ambiente: {dte.ambiente}")
                print(f"tipoDTE: {dte.tipoDte}")
                print(f"folioReutilizado: {dte.folioReutilizado}")
                print(f"fechaCreacion: {dte.fechaCreacion}")
                print(f"Folio: {dte.folio}")
                print(f"razonSocialReceptor: {dte.razonSocialReceptor}")
                print(f"Total: {dte.total}")
                print(dte)
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
	
if __name__ == "__main__":
    asyncio.run(main())