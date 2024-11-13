from SimpleFacturaSDK.Base import APIClient
import requests
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)

solicitud =Credenciales(
    rut_emisor="76269769-6"
)
try:
    
    Conciliar = client_api.Facturacion.ConciliarEmitidos(solicitud,5,2024)
    print("\nDatos de la Respuesta:")
    print(f"Status: {Conciliar.status}")
    print(f"Message: {Conciliar.message}")
    print(f"Data: {Conciliar.data}")
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")

