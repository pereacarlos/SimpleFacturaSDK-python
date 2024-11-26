from dataclasses import dataclass, asdict
from typing import List, Optional
from enumeracion.CodigosAduana import Moneda
@dataclass
class Totales:
    TpoMoneda: Optional[Moneda] = None
    MntNeto: Optional[float] = None
    TasaIVA: Optional[str] = None
    IVA: Optional[int] = None
    MntTotal: Optional[float] = None
    MntExe: Optional[float] = None