#AnularFolios
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Folios.AnularFoliosRequest import AnularFoliosRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= AnularFoliosRequest(
            credenciales=Credenciales(
                rut_emisor = "78181331-1",
                nombre_sucursal = "Casa Matriz"
            ),
            codigoTipoDte= DTEType.FacturaElectronica,
            ambiente=0,
            folioInicio=9262,
            folioTermino=9262,
            motivoAnulacion="Motivo de anulación"
        )
        try:
            AnularFolios = await client_api.Folios.anular_Folio(solicitud)
            print("\nDatos de la Respuesta:")
            print(f"Status: {AnularFolios.status}")
            print(f"Message: {AnularFolios.message}")
            print(f"Data: {AnularFolios.data}")
            print(f"Error: {AnularFolios.errors}")
        except Exception as err:
            print(f"Error: {err}")
if __name__ == "__main__":
    asyncio.run(main())
