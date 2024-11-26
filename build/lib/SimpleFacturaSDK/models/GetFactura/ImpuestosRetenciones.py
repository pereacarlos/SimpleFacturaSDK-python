from dataclasses import dataclass, field
from enumeracion.TipoImpuesto import TipoImpuestoEnum

@dataclass
class ImpuestosRetenciones:
    TasaImp: float
    MontoImp: int 
    TipoImp:TipoImpuestoEnum

