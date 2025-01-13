# client_simple_factura.py
import aiohttp
import os
from datetime import datetime, timezone
from config import BASE_URL

from SimpleFacturaSDK.services.FacturaService import FacturacionService
from SimpleFacturaSDK.services.ProductoService import ProductoService
from SimpleFacturaSDK.services.ProveedorService import ProveedorService
from SimpleFacturaSDK.services.ClientesService import ClientesService
from SimpleFacturaSDK.services.SucursalService import SucursalService
from SimpleFacturaSDK.services.FolioService import FolioService
from SimpleFacturaSDK.services.ConfiguracionService import ConfiguracionService
from SimpleFacturaSDK.services.BoletaHonorarioService import BoletaHonorarioService
from SimpleFacturaSDK.services.UsuarioService import UsuarioService

from SimpleFacturaSDK.Utilidades.auth_utils import (
    obtener_y_configurar_token,
    ensure_token_valid,
    token_ha_expirado,
)

class ClientSimpleFactura:
    def __init__(self, username=None, password=None):
        self.base_url = BASE_URL
        self.username = username or os.getenv("SF_USERNAME")
        self.password = password or os.getenv("SF_PASSWORD")
        self.headers = {
            'Accept': 'application/json',
        }
        self.token = None
        self.expires_at = None
        # No tenemos last_username y last_password al inicio; se setearán al obtener el token
        self.services = [
            ("Facturacion", FacturacionService),
            ("Productos", ProductoService),
            ("Proveedores", ProveedorService),
            ("Clientes", ClientesService),
            ("Sucursales", SucursalService),
            ("Folios", FolioService),
            ("ConfiguracionService", ConfiguracionService),
            ("BoletaHonorarioService", BoletaHonorarioService),
            ("Usuarios", UsuarioService),
        ]

    async def __aenter__(self):
        # Obtener token al iniciar
        await obtener_y_configurar_token(self)
        
        self.session = aiohttp.ClientSession(headers=self.headers)
        # Inicializamos los servicios con la sesión ya autenticada
        for service_name, service_class in self.services:
            service_instance = service_class(self.base_url, self.headers, self.session, self)
            setattr(self, service_name, service_instance)
        
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        for service_name, service_class in self.services:
            service_instance = getattr(self, service_name, None)
            if service_instance and hasattr(service_instance, 'close'):
                await service_instance.close()
        await self.session.close()

    async def ensure_token_valid(self):
        await ensure_token_valid(self)

    def token_ha_expirado(self):
        return token_ha_expirado(self)
