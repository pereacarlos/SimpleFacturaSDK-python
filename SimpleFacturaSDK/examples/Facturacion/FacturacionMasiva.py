#Facturacion masiva 
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
        credenciales = Credenciales(
            rut_emisor="76269769-6",
            nombre_sucursal="Casa Matriz"
        )
        path_csv = r"C:\Users\perea\Downloads\ejemplo_carga_masiva_nacional.csv"
        try:
            factura = await client_api.Facturacion.facturacion_Masiva(credenciales, path_csv)
            print("\nDatos de la Respuesta:")
            print(factura.data)
            print("Status Code:", factura.status)
            print("Message:", factura.message)
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())