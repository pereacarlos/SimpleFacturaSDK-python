from dataclasses import dataclass, field
from SimpleFacturaSDK.enum.TipoImpuesto import TipoImpuestoEnum

@dataclass
class ImpuestosRetencionesOtraMoneda:
    TipoImpOtrMnda: TipoImpuestoEnum = TipoImpuestoEnum.NotSet
    __tasaImpuesto: float = field(default=0.0, init=False)
    __montoImpuesto: float = field(default=0.0, init=False)

    @property
    def TasaImpOtrMnda(self) -> float:
        return round(self.__tasaImpuesto, 2)

    @TasaImpOtrMnda.setter
    def TasaImpOtrMnda(self, value: float):
        self.__tasaImpuesto = value

    @property
    def VlrImpOtrMnda(self) -> float:
        return round(self.__montoImpuesto, 4)

    @VlrImpOtrMnda.setter
    def VlrImpOtrMnda(self, value: float):
        self.__montoImpuesto = value


    def __init__(self):
        self.TipoImpOtrMnda = TipoImpuestoEnum.NotSet
        self.TasaImpOtrMnda = 0.0
        self.VlrImpOtrMnda = 0.0