# Base.py
try:
    from services.FacturaService import FacturacionService
    from services.ProductoService import ProductoService
    from services.ProveedorService import ProveedorService
    from services.ClientesService import ClientesService
    from services.SucursalService import SucursalService
    from services.FolioService import FolioService
    from services.ConfiguracionService import ConfiguracionService
    from services.BoletaHonorarioService import BoletaHonorarioService
except ImportError:
    from SimpleFacturaSDK.services.FacturaService import FacturacionService
    from SimpleFacturaSDK.services.ProductoService import ProductoService
    from SimpleFacturaSDK.services.ProveedorService import ProveedorService
    from SimpleFacturaSDK.services.ClientesService import ClientesService
    from SimpleFacturaSDK.services.SucursalService import SucursalService
    from SimpleFacturaSDK.services.FolioService import FolioService
    from SimpleFacturaSDK.services.ConfiguracionService import ConfiguracionService
    from SimpleFacturaSDK.services.BoletaHonorarioService import BoletaHonorarioService



import requests
import base64

#BASE_URL = "https://api.simplefactura.cl"

BASE_URL = "https://backend-qa.simplefactura.cl"

class ClientSimpleFactura:
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
        self.ConfiguracionService = ConfiguracionService(self.session, self.base_url)
        self.BoletaHonorarioService = BoletaHonorarioService(self.session, self.base_url)