from dataclasses import dataclass, field
from typing import Optional
from models.GetFactura.Chofer import Chofer
from models.GetFactura.Aduana import Aduana

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

    

@dataclass
class Transporte:
    Patente: Optional[str] = None
    RUTTrans: Optional[str] = None
    Chofer: Optional[Chofer]= None
    DirDest: Optional[str] = None
    CmnaDest: Optional[str] = None
    CiudadDest: Optional[str] = None
    Aduana: Optional[Aduana] = None
