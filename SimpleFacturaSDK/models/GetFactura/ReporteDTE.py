from dataclasses import dataclass, asdict
from SimpleFacturaSDK.models.GetFactura.DetalleDte import DetalleDte 
from typing import Optional, List
from datetime import datetime

@dataclass
class ReporteDTE:
    fecha: datetime
    tiposDTE: str
    emitidos: int
    anulados: int
    totalNeto: float
    totalExento: float
    totalIva: float
    total: float
    detalle: List[DetalleDte]


    @classmethod
    def from_dict(cls, data: dict):
        detalles_data = data.get('Detalles', [])
        detalles = [DetalleDte.from_dict(detalle) for detalle in detalles_data]
        
        return cls(
            fecha=data.get('fecha'),
            tiposDTE=data.get('tiposDTE'),
            emitidos=data.get('emitidos'),
            anulados=data.get('anulados'),
            totalNeto=data.get('totalNeto'),
            totalExento=data.get('totalExento'),
            totalIva=data.get('totalIva'),
            total=data.get('total'),
            detalle=detalles
        )

    def to_dict(self):
        return asdict(self)
