
from dataclasses import dataclass, asdict
from typing import List, Optional
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CdgItem
from SimpleFacturaSDK.enumeracion.IndicadorFacturacionExencion import IndicadorFacturacionExencionEnum
from SimpleFacturaSDK.models.GetFactura.Retenedor import Retenedor
from SimpleFacturaSDK.models.GetFactura.Subcantidad import SubCantidad
from SimpleFacturaSDK.models.GetFactura.SubDescuento import SubDescuento
from SimpleFacturaSDK.models.GetFactura.SubRecargo import SubRecargo
from SimpleFacturaSDK.models.GetFactura.OtraMonedaDetalle import OtraMonedaDetalle
from datetime import datetime
@dataclass
class Detalle:
    NroLinDet: int
    NmbItem: str
    CdgItem: List[CdgItem]
    QtyItem: float
    UnmdItem: str
    PrcItem: float
    MontoItem: int
    QtyRef: float = None
    UnmdRef: str = None
    PrcRef: float = None
    DescuentoPct: float = None
    DescuentoMonto: int = None
    RecargoPct: float = None
    RecargoMonto: int = None
    SubRecargo: Optional[SubRecargo] = None
    SubDscto: Optional[SubDescuento] = None
    FchElabor: Optional[datetime] = None
    FchVencim: Optional[datetime] = None
    IndExe: Optional[IndicadorFacturacionExencionEnum] = None
    DscItem: Optional[str] = None
    Retenedor: Optional[Retenedor] = None
    Subcantidad: Optional[SubCantidad] = None
    OtrMnda: Optional[OtraMonedaDetalle] = None
