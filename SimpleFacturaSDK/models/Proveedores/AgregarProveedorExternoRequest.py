from dataclasses import dataclass
from typing import List, Optional

from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.Proveedores.ProveedorExternoEnt import NuevoProveedorExternoEnt

@dataclass
class AgregarProveedorExternoRequest:
    Credenciales: Credenciales
    Proveedores: Optional[List[NuevoProveedorExternoEnt]] = None

    def to_dict(self):
        return {
            "credenciales": self.Credenciales.to_dict(),
            "proveedores": [proveedor.to_dict() for proveedor in self.Proveedores] if self.Proveedores else [],
        }
