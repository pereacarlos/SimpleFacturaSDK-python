from SimpleFacturaSDK.Base import APIClient
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.ListadoRequest import ListaDteRequestEnt
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.models.Folios.SolicitudFolios import SolicitudFolios
from SimpleFacturaSDK.models.Folios.TimbrajeEnt import TimbrajeEnt
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
import json
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)
solicitud= FolioRequest(
    credenciales=Credenciales(
        rut_emisor = "76269769-6",
        nombre_sucursal = "Casa Matriz"
    ),
    CodigoTipoDte= None,
    Ambiente=0
)
try:
    ConsultarFolios = client_api.Folios.ConsultarFolios(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {ConsultarFolios.status}")
    print(f"Message: {ConsultarFolios.message}")
    print(f"Data: {ConsultarFolios.data}")
    for folio in ConsultarFolios.data:
        print(f"folio: {folio.foliosDisponibles}")
        print(f"codigoSii: {folio.codigoSii}")
        print(f"fechaIngreso: {folio.fechaIngreso}")
        print(f"desde: {folio.desde}")
        print(f"hasta: {folio.hasta}")

except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")
