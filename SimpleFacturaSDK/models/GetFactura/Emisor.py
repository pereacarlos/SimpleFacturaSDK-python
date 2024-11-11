from dataclasses import dataclass
from typing import List
@dataclass
class Emisor:
    RUTEmisor: str
    RznSoc: str
    GiroEmis: str
    Telefono: List[str]
    CorreoEmisor: str
    Acteco: List[int]
    DirOrigen: str
    CmnaOrigen: str
    CiudadOrigen: str
    RznSocEmisor: str
    GiroEmisor: str