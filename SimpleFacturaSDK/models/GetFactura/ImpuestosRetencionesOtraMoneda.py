from dataclasses import dataclass, field
from enum import Enum

class TipoImpuestoEnum(Enum):
    NotSet = 0
    # Agregar otros códigos de tipo de impuesto según sea necesario

@dataclass
class ImpuestosRetencionesOtraMoneda:
    TipoImpOtrMnda: TipoImpuestoEnum = TipoImpuestoEnum.NotSet
    _tasaImpuesto: float = field(default=0.0, init=False)
    _montoImpuesto: float = field(default=0.0, init=False)

    @property
    def TasaImpOtrMnda(self) -> float:
        return round(self._tasaImpuesto, 2)

    @TasaImpOtrMnda.setter
    def TasaImpOtrMnda(self, value: float):
        self._tasaImpuesto = value

    @property
    def VlrImpOtrMnda(self) -> float:
        return round(self._montoImpuesto, 4)

    @VlrImpOtrMnda.setter
    def VlrImpOtrMnda(self, value: float):
        self._montoImpuesto = value


    def __init__(self):
        self.TipoImpOtrMnda = TipoImpuestoEnum.NOT_SET
        self.TasaImpOtrMnda = 0.0
        self.VlrImpOtrMnda = 0.0