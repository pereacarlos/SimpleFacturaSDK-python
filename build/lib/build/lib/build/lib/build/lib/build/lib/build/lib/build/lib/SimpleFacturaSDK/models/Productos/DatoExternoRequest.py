from dataclasses import dataclass, field
from typing import List, Optional
from models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from models.GetFactura import Credenciales
from models.Clientes.NuevoReceptorExternoRequest import NuevoReceptorExternoRequest

@dataclass
class DatoExternoRequest:
    Credenciales: Credenciales
    Productos: Optional[List[NuevoProductoExternoRequest]] = None
    Clientes: Optional[List[NuevoReceptorExternoRequest]] = None

    def to_dict(self):
        return {
            "credenciales": self.Credenciales.to_dict(),
            "Productos": [p.to_dict() for p in self.Productos] if self.Productos else [],
            "Clientes": [c.to_dict() for c in self.Clientes] if self.Clientes else []
        }