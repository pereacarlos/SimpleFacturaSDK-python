from dataclasses import dataclass, asdict
from typing import List, Optional
from SimpleFacturaSDK.enumeracion.CodigosAduana import Moneda
@dataclass
class Totales:
    TpoMoneda: Moneda
    MntNeto: Optional[float] = None
    TasaIVA: Optional[str] = None
    IVA: Optional[int] = None
    MntTotal: Optional[float] = None
    MntExe: Optional[float] = None