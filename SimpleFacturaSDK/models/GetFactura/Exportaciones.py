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


    def __init__(self):
        self.Id = None
        self.Encabezado = Encabezado()
        self.Detalle = []
        self.SubTotInfo = []
        self.DscRcgGlobal = []
        self.Referencia = []
        self.Comisiones = []
