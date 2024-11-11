from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoDescuento import ExpresionDineroEnum   

@dataclass
class SubDescuento:
    TipoDscto: ExpresionDineroEnum.NotSet
    ValorDscto: float 
