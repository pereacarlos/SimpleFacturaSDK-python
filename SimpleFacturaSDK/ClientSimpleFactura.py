
from services.FacturaService import FacturacionService
from services.ProductoService import ProductoService
from services.ProveedorService import ProveedorService
from services.ClientesService import ClientesService
from services.SucursalService import SucursalService
from services.FolioService import FolioService
from services.ConfiguracionService import ConfiguracionService
from services.BoletaHonorarioService import BoletaHonorarioService
import requests
import base64
from dotenv import load_dotenv
import os
load_dotenv()

#BASE_URL = "https://api.simplefactura.cl"
BASE_URL = os.getenv("SF_BASE_URL")
class ClientSimpleFactura:
    def __init__(self, username, password):
        self.session = requests.Session()
        self.base_url = BASE_URL
        auth_token = f"{username}:{password}".encode("ascii")
        base64_auth_token = base64.b64encode(auth_token).decode("ascii")
        self.headers = {
            'Authorization': f'Basic {base64_auth_token}',
            'Accept': 'application/json',
            #'Content-Type': 'application/json'
        }
        self.session.headers.update(self.headers)
        services = [
            ("Facturacion", FacturacionService),
            ("Productos", ProductoService),
            ("Proveedores", ProveedorService),
            ("Clientes", ClientesService),
            ("Sucursales", SucursalService),
            ("Folios", FolioService),
            ("ConfiguracionService", ConfiguracionService),
            ("BoletaHonorarioService", BoletaHonorarioService)
        ]
        for service_name, service_class in services:
            setattr(self, service_name, service_class(self.base_url, self.headers))
