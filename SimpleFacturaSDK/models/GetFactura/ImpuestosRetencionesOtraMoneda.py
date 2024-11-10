from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoImpuesto import TipoImpuestoEnum

@dataclass
class ImpuestosRetencionesOtraMoneda:
    TipoImpOtrMnda: TipoImpuestoEnum = TipoImpuestoEnum.NotSet
    TasaImpOtrMnda: float 
    VlrImpOtrMnda: float

    __tasaImpuesto: float 
    __montoImpuesto: float

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