
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura as APIClient
import base64
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales

username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)
solicitud= Credenciales(
    rut_emisor="76269769-6"
)
try:
    DatosEmpresa = client_api.ConfiguracionService.datos_empresa(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {DatosEmpresa.status}")
    print(f"Message: {DatosEmpresa.message}")
    print(f"Data: {DatosEmpresa.data}")
    print(f"rut: {DatosEmpresa.data.rut}")
    print(f"razonSocial: {DatosEmpresa.data.razonSocial}")
    print(f"giro: {DatosEmpresa.data.giro}")
   
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")
