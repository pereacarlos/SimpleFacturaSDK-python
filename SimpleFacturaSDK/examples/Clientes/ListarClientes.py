
#Listar Clientes
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
       
if __name__ == "__main__":
    asyncio.run(main())
   