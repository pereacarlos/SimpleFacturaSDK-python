#Datos Empresas
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
            rut_emisor="76269769-6"
        )
        try:
            DatosEmpresa = await client_api.ConfiguracionService.datos_empresa(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {DatosEmpresa.status}")
            print(f"Message: {DatosEmpresa.message}")
            print(f"Data: {DatosEmpresa.data}")
            print(f"rut: {DatosEmpresa.data.rut}")
            print(f"razonSocial: {DatosEmpresa.data.razonSocial}")
            print(f"giro: {DatosEmpresa.data.giro}")
    
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())