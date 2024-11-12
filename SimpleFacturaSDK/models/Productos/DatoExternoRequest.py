from dataclasses import dataclass, field
from typing import List, Optional
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from SimpleFacturaSDK.models.GetFactura import Credenciales
from SimpleFacturaSDK.models.Clientes.NuevoReceptorExternoRequest import NuevoReceptorExternoRequest

@dataclass
class DatoExternoRequest:
    Credenciales: Credenciales
    Productos: Optional[List[NuevoProductoExternoRequest]] = None
    Clientes: Optional[List[NuevoReceptorExternoRequest]] = None

    def to_dict(self):
        return {
            "credenciales": self.Credenciales.to_dict(),
            'Productos': [p.to_dict() for p in self.Productos],
            'Clientes': [c.to_dict() for c in self.Clientes]
        }