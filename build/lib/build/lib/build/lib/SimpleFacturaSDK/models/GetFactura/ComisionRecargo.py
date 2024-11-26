
from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.enumeracion.TipoRecargoComision import TipoRecargoComisionEnum

@dataclass
class ComisionRecargo:
    TipoMovim: TipoRecargoComisionEnum
    NroLinCom: int 
    Glosa: str
    TasaComision: float
    ValComNeto: int
    ValComExe: int
    ValComIVA: int
