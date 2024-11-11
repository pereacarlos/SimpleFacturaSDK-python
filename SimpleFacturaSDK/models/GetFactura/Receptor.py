from dataclasses import dataclass
from typing import Optional
from SimpleFacturaSDK.models.GetFactura.Extranjero import Extranjero

@dataclass
class Receptor:
    RUTRecep: str
    RznSocRecep: str
    GiroRecep: str
    CorreoRecep: str
    DirRecep: str
    CmnaRecep: str
    CiudadRecep: str
    Extranjero: Optional[Extranjero] = None