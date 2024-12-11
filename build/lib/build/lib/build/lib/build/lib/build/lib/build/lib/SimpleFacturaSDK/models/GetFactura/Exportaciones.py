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
    Encabezado: Encabezado
    Detalle: List[DetalleExportacion]
    Id: Optional[str] = None
    SubTotInfo: Optional[List[SubTotal]] = None
    DscRcgGlobal: Optional[List[DescuentosRecargos]] = None
    Referencia: Optional[List[Referencia]] = None
    Comisiones: Optional[List[ComisionRecargo]] = None

