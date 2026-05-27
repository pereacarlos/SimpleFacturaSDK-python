from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class AnularGuiaRequest:
    RutEmpresa: str
    Folio: int
    Ambiente: int

    def to_dict(self):
        return {
            "RutEmpresa": self.RutEmpresa,
            "Folio": self.Folio,
            "Ambiente": self.Ambiente
        }
   