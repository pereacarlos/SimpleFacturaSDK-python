
import asyncio
from ClientSimpleFactura import ClientSimpleFactura
from models.GetFactura.Credenciales import Credenciales
async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
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
    finally:
        await client_api.Sucursales.close()
       
if __name__ == "__main__":
    asyncio.run(main())
    

    
