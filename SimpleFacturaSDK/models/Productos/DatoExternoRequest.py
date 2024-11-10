from dataclasses import dataclass, field
from typing import List, Optional
from SimpleFacturaSDK.models.Clientes.NuevoReceptorExternoRequest import NuevoReceptorExternoRequest
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SDKSimpleFactura.Models.Productos import NuevoProductoExternoRequest

@dataclass
class DatoExternoRequest:
    Credenciales: Credenciales
    Productos: Optional[List[NuevoProductoExternoRequest]]
    Clientes: Optional[List[NuevoReceptorExternoRequest]] 

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Credenciales=Credenciales,
            Productos=[NuevoProductoExternoRequest],
            Clientes=[NuevoReceptorExternoRequest]
        )

    def to_dict(self):
        return {
            'Credenciales': self.Credenciales.to_dict(),
            'Productos': [p.to_dict() for p in self.Productos],
            'Clientes': [c.to_dict() for c in self.Clientes]
        }