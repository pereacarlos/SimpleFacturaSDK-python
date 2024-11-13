from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoDescuento import ExpresionDineroEnum
@dataclass
class SubRecargo:
    TipoRecargo: ExpresionDineroEnum
    ValorRecargo: float 
