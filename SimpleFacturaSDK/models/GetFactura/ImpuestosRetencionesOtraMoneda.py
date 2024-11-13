from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.TipoImpuesto import TipoImpuestoEnum

@dataclass
class ImpuestosRetencionesOtraMoneda:
    TasaImpOtrMnda: float 
    VlrImpOtrMnda: float
    TipoImpOtrMnda: TipoImpuestoEnum

