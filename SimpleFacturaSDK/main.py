
import asyncio
from ClientSimpleFactura import ClientSimpleFactura
from models.Proveedores.AcuseReciboExternoRequest import AcuseReciboExternoRequest
from models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from enumeracion.ResponseType import ResponseType
from enumeracion.RejectionType import RejectionType
from models.GetFactura.Credenciales import Credenciales
from datetime import datetime
fecha_desde = datetime.strptime("2024-09-03", "%Y-%m-%d").isoformat()
fecha_hasta = datetime.strptime("2024-11-11", "%Y-%m-%d").isoformat()

async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
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
    finally:
        await client_api.Proveedores.close()
       
if __name__ == "__main__":
    asyncio.run(main())
