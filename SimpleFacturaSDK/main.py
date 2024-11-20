import asyncio

from ClientSimpleFactura import ClientSimpleFactura
from models.GetFactura.Credenciales import Credenciales

async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
    solicitud= Credenciales(rut_emisor="76269769-6")


    try:
        ListClient = await client_api.Clientes.ListarClientes(solicitud)
        print("\nDatos de la Respuesta:")
        print(f"Status: {ListClient.status}")
        print(f"Message: {ListClient.message}")
        for cliente in ListClient.data:
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
    


    