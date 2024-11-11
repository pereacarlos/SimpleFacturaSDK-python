from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.enumeracion.CodigosAduana import TipoBultoEnum


def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class TipoBulto:
    CodTpoBultos: TipoBultoEnum
    CantBultos: int
    IdContainer: str 
    Sello: str
    EmisorSello: str 
    Marcas: Optional[str] = None
