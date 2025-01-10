#Obtener DtE de una factura
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
import json
import base64
import requests
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="76269769-6"
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=12553,
                codigoTipoDte=39,
                ambiente=0
            )
        )
        try:
            dte_bytes = await client_api.Facturacion.obtener_dte(solicitud)
            print(f"Status: {dte_bytes.status}")
            print(f"Message: {dte_bytes.message}")
            print(f"TipoDTE: {dte_bytes.data.tipoDte}")
            print(f"folioReutilizado: {dte_bytes.data.folioReutilizado}")
            print(f"fechaCreacionr: {dte_bytes.data.fechaCreacion}")
            print(f"Folio: {dte_bytes.data.folio}")
            print(f"razonSocialReceptor: {dte_bytes.data.razonSocialReceptor}")
            print(f"iva: {dte_bytes.data.iva}")
            print(dte_bytes.data)

        except requests.exceptions.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
            print("Detalle del error:", http_err.response.text)
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())