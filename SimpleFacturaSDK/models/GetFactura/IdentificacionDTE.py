from dataclasses import dataclass
from datetime import datetime
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicioEnum
@dataclass
class IdDoc:
    TipoDTE: DTEType  
    FchEmis: str
    FmaPago: int
    FchVenc: str
    IndServicio: IndicadorServicioEnum
