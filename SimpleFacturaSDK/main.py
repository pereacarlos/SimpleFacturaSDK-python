
import asyncio
import httpx
from ClientSimpleFactura import ClientSimpleFactura
import requests
from enumeracion.TipoDTE import DTEType
from models.GetFactura.EnvioMailRequest import EnvioMailRequest, DteClass, MailClass
async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
    solicitud = EnvioMailRequest(
        RutEmpresa="76269769-6",
        Dte= DteClass(folio=2149, tipoDTE=33),
        Mail= MailClass(
            to=["contacto@chilesystems.com"],
            ccos=["correo@gmail.com"],
            ccs=["correo2@gmail.com"]
        ),
        Xml=True,
        Pdf=True,
        Comments="ESTO ES UN COMENTARIO"
    )

    try:
        enviarCorreo = await client_api.Facturacion.enviarCorreo(solicitud)
        print("\nDatos de la Respuesta:")
        print(f"Status: {enviarCorreo.status}")
        print(f"Message: {enviarCorreo.message}")
        print(f"Data: {enviarCorreo.data}")
    except httpx.HTTPStatusError as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())
