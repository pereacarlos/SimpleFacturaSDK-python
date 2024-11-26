
from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.enumeracion.TipoMovimiento import TipoMovimientoEnum
from SimpleFacturaSDK.enumeracion.TipoDescuento import ExpresionDineroEnum
from SimpleFacturaSDK.enumeracion.IndicadorExento import IndicadorExentoEnum
def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''
@dataclass
class DescuentosRecargos:
    NroLinDR: int
    TpoMov: TipoMovimientoEnum
    GlosaDR: str 
    TpoValor: ExpresionDineroEnum
    ValorDR: float 
    ValorDROtrMnda: float 
    IndExeDR: IndicadorExentoEnum 
