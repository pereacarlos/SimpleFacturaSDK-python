# Base.py
from SimpleFacturaSDK.services.FacturaService import FacturacionService
from SimpleFacturaSDK.services.ProductoService import ProductoService
from SimpleFacturaSDK.services.ProveedorService import ProveedorService
from SimpleFacturaSDK.services.ClientesService import ClientesService
from SimpleFacturaSDK.services.SucursalService import SucursalService
from SimpleFacturaSDK.services.FolioService import FolioService
import requests
import base64

BASE_URL = "https://api.simplefactura.cl"

class APIClient:
    def __init__(self, username, password):
        # Configure the HTTP client
        self.session = requests.Session()
        self.base_url = BASE_URL
        
        # Configure basic authentication
        auth_token = f"{username}:{password}".encode("ascii")
        base64_auth_token = base64.b64encode(auth_token).decode("ascii")
        
        # Set headers for the session
        self.session.headers.update({
            'Authorization': f'Basic {base64_auth_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
        
        # Initialize services
        self.Facturacion = FacturacionService(self.session, self.base_url)
        self.Productos = ProductoService(self.session, self.base_url)
        self.Proveedores = ProveedorService(self.session, self.base_url)
        self.Clientes = ClientesService(self.session, self.base_url)
        self.Sucursales = SucursalService(self.session, self.base_url)
        self.Folios = FolioService(self.session, self.base_url)