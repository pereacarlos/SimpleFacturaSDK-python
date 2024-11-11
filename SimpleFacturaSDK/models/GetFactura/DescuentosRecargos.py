from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.enumeracion.TipoMovimiento import TipoMovimientoEnum
from SimpleFacturaSDK.enumeracion.ExpresionDinero import ExpresionDineroEnum
from SimpleFacturaSDK.enumeracion.IndicadorExento import IndicadorExentoEnum
def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class DescuentosRecargos:
    NroLinDR: int
    TpoMov: TipoMovimientoEnum
    GlosaDR: str 
    tpo_valor: ExpresionDineroEnum
    ValorDR: float 
    ValorDROtrMnda: float 
    ind_exe_dr: IndicadorExentoEnum 

