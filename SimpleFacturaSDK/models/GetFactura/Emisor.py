from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Emisor:
    RUTEmisor: str
    RznSoc: str = ""
    GiroEmis: str = ""
    Telefono: List[str] = field(default_factory=list)
    CorreoEmisor: str = ""
    Acteco: List[int] = field(default_factory=list)
    DirOrigen: str = ""
    CmnaOrigen: str = ""
    CiudadOrigen: str = ""
    RznSocEmisor: Optional[str] = None
    GiroEmisor: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Emisor":
        return cls(
            RUTEmisor=data.get("RUTEmisor", ""),
            RznSoc=data.get("RznSoc", ""),
            GiroEmis=data.get("GiroEmis", ""),
            Telefono=data.get("Telefono", []),
            CorreoEmisor=data.get("CorreoEmisor", ""),
            Acteco=data.get("Acteco", []),
            DirOrigen=data.get("DirOrigen", ""),
            CmnaOrigen=data.get("CmnaOrigen", ""),
            CiudadOrigen=data.get("CiudadOrigen", ""),
            RznSocEmisor=data.get("RznSocEmisor"),
            GiroEmisor=data.get("GiroEmisor")
        )
