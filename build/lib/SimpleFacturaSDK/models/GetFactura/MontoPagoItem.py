from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class MontoPagoItem:
    MntPago: int
    GlosaPagos: str
    FchPago: str
   