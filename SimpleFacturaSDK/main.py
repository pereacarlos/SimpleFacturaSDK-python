import asyncio
import httpx
from ClientSimpleFactura import ClientSimpleFactura
import requests
from models.GetFactura.Credenciales import Credenciales
async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
    solicitud =Credenciales(
        rut_emisor="76269769-6"
    )

    try:
        Conciliar = await client_api.Facturacion.ConciliarEmitidos(solicitud,5,2024)
        print("\nDatos de la Respuesta:")
        print(f"Status: {Conciliar.status}")
        print(f"Message: {Conciliar.message}")
        print(f"Data: {Conciliar.data}")


    except httpx.HTTPStatusError as err:
        print(f"Error: {err}")

    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    asyncio.run(main())
