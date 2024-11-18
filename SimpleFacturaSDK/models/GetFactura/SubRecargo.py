from dataclasses import dataclass, field
from enumeracion.TipoDescuento import ExpresionDineroEnum
@dataclass
class SubRecargo:
    TipoRecargo: ExpresionDineroEnum
    ValorRecargo: float 
