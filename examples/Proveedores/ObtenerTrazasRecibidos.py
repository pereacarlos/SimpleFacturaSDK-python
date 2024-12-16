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
                rut_emisor="76269769-6",
                rut_contribuyente="76269769-6",
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=2232,
                codigoTipoDte=33,
                ambiente=0
            )
        )
        try:
            trazas_bytes = await client_api.Facturacion.obtener_Trazas(solicitud)
            print(f"Status: {trazas_bytes.status}")
            print(f"Message: {trazas_bytes.message}")
            for trazas in dte_bytes.data:
                print(f"Fecha: {trazas.fecha}")
                print(f"Descripcion: {trazas.descripcion}")
                print(trazas)

        except requests.exceptions.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
            print("Detalle del error:", http_err.response.text)
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())