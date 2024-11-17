from dataclasses import dataclass, field
from typing import Optional
from enumeracion.CodigosAduana import TipoBultoEnum


@dataclass
class TipoBulto:
    CodTpoBultos: TipoBultoEnum
    CantBultos: int
    IdContainer: str 
    Sello: str
    EmisorSello: str 
    Marcas: Optional[str] = None
