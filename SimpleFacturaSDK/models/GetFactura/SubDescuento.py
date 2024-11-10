from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoDescuento import ExpresionDineroEnum   

@dataclass
class SubDescuento:
    TipoDscto: ExpresionDineroEnum.NotSet
    ValorDscto: float 
    __valorDescuento: float

    def __post_init__(self):
        self.__valorDescuento = round(self.ValorDscto, 2)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TipoDscto=ExpresionDineroEnum(data.get('TipoDscto')),
            ValorDscto=data.get('ValorDscto')
        )
  
