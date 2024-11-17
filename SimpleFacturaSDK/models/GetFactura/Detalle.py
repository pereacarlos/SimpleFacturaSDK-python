from dataclasses import dataclass, asdict
from typing import List, Optional
from models.GetFactura.CodigoItem import CdgItem
from enumeracion.IndicadorFacturacionExencion import IndicadorFacturacionExencionEnum

@dataclass
class Detalle:
    NroLinDet: int
    NmbItem: str
    CdgItem: List[CdgItem]
    QtyItem: float
    UnmdItem: str
    PrcItem: float
    MontoItem: int
    IndExe: Optional[IndicadorFacturacionExencionEnum] = None
    DscItem: Optional[str] = None
