from dataclasses import dataclass
from typing import Optional
from SimpleFacturaSDK.models.GetFactura.Extranjero import Extranjero

@dataclass
class Receptor:
    RUTRecep: str
    RznSocRecep: str
    CorreoRecep: str
    DirRecep: str
    CmnaRecep: str
    CiudadRecep: str
    GiroRecep: str = "" 
    Extranjero: Optional[Extranjero] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Receptor":
        return cls(
            RUTRecep=data.get("RUTRecep", ""),
            RznSocRecep=data.get("RznSocRecep", ""),
            CorreoRecep=data.get("CorreoRecep", ""),
            DirRecep=data.get("DirRecep", ""),
            CmnaRecep=data.get("CmnaRecep", ""),
            CiudadRecep=data.get("CiudadRecep", ""),
            GiroRecep=data.get("GiroRecep", ""),
            Extranjero=Extranjero.from_dict(data.get("Extranjero")) if data.get("Extranjero") else None
        )