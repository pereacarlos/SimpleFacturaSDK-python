import asyncio

from ClientSimpleFactura import ClientSimpleFactura
from models.GetFactura.Credenciales import Credenciales

async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
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
    finally:
        await client_api.ConfiguracionService.close()
       
if __name__ == "__main__":
    asyncio.run(main())
    


    