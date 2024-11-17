from ClientSimpleFactura import ClientSimpleFactura
import base64
import requests
from models.ResponseDTE import Response
from models.GetFactura.Credenciales import Credenciales
username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = ClientSimpleFactura(username, password)
solicitud= Credenciales(rut_emisor="76269769-6")
try:
    ListSucursal = client_api.Sucursales.ListarSucursales(solicitud)
    print("\nDatos de la Respuesta:")
    print(f"Status: {ListSucursal.status}")
    print(f"Message: {ListSucursal.message}")
    for cliente in ListSucursal.data:
        print(f"Nombre: {cliente.nombre}")
        print(f"Direccion: {cliente.direccion}")
        print("\n")
   
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")



