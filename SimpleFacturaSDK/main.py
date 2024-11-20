import asyncio
from ClientSimpleFactura import ClientSimpleFactura
from models.ResponseDTE import Response
import json
from models.GetFactura.Credenciales import Credenciales
async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
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
    finally:
        await client_api.Productos.close()
if __name__ == "__main__":
    asyncio.run(main())
    
