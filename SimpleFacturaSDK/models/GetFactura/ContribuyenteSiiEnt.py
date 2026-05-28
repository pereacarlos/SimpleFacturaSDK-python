from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ContribuyenteSiiEnt:
    rut: str
    razonSocial: str
    correoIntercambio: str
    fechaActualizacion: Optional[datetime] = None


    def to_dict(self):
        return {
            "rut": self.rut,
            "razonSocial": self.razonSocial,
            "correoIntercambio": self.correoIntercambio,
            "fechaActualizacion": self.fechaActualizacion
        }
