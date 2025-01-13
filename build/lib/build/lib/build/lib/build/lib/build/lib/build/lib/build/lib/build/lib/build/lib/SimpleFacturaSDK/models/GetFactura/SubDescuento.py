from dataclasses import dataclass, field
from enumeracion.TipoDescuento import ExpresionDineroEnum   

@dataclass
class SubDescuento:
    TipoDscto: ExpresionDineroEnum.NotSet
    ValorDscto: float 
