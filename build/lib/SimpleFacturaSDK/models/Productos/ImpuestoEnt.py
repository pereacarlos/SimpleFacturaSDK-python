from dataclasses import dataclass, field, asdict
from typing import Optional
import json

@dataclass
class ImpuestoEnt:
    nombre: str
    valor: float
    tasa: float
    codigo: int
    activo: Optional[bool] = None
    impuestoId: Optional[int] = None
    isRetencion: Optional[bool] = None
    tipoImpuesto: Optional[int] = None

    def to_dict(self):
        return asdict(self)
