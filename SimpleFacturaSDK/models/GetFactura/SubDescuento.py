from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoDescuento import ExpresionDineroEnum   

@dataclass
class SubDescuento:
    TipoDscto: ExpresionDineroEnum = ExpresionDineroEnum.NotSet
    ValorDscto: float = 0.0
    __valorDescuento: float = field(default=0.0, metadata={"decimals": 2})

    def __post_init__(self):
        self.__valorDescuento = round(self.ValorDscto, 2)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TipoDscto=ExpresionDineroEnum(data.get('TipoDscto')),
            ValorDscto=data.get('ValorDscto')
        )
  
