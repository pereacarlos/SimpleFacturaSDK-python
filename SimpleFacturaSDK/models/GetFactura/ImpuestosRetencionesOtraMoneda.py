from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoImpuesto import TipoImpuestoEnum

@dataclass
class ImpuestosRetencionesOtraMoneda:
    TipoImpOtrMnda: TipoImpuestoEnum = TipoImpuestoEnum.NotSet
    TasaImpOtrMnda: float = 0.0
    VlrImpOtrMnda: float = 0.0

    __tasaImpuesto: float = field(default=0.0, init=False, metadata={"decimals": 2})
    __montoImpuesto: float = field(default=0.0, init=False, metadata={"decimals": 4})

    def __post_init__(self):
        self.__tasaImpuesto = round(self.TasaImpOtrMnda, 2)
        self.__montoImpuesto = round(self.VlrImpOtrMnda, 4)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TipoImpOtrMnda=TipoImpuestoEnum(data.get('TipoImpOtrMnda')),
            TasaImpOtrMnda=data.get('TasaImpOtrMnda'),
            VlrImpOtrMnda=data.get('VlrImpOtrMnda')
        )