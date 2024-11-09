from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoDescuento import ExpresionDineroEnum
@dataclass
class SubRecargo:
    TipoRecargo: ExpresionDineroEnum = ExpresionDineroEnum.NotSet
    ValorRecargo: float = 0.0
    __valorRecargo: float = field(default=0.0, metadata={"decimals": 2})

    def __post_init__(self):
        self.__valorRecargo = round(self.ValorRecargo, 2)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TipoRecargo=ExpresionDineroEnum(data.get('TipoRecargo')),
            ValorRecargo=data.get('ValorRecargo')
        )