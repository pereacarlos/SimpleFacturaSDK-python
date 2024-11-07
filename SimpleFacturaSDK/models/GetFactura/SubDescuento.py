from dataclasses import dataclass
from SimpleFacturaSDK.enumeracion.TipoDescuento import ExpresionDineroEnum   

@dataclass
class SubDescuento:
    TipoDscto: ExpresionDineroEnum = ExpresionDineroEnum.NotSet
    __valorDescuento: float = 0.0
    @property
    def ValorDscto(self) -> float:
        return round(self.__valorDescuento, 2)

    @ValorDscto.setter
    def ValorDscto(self, value: float):
        self.__valorDescuento = value

    def __init__(self):
        self.TipoDscto = ExpresionDineroEnum.NotSet
        self.ValorDscto = 0.0