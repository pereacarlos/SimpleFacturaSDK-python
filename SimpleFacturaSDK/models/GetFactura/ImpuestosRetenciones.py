from dataclasses import dataclass, field
from enum import Enum

class TipoImpuestoEnum(Enum):
    NotSet = 0
    # Agregar otros códigos de tipo de impuesto según sea necesario

@dataclass
class ImpuestosRetenciones:
    TipoImp: TipoImpuestoEnum = TipoImpuestoEnum.NotSet
    MontoImp: int = 0
    _tasaImpuesto: float = field(default=0.0, init=False)

    @property
    def TasaImp(self) -> float:
        return round(self._tasaImpuesto, 2)

    @TasaImp.setter
    def TasaImp(self, value: float):
        self._tasaImpuesto = value

    def __init__(self):
        self.TipoImp = TipoImpuestoEnum.NOT_SET
        self.TasaImp = 0.0
        self.MontoImp = 0