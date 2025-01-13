#Listar productos 
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
        solicitud= Credenciales(
            rut_emisor="76269769-6",
            nombre_sucursal="Casa Matriz"
        )
        try:
            ListProduct = await client_api.Productos.listarProductos(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListProduct.status}")
            print(f"Message: {ListProduct.message}")
            for i in ListProduct.data:
                print(f"productoId: {i.productoId}")
                print(f"nombre: {i.nombre}")
                print(f"precio: {i.precio}")
                print(f"exento: {i.exento}")
                for imp in i.impuestos:
                    print(f"codigoSii: {imp.codigoSii}")
                    print(f"nombreImp: {imp.nombreImp}")
                    print(f"tasa: {imp.tasa}")
    
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())