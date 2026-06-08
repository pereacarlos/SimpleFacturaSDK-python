import asyncio
import os

from dotenv import load_dotenv

from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.ListaProveedorEnum import ListaProveedorEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Proveedores.AgregarProveedorExternoRequest import AgregarProveedorExternoRequest
from SimpleFacturaSDK.models.Proveedores.ProveedorExternoEnt import NuevoProveedorExternoEnt

load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")


async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = AgregarProveedorExternoRequest(
            Credenciales=Credenciales(rut_emisor="78181331-1"),
            Proveedores=[
                NuevoProveedorExternoEnt(
                    Rut="85101774-7",
                    RazonSocial="Empresa Proveedor SpA",
                    Giro="Servicios de Tecnología",
                    DirFact="Av. Providencia 1234, Of. 5",
                    CorreoPar="contacto@proveedor.cl",
                    Ciudad="Santiago",
                    Comuna="Providencia",
                    CorreoFact="dte@proveedor.cl",
                    ListaProveedor=ListaProveedorEnum.ListaBlanca,
                )
            ],
        )
        try:
            proveedores = await client_api.Proveedores.AgregarProveedores(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {proveedores.status}")
            print(f"Message: {proveedores.message}")
            for proveedor in proveedores.data or []:
                print(f"RUT: {proveedor.rut}")
                print(f"RazonSocial: {proveedor.razonSocial}")
                print(f"ListaProveedor: {proveedor.listaProveedor}")
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    asyncio.run(main())
