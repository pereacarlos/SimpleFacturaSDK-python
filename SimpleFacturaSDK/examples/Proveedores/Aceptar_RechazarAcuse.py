#Aceptar o Rechazar Acuse Proveedores
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.Proveedores.AcuseReciboExternoRequest import AcuseReciboExternoRequest
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.enumeracion.ResponseType import ResponseType
from SimpleFacturaSDK.enumeracion.RejectionType import RejectionType
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import os
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
async def main():
    async with ClientSimpleFactura(username, password) as client_api:
        solicitud= AcuseReciboExternoRequest(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                rut_contribuyente= "77720532-3",
                nombre_sucursal="Casa Matriz"
            ),
            dteReferenciadoExterno=DteReferenciadoExterno(
                folio=220,
                codigoTipoDte=33,
                ambiente=0
            ),
            respuesta=ResponseType.Rejected,
            tipo_rechazo=RejectionType.RCD,
            comentario="test"
        )
        try:
            AceptarRecchazarAcuse = await client_api.Proveedores.Aceptar_RechazarDTE(solicitud)
            print(AceptarRecchazarAcuse)
            print("\nDatos de la Respuesta:")
            print(f"Status: {AceptarRecchazarAcuse.status}")
            print(f"Message: {AceptarRecchazarAcuse.message}")
            print(f"Data: {AceptarRecchazarAcuse.data}")

        except Exception as err:
            print(f"Error: {err}")
       
if __name__ == "__main__":
    asyncio.run(main())