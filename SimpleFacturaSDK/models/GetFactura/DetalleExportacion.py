from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CdgItem
from SimpleFacturaSDK.enumeracion.IndicadorFacturacionExencion import IndicadorFacturacionExencionEnum
from SimpleFacturaSDK.models.GetFactura.Retenedor import Retenedor
from SimpleFacturaSDK.models.GetFactura.SubCantidad import SubCantidad
from SimpleFacturaSDK.models.GetFactura.OtraMonedaDetalle import OtraMonedaDetalle
from SimpleFacturaSDK.models.GetFactura.SubDescuento import SubDescuento
from SimpleFacturaSDK.models.GetFactura.SubRecargo import SubRecargo
from SimpleFacturaSDK.enumeracion.TipoImpuesto import TipoImpuestoEnum

@dataclass
class DetalleExportacion:
    NroLinDet: int 
    IndExe: IndicadorFacturacionExencionEnum
    NmbItem: str
    DscItem: str 
    QtyRef: float 
    UnmdRef: str 
    PrcRef: float 
    QtyItem: float 
    FechaElaboracionString: str
    FchElabor = datetime
    FechaVencimientoString: str 
    FchVenc = datetime
    UnmdItem: str 
    PrcItem: float
    DescuentoPct: float 
    DescuentoMonto: int 
    RecargoPct: float 
    RecargoMonto: int 
    MontoItem: float 
    Retenedor: Optional[Retenedor] = None
    CdgItem: Optional[List[CdgItem]] = None
    Subcantidad: Optional[List[SubCantidad]] = None
    OtrMnda: Optional[OtraMonedaDetalle] = None
    SubDscto: Optional[List[SubDescuento]] = None
    SubRecargo: Optional[List[SubRecargo]] = None
    CodigoImpuestoAdicional: Optional[List[TipoImpuestoEnum]] = None




