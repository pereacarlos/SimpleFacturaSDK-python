
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura as APIClient
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
solicitud= SolicitudFolios(
    RutEmpresa = "76269769-6",
    TipoDTE = 33,
    Ambiente = 0
)
try:
    FolioSinUsar = client_api.Folios.Folios_Sin_Uso(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {FolioSinUsar.status}")
    print(f"Message: {FolioSinUsar.message}")
    print(f"Data: {FolioSinUsar.data}")
    for data in FolioSinUsar.data:
        print(f"desde: {data.desde}")
        print(f"hasta: {data.hasta}")
        print(f"Cantidad: {data.cantidad}")
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")
