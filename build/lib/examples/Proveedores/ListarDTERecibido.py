#ListarDTERecibido Proveedores
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
fecha_desde = datetime.strptime("2024-04-01", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2024-04-30", "%Y-%m-%d")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= None,
            codigoTipoDte=None,
            desde=fecha_desde,
            hasta=fecha_hasta,
        )
        try:
            ListProveedores = await client_api.Proveedores.listarDteRecibidos(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListProveedores.status}")
            print(f"Message: {ListProveedores.message}")
            for lista in ListProveedores.data:
                print(f"Ambiente: {lista.ambiente}")
                print(f"codigoSii: {lista.codigoSii}")
                print(f"Tipo DTE: {lista.tipoDte}")
                print(f"estadoSII: {lista.estadoSII}")
                print(f"estado: {lista.estado}")
                print(f"folio: {lista.folio}")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())