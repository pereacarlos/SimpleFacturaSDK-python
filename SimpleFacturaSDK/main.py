from SimpleFacturaSDK.Base import APIClient
import requests
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.EnvioMailRequest import EnvioMailRequest, DteClass, MailClass
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime
fecha_desde = datetime.strptime("2023-10-25", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2023-10-30", "%Y-%m-%d")
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)

solicitud = ListaDteRequestEnt(
    Credenciales=Credenciales(
        rut_emisor="76269769-6"
    ),
    ambiente=AmbienteEnum.Certificacion,
    desde=fecha_desde,
    hasta=fecha_hasta
)

try:
    
    Consolidado = client_api.Facturacion.consolidadoVentas(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {Consolidado.status}")
    print(f"Message: {Consolidado.message}")
    for item in Consolidado.data:
        print(f"fecha: {item.fecha}")
        print(f"tipoDTE: {item.tiposDTE}")
        print(f"Emitidos: {item.emitidos}")
        print(f"anulados: {item.anulados}")
        print(f"total: {item.total}")
        print(f"totalNeto: {item.totalNeto}")
        print(f"totalIva: {item.totalIva}")
        print(item)
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")

