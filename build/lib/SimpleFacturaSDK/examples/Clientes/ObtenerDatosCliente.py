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
        rutCliente = "17096073-4"

        try:
            response = await client_api.Clientes.ObtenerDatosCliente(solicitud, rutCliente)
            print("\nDatos de la Respuesta:")
            print(f"Status: {response.status}")
            print(f"Message: {response.message}")
            if response.data:
                print(f"RUT: {response.data.rut}")
                print(f"DV: {response.data.dv}")
                print(f"Rut Formateado: {response.data.rutFormateado}")
                print(f"Razon Social: {response.data.razonSocial}")
                print(f"Nombre Fantasia: {response.data.nombreFantasia}")
                print(f"Giro: {response.data.giro}")
                print(f"DirParticular: {response.data.dirPart}")
                print(f"DirFantacia: {response.data.dirFact}")
                print(f"Correo particular: {response.data.correoPar}")
                print(f"Correo Fantacia: {response.data.correoFact}")
                print(f"Comuna: {response.data.comuna}")
                print(f"Ciudad: {response.data.ciudad}")
                print(f"Activo: {response.data.activo}")
            print("\n")
        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())
   