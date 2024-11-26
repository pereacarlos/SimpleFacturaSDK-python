import aiohttp
from services.FacturaService import FacturacionService
from services.ProductoService import ProductoService
from services.ProveedorService import ProveedorService
from services.ClientesService import ClientesService
from services.SucursalService import SucursalService
from services.FolioService import FolioService
from services.ConfiguracionService import ConfiguracionService
from services.BoletaHonorarioService import BoletaHonorarioService
import base64
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("SF_BASE_URL")

class ClientSimpleFactura:
    def __init__(self, username, password):
        self.base_url = BASE_URL
        auth_token = f"{username}:{password}".encode("ascii")
        base64_auth_token = base64.b64encode(auth_token).decode("ascii")
        self.headers = {
            'Authorization': f'Basic {base64_auth_token}',
            'Accept': 'application/json',
        }
        self.services = [
            ("Facturacion", FacturacionService),
            ("Productos", ProductoService),
            ("Proveedores", ProveedorService),
            ("Clientes", ClientesService),
            ("Sucursales", SucursalService),
            ("Folios", FolioService),
            ("ConfiguracionService", ConfiguracionService),
            ("BoletaHonorarioService", BoletaHonorarioService),
        ]

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=self.headers)
        for service_name, service_class in self.services:
            setattr(self, service_name, service_class(self.base_url, self.headers, self.session))
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        for service_name, service_class in self.services:
            service_instance = getattr(self, service_name, None)
            if service_instance and hasattr(service_instance, 'close'):
                await service_instance.close()
        await self.session.close()

