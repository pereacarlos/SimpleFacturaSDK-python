from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoImpuestoEnum import TipoImpuestoEnum

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
        self.TipoImp = TipoImpuestoEnum.NotSet
        self.TasaImp = 0.0
        self.MontoImp = 0