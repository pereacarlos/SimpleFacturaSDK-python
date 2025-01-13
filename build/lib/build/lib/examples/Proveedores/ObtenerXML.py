#Obtener XML Proveedores
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud=ListaDteRequestEnt(
            Credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente="96689310-9"
            ),
            ambiente=AmbienteEnum.Produccion,
            folio= 7366834,
            codigoTipoDte=DTEType.NotaCreditoElectronica
        )
        try:
            Obtenerxml = await client_api.Proveedores.obtenerXml(solicitud)
            ruta = "xml2.xml"
            with open(ruta, "wb") as file:
                file.write(Obtenerxml.data)
            print(f"XML guardado en {ruta}")

        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())