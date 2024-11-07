from dataclasses import dataclass
from SimpleFacturaSDK.enum.TipoDescuento import ExpresionDineroEnum
@dataclass
class SubRecargo:
    TipoRecargo: ExpresionDineroEnum = ExpresionDineroEnum.NotSet
    __valorRecargo: float = 0.0
    @property
    def ValorRecargo(self) -> float:
        return round(self.__valorRecargo, 2)

    @ValorRecargo.setter
    def ValorRecargo(self, value: float):
        self.__valorRecargo = value

    def __init__(self):
        self.TipoRecargo = ExpresionDineroEnum.NotSet
        self.ValorRecargo = 0.0