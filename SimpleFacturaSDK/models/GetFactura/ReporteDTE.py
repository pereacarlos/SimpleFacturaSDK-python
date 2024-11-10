from dataclasses import dataclass, asdict
from SimpleFacturaSDK.models.GetFactura.DetalleDte import DetalleDte 
from typing import Optional, List
from datetime import datetime

@dataclass
class ReporteDTE:
    Fecha: datetime
    TipoDTE: str
    Emitidos: int
    Anulados: int
    TotalNeto: float
    TotalExento: float
    TotalIva: float
    Total: float
    Detalles: List[DetalleDte]

    @classmethod
    def from_dict(cls, data: dict):
        detalles_data = data.get('Detalles', [])
        detalles = [DetalleDte.from_dict(detalle) for detalle in detalles_data]
        
        return cls(
            Fecha=data.get('Fecha'),
            TipoDTE=data.get('TipoDTE'),
            Emitidos=data.get('Emitidos'),
            Anulados=data.get('Anulados'),
            TotalNeto=data.get('TotalNeto'),
            TotalExento=data.get('TotalExento'),
            TotalIva=data.get('TotalIva'),
            Total=data.get('Total'),
            Detalles=detalles
        )

    def to_dict(self):
        return asdict(self)
