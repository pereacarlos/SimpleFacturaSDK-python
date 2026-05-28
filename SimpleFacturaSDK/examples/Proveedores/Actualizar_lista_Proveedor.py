from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.ListaProveedorEnum import ListaProveedorEnum
from SimpleFacturaSDK.models.Proveedores.ListaProveedorRequest import ListaProveedorRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import asyncio
import httpx
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = ListaProveedorRequest(
            Credenciales=Credenciales(
                rut_emisor="78181331-1"
            ),
            RutProveedor="17432554-5",
            ListaProveedor=ListaProveedorEnum.ListaBlanca
        )

        try:
            updateListProveedor = await client_api.Proveedores.actualizar_Lista_Proveedor(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {updateListProveedor.status}")
            print(f"Message: {updateListProveedor.message}")
            print(f"Data: {updateListProveedor.data}")
            print(f"Errors: {updateListProveedor.errors}")
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())