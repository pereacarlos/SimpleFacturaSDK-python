
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
            ListUsuario = await client_api.Usuarios.ListarUsuario(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListUsuario.status}")
            print(f"Message: {ListUsuario.message}")
            for cliente in ListUsuario.data:
                print(f"Rut: {cliente.rut}")
                print(f"Nombre: {cliente.nombre}")
                print(f"Apellidos: {cliente.apellidos}")
                print(f"Email: {cliente.email}")
                print("\n")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())