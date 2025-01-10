#Listar sucursales
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= Credenciales(rut_emisor="76269769-6")

        try:
            ListSucursal = await client_api.Sucursales.ListarSucursales(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListSucursal.status}")
            print(f"Message: {ListSucursal.message}")
            for cliente in ListSucursal.data:
                print(f"Nombre: {cliente.nombre}")
                print(f"Direccion: {cliente.direccion}")
                print("\n")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
    