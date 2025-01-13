#Crear productos
import asyncio
import json
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Productos.DatoExternoRequest import DatoExternoRequest
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Productos=[
                NuevoProductoExternoRequest(
                    nombre="NOmGoma 26",
                    codigoBarra="NOMGoma 25",
                    unidadMedida="un",
                    precio=50,
                    exento=False,
                    tieneImpuestos=False,
                    impuestos=[0]
                ),
                NuevoProductoExternoRequest(
                    nombre="NOMGoma 2122",
                    codigoBarra="NOMGoma 2212",
                    unidadMedida="un",
                    precio=50,
                    exento=False,
                    tieneImpuestos=True,
                    impuestos=[ 271,23]
                
                )
            ]
        )
        try:
            addProducts = await client_api.Productos.CrearProducto(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {addProducts.status}")
            print(f"Message: {addProducts.message}")
            for productos in addProducts.data:
                print(f"ProductoId: {productos.productoId}")
                print(f"Nombre: {productos.nombre}")
                print(f"Precio: {productos.precio}")
                print(f"Exento: {productos.exento}")
                print(f"Activo: {productos.activo}")
                print(f"EmisorId: {productos.emisorId}")
                print(f"SucursalId: {productos.sucursalId}")
                print(f"Impuestos: {productos.impuestos}")
                print(f"CodigoBarra: {productos.codigoBarra}")
                print(f"UnidadMedida: {productos.unidadMedida}")
                print(f"NombreCategoria: {productos.NombreCategoria}")
                print(f"NombreMarca: {productos.NombreMarca}")
                print(f"Stock: {productos.Stock}")
                print("\n")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())