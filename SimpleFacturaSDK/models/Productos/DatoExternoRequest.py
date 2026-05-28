from dataclasses import dataclass, field
from typing import List, Optional
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest
from SimpleFacturaSDK.models.GetFactura import Credenciales
from SimpleFacturaSDK.models.Clientes.NuevoReceptorExternoRequest import NuevoReceptorExternoRequest
from SimpleFacturaSDK.models.Clientes.EditarDatosClienteExternoEnt import EditarDatosClienteExternoEnt

@dataclass
class DatoExternoRequest:
    Credenciales: Credenciales
    Productos: Optional[List[NuevoProductoExternoRequest]] = None
    Clientes: Optional[List[NuevoReceptorExternoRequest]] = None
    UpdateClientes: Optional[List[EditarDatosClienteExternoEnt]] = None

    def to_dict(self):
        return {
            "credenciales": self.Credenciales.to_dict(),
            "Productos": [p.to_dict() for p in self.Productos] if self.Productos else [],
            "Clientes": [c.to_dict() for c in self.Clientes] if self.Clientes else [],
            "UpdateClientes": [uc.to_dict() for uc in self.UpdateClientes] if self.UpdateClientes else []
        }