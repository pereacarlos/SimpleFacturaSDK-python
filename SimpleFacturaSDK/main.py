from SimpleFacturaSDK.Base import APIClient
import requests
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime
fecha_desde = datetime.strptime("2024-08-01", "%Y-%m-%d")
fecha_hasta = datetime.strptime("2024-08-17", "%Y-%m-%d")
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)


solicitud = ListaDteRequestEnt(
    Credenciales=Credenciales(
        rut_emisor="76269769-6",
        rut_contribuyente="10422710-4",
        nombre_sucursal="Casa Matriz"
    ),
    ambiente=AmbienteEnum.Certificacion,
    folio=0,
    codigoTipoDte=DTEType.NotSet,
    desde=fecha_desde,
    hasta=fecha_hasta
)

try:
    Listado = client_api.Facturacion.listadoDteEmitidos(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {Listado.status}")
    print(f"Message: {Listado.message}")

    for dte in Listado.data:
        print(f"ambiente: {dte.ambiente}")
        print(f"tipoDTE: {dte.tipoDte}")
        print(f"folioReutilizado: {dte.folioReutilizado}")
        print(f"fechaCreacion: {dte.fechaCreacion}")
        print(f"Folio: {dte.folio}")
        print(f"razonSocialReceptor: {dte.razonSocialReceptor}")
        print(f"Total: {dte.total}")
        print(dte)
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")
