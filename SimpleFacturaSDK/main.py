
import asyncio
from ClientSimpleFactura import ClientSimpleFactura
from models.Folios.SolicitudFolios import SolicitudFolios
async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
    solicitud= SolicitudFolios(
        RutEmpresa="76269769-6",
        TipoDTE=33,
        Ambiente=0
    )


    try:
        ConsultaFolio = await client_api.Folios.ConsultaFoliosDisponibles(solicitud)
        print("\nDatos de la Respuesta:")
        print(f"Status: {ConsultaFolio.status}")
        print(f"Message: {ConsultaFolio.message}")
        print(f"Data: {ConsultaFolio.data}")

    except Exception as err:
        print(f"Error: {err}")
    finally:
        await client_api.Folios.close()
       
if __name__ == "__main__":
    asyncio.run(main())
