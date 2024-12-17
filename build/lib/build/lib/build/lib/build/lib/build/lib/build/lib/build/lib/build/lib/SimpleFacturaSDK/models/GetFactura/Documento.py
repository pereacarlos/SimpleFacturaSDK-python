from dataclasses import dataclass, field, asdict
from typing import List, Optional
from datetime import datetime
from models.GetFactura.Encabezado import Encabezado
from models.GetFactura.Detalle import Detalle
from models.GetFactura.SubTotal import SubTotal
from models.GetFactura.DescuentosRecargos import DescuentosRecargos
from models.GetFactura.Referencia import Referencia
from models.GetFactura.ComisionRecargo import ComisionRecargo
@dataclass
class Documento:
    Encabezado: Encabezado
    Detalle: List[Detalle]
    Referencia: Optional[List[Referencia]] = None
