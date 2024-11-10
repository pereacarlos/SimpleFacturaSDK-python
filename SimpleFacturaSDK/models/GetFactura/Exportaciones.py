from dataclasses import dataclass, field
from typing import List, Optional
from .Encabezado import Encabezado
from .SubTotal import SubTotal
from .DescuentosRecargos import DescuentosRecargos
from .Referencia import Referencia
from .ComisionRecargo import ComisionRecargo
from .DetalleExportacion import DetalleExportacion
@dataclass
class Exportaciones:
    Id: Optional[str] = None
    Encabezado: Encabezado = field(default_factory=Encabezado)
    Detalle: List[DetalleExportacion] = field(default_factory=list)
    SubTotInfo: Optional[List[SubTotal]] = None
    DscRcgGlobal: Optional[List[DescuentosRecargos]] = None
    Referencia: Optional[List[Referencia]] = None
    Comisiones: Optional[List[ComisionRecargo]] = None


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Id=data.get('id'),
            Encabezado=Encabezado.from_dict(data.get('Encabezado')) if data.get('Encabezado') else Encabezado(),
            Detalle=[DetalleExportacion.from_dict(d) for d in data.get('Detalle', [])] if data.get('Detalle') else [],
            SubTotInfo=[SubTotal.from_dict(s) for s in data.get('SubTotInfo', [])] if data.get('SubTotInfo') else [],
            DscRcgGlobal=[DescuentosRecargos.from_dict(d) for d in data.get('DscRcgGlobal', [])] if data.get('DscRcgGlobal') else [],
            Referencia=[Referencia.from_dict(r) for r in data.get('Referencia', [])] if data.get('Referencia') else [],
            Comisiones=[ComisionRecargo.from_dict(c) for c in data.get('Comisiones', [])] if data.get('Comisiones') else []
        )
