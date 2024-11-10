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
    Id: Optional[str]
    Encabezado: Encabezado
    Detalle: List[DetalleExportacion]
    SubTotInfo: Optional[List[SubTotal]] 
    DscRcgGlobal: Optional[List[DescuentosRecargos]] 
    Referencia: Optional[List[Referencia]]
    Comisiones: Optional[List[ComisionRecargo]]


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Id=data.get('Id'),
            Encabezado=Encabezado,
            Detalle=[DetalleExportacion],
            SubTotInfo=[SubTotal],
            DscRcgGlobal=[DescuentosRecargos],
            Referencia=[Referencia],
            Comisiones=[ComisionRecargo]
        )
