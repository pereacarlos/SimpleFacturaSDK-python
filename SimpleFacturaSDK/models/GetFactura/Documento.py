from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from Encabezado import Encabezado
from Detalle import Detalle
from SubTotal import SubTotal
from DescuentosRecargos import DescuentosRecargos
from Referencia import Referencia
from ComisionRecargo import ComisionRecargo

@dataclass
class Documento:
 
    Id: Optional[str] = None
    Encabezado: Optional[Encabezado] = field(default_factory=Encabezado)

    Detalle: List[Detalle] = field(default_factory=list)

    SubTotInfo: List[SubTotal] = field(default_factory=list)

    DscRcgGlobal: Optional[List[DescuentosRecargos]] = field(default_factory=list)

    Referencia: Optional[List[Referencia]] = field(default_factory=list)

   
    Comisiones: Optional[List[ComisionRecargo]] = field(default_factory=list)

    def __init__(self):
        self.Id = None
        self.Encabezado = Encabezado()
        self.Detalle = []
        self.SubTotInfo = []
        self.DscRcgGlobal = []
        self.Referencia = []
        self.Comisiones = []