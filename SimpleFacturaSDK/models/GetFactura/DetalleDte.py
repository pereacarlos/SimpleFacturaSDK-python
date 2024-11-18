
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from enumeracion.TipoDTE import DTEType

@dataclass
class DetalleDte:
    Nombre: Optional[str] = None
    Descripcion: Optional[str] = None
    Exento: Optional[str] = None
    Precio: Optional[float] = None
    Cantidad: Optional[float] = None
    TotalImpuestos: Optional[float] = None
    Total: Optional[float] = None
    Fecha: Optional[datetime] = None
    CodigoSii: Optional[DTEType] = None
    TipoDTE: Optional[str] = None
    CantidadEmitidos: Optional[int] = None
    CantidadAnulados: Optional[int] = None
    TotalNeto: Optional[float] = None
    TotalExento: Optional[float] = None
    TotalIva: Optional[float] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Nombre=data.get('nombre'),
            Descripcion=data.get('descripcion'),
            Exento=data.get('exento'),
            Precio=data.get('precio'),
            Cantidad=data.get('cantidad'),
            TotalImpuestos=data.get('totalImpuestos'),
            Total=data.get('total'),
            Fecha=data.get('Fecha'),
            CodigoSii=data.get('CodigoSii'),
            TipoDTE=data.get('TipoDTE'),
            CantidadEmitidos=data.get('CantidadEmitidos'),
            CantidadAnulados=data.get('CantidadAnulados'),
            TotalNeto=data.get('TotalNeto'),
            TotalExento=data.get('TotalExento'),
            TotalIva=data.get('TotalIva')
        )
