from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from enumeracion.TipoDTE import DTEType
from enumeracion.IndicadorServicio import IndicadorServicioEnum
@dataclass
class IdDoc:
    TipoDTE: DTEType  
    FchEmis: str
    FchVenc: str
    FmaPago: Optional[int] = None
    IndServicio: Optional[IndicadorServicioEnum] = None

 
