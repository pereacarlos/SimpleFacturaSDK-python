from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicioEnum
@dataclass
class IdDoc:
    TipoDTE: DTEType  
    FchEmis: str
    FchVenc: str
    FmaPago: Optional[int] = None
    IndServicio: Optional[IndicadorServicioEnum] = None

 
