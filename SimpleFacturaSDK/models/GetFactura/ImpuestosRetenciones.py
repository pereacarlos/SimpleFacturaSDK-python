from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoImpuesto import TipoImpuestoEnum

@dataclass
class ImpuestosRetenciones:
    TipoImp: TipoImpuestoEnum = TipoImpuestoEnum.NotSet
    TasaImp: float = 0.0
    MontoImp: int = 0
    _tasaImpuesto: float = field(default=0.0, init=False, metadata={"decimals": 2})

    def __post_init__(self):
        self._tasaImpuesto = round(self.TasaImp, 2)
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TipoImp=TipoImpuestoEnum(data.get('TipoImp')),
            TasaImp=data.get('TasaImp'),
            MontoImp=data.get('MontoImp')
        )