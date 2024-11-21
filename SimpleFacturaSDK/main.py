import asyncio

from ClientSimpleFactura import ClientSimpleFactura
from models.Folios.SolicitudFolios import SolicitudFolios

async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
    solicitud= SolicitudFolios(
        RutEmpresa = "76269769-6",
        TipoDTE = 33,
        Ambiente = 0
    )
    try:
        FolioSinUsar = await client_api.Folios.Folios_Sin_Uso(solicitud)
        print("\nDatos de la Respuesta:")
        print(f"Status: {FolioSinUsar.status}")
        print(f"Message: {FolioSinUsar.message}")
        print(f"Data: {FolioSinUsar.data}")
        for data in FolioSinUsar.data:
            print(f"desde: {data.desde}")
            print(f"hasta: {data.hasta}")
            print(f"Cantidad: {data.cantidad}")


    except Exception as err:
        print(f"Error: {err}")
    finally:
        await client_api.Folios.close()
       
if __name__ == "__main__":
    asyncio.run(main())
    


    