from dataclasses import dataclass, field, asdict
from typing import List, Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.Encabezado import Encabezado
from SimpleFacturaSDK.models.GetFactura.Detalle import Detalle
from SimpleFacturaSDK.models.GetFactura.SubTotal import SubTotal
from SimpleFacturaSDK.models.GetFactura.DescuentosRecargos import DescuentosRecargos
from SimpleFacturaSDK.models.GetFactura.Referencia import Referencia
from SimpleFacturaSDK.models.GetFactura.ComisionRecargo import ComisionRecargo
@dataclass
class Documento:
    Encabezado: Encabezado
    Detalle: List[Detalle]
    Referencia: Optional[List[Referencia]] = None
