import asyncio
import os

from dotenv import load_dotenv

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Proveedores.ListarProveedoresRequest import ListarProveedoresRequest

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = ListarProveedoresRequest(RutEmisor="78181331-1")

        try:
            proveedores = await client_api.Proveedores.ListarProveedores(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {proveedores.status}")
            print(f"Message: {proveedores.message}")
            for proveedor in proveedores.data or []:
                print(f"RUT: {proveedor.rut}")
                print(f"RazonSocial: {proveedor.razonSocial}")
                print(f"Giro: {proveedor.giro}")
                print(f"DirFact: {proveedor.dirFact}")
                print(f"CorreoPar: {proveedor.correoPar}")
                print(f"Ciudad: {proveedor.ciudad}")
                print(f"Comuna: {proveedor.comuna}")
                print(f"CorreoFact: {proveedor.correoFact}")
                print(f"ListaProveedor: {proveedor.listaProveedor}")
                print(f"Activo: {proveedor.activo}")
                print("")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())
