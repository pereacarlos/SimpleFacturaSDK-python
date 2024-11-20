import asyncio

from ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
import json
from models.ResponseDTE import Response
from enumeracion.Ambiente import AmbienteEnum
from enumeracion.TipoDTE import DTEType
from models.GetFactura.Credenciales import Credenciales
from models.Productos.DatoExternoRequest import DatoExternoRequest
from models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from models.Clientes.NuevoReceptorExternoRequest import NuevoReceptorExternoRequest

async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
    solicitud= DatoExternoRequest(
        Credenciales=Credenciales(
            rut_emisor="76269769-6",
            nombre_sucursal="Casa Matriz"
        ),
        Clientes=[
            NuevoReceptorExternoRequest(
                Rut="57681892-0",
                RazonSocial="Cliente Test 1",
                Giro="Giro 1",
                DirPart="direccion 1",
                DirFact="direccion 1",
                CorreoPar="correo 1",
                CorreoFact="correo 1",
                Ciudad="Ciudad 1",
                Comuna="Comuna 1"
            ),
            NuevoReceptorExternoRequest(
                Rut="56516677-8",
                RazonSocial="Cliente Test 2",
                Giro="Giro 2",
                DirPart="direccion 2",
                DirFact="direccion 2",
                CorreoPar="correo 2",
                CorreoFact="correo 2",
                Ciudad="Ciudad 2",
                Comuna="Comuna 2"
            ),
            NuevoReceptorExternoRequest(
                Rut="68959276-7",
                RazonSocial="Cliente Test 3",
                Giro="Giro 3",
                DirPart="direccion 3",
                DirFact="direccion 3",
                CorreoPar="correo 3",
                CorreoFact="correo 3",
                Ciudad="Ciudad 3",
                Comuna="Comuna 3"
            )
        ]
    )

    try:
        AddClient = await client_api.Clientes.CrearClientes(solicitud)
        print("\nDatos de la Respuesta:")
        print(f"Status: {AddClient.status}")
        print(f"Message: {AddClient.message}")
        
        for cliente in AddClient.data:
            print(f"ReceptorId: {cliente.receptorId}")
            print(f"EmisorId: {cliente.emisorId}")
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
    


    