from dataclasses import dataclass, field, asdict
from typing import Optional
import json

@dataclass
class ImpuestoEnt:
    ImpuestoId: Optional[int]
    Nombre: str
    Valor: float
    IsRetencion: bool
    Activo: bool
    TipoImpuesto: int
    Tasa: float
    Codigo: int

    def to_dict(self):
        result = asdict(self)
        return {k: v for k, v in result.items() if v is not None}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            ImpuestoId=data.get('ImpuestoId'),
            Nombre=data.get('Nombre'),
            Valor=data.get('Valor'),
            IsRetencion=data.get('IsRetencion'),
            Activo=data.get('Activo'),
            TipoImpuesto=data.get('TipoImpuesto'),
            Tasa=data.get('Tasa'),
            Codigo=data.get('Codigo')
        )

