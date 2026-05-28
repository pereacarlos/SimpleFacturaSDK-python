from dataclasses import dataclass, field
from typing import Optional


@dataclass
class EditarDatosClienteExternoEnt:
    Rut: str
    RazonSocial: Optional[str] = None
    Giro: Optional[str] = None
    DirPart: Optional[str] = None
    DirFact: Optional[str] = None
    CorreoPar: Optional[str] = None
    CorreoFact: Optional[str] = None
    Ciudad: Optional[str] = None
    Comuna: Optional[str] = None

    def to_dict(self):
        return {
            "Rut": self.Rut,
            "RazonSocial": self.RazonSocial,
            "Giro": self.Giro,
            "DirPart": self.DirPart,
            "DirFact": self.DirFact,
            "CorreoPar": self.CorreoPar,
            "CorreoFact": self.CorreoFact,
            "Ciudad": self.Ciudad,
            "Comuna": self.Comuna
        }