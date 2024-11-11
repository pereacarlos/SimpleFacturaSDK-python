from dataclasses import dataclass, asdict
from typing import List, Optional
@dataclass
class Totales:
    MntNeto: str
    TasaIVA: str
    IVA: str
    MntTotal: str