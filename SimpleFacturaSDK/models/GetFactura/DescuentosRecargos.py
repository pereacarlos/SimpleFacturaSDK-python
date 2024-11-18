from dataclasses import dataclass, field
from typing import Optional
from enumeracion.TipoMovimiento import TipoMovimientoEnum
from enumeracion.TipoDescuento import ExpresionDineroEnum
from enumeracion.IndicadorExento import IndicadorExentoEnum
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

