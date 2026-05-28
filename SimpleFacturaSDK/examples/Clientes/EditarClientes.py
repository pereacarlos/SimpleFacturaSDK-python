import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Productos.DatoExternoRequest import DatoExternoRequest
from SimpleFacturaSDK.models.Clientes.EditarDatosClienteExternoEnt import EditarDatosClienteExternoEnt
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= DatoExternoRequest(
            Credenciales=Credenciales(
                rut_emisor="78181331-1",
                nombre_sucursal="Casa Matriz"
            ),
            Clientes=[
                EditarDatosClienteExternoEnt(
                    Rut="77123456-9",
                    RazonSocial="Cliente Test 1",
                    Giro="Giro 1",
                    DirPart="direccion 1",
                    DirFact="direccion 1",
                    CorreoPar="modificado@123.cl",
                    CorreoFact="modificado@123.cl",
                    Ciudad="Ciudad 1",
                    Comuna="Comuna 1"
                ),
                EditarDatosClienteExternoEnt(
                    Rut="20852552-2",
                    RazonSocial="Cliente Test 2",
                    Giro="Giro 2",
                    DirPart="direccion 2",
                    DirFact="direccion 2",
                    CorreoPar="modificado@321.cl",
                    CorreoFact="modificado@321.cl",
                    Ciudad="Ciudad 2",
                    Comuna="Comuna 2"
                ),
                EditarDatosClienteExternoEnt(
                    Rut="9813831-5",
                    RazonSocial="Cliente Test 3",
                    Giro="Giro 3",
                    DirPart="direccion 3",
                    DirFact="direccion 3",
                    CorreoPar="modificado@456.cl",
                    CorreoFact="modificado@456.cl",
                    Ciudad="Ciudad 3",
                    Comuna="Comuna 3"
                )
            ]
        )
        try:
            UpdateClient = await client_api.Clientes.Actualizar_Clientes(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {UpdateClient.status}")
            print(f"Message: {UpdateClient.message}")
            
            for cliente in UpdateClient.data:
                print(f"RUT: {cliente.rut}")
                print(f"Dv: {cliente.dv}")
                print(f"RutFormateado: {cliente.rutFormateado}")
                print(f"RazonSocial: {cliente.razonSocial}")
                print(f"NombreFantasia: {cliente.nombreFantasia}")
                print(f"Giro: {cliente.giro}")
                print(f"DirPart: {cliente.dirPart}")
                print(f"DirFact: {cliente.dirFact}")
                print(f"CorreoPar: {cliente.correoPar}")
                print(f"CorreoFact: {cliente.correoFact}")
                print(f"Ciudad: {cliente.ciudad}")
                print(f"Comuna: {cliente.comuna}")
                print(f"Activo: {cliente.activo}")
                print("\n")
        except Exception as err:
            print(f"Error: {err}")
        finally:
            await client_api.Clientes.close()
       
if __name__ == "__main__":
    asyncio.run(main())
    