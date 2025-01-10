#EnviarCorreo
import asyncio
import httpx
import requests
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.EnvioMailRequest import EnvioMailRequest, DteClass, MailClass
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
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