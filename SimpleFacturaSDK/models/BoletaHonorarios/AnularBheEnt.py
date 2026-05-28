from dataclasses import dataclass
from typing import Union

from SimpleFacturaSDK.enumeracion.AnulacionBoletaHonorario import AnulacionBoletaHonorario


@dataclass
class AnularBheEnt:
    RutEmpresa: str
    Folio: int
    Motivo: AnulacionBoletaHonorario

    def to_dict(self):
        return {
            "RutEmpresa": self.RutEmpresa,
            "folio": self.Folio,
            "motivo": self.Motivo.value if isinstance(self.Motivo, AnulacionBoletaHonorario) else self.Motivo,
        }
