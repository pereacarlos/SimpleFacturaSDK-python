from dataclasses import dataclass, asdict
from typing import List, Optional
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CdgItem

@dataclass
class Detalle:
    NroLinDet: str
    NmbItem: str
    CdgItem: List[CdgItem]
    QtyItem: str
    UnmdItem: str
    PrcItem: str
    MontoItem: str