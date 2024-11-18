from dataclasses import dataclass, field
from typing import Optional
from enumeracion.TipoRecargoComision import TipoRecargoComisionEnum

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class ComisionRecargo:
    TipoMovim: TipoRecargoComisionEnum
    NroLinCom: int 
    Glosa: str
    TasaComision: float
    ValComNeto: int
    ValComExe: int
    ValComIVA: int
