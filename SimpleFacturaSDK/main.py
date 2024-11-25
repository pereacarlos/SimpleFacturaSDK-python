import asyncio
from client_simple_factura import ClientSimpleFactura
from models.BoletaHonorarios.ListaBHERequest import ListaBHERequest
from models.GetFactura.Credenciales import Credenciales
from datetime import datetime
fecha_desde = datetime.strptime("2024-09-03", "%Y-%m-%d").isoformat()
fecha_hasta = datetime.strptime("2024-11-11", "%Y-%m-%d").isoformat()
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= ListaBHERequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz"
            ),
            Folio=None,
            Desde=fecha_desde,
            Hasta=fecha_hasta
        )


        try:
            ListadoBHERecibido = await client_api.BoletaHonorarioService.ListadoBHERecibido(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {ListadoBHERecibido.status}")
            print(f"Message: {ListadoBHERecibido.message}")
            for cliente in ListadoBHERecibido.data:
                print(f"fOLIO: {cliente.folio}")
                print(f"FECHAEMISION: {cliente.fechaEmision}")
                print("\n")  
    
        except Exception as err:
            print(f"Error: {err}")

if __name__ == "__main__":
    asyncio.run(main())