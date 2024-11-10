from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoImpuesto import TipoImpuestoEnum

@dataclass
class ImpuestosRetenciones:
    TipoImp: TipoImpuestoEnum = TipoImpuestoEnum.NotSet
    TasaImp: float
    MontoImp: int 
    _tasaImpuesto: float

    def __post_init__(self):
        self._tasaImpuesto = round(self.TasaImp, 2)
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TipoImp=TipoImpuestoEnum(data.get('TipoImp')),
            TasaImp=data.get('TasaImp'),
            MontoImp=data.get('MontoImp')
        )