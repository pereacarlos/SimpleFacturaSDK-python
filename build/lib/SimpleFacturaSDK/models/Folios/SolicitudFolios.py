from dataclasses import dataclass, field, asdict
from typing import Optional
import json

@dataclass
class SolicitudFolios:
    RutEmpresa: str
    TipoDTE: int
    Ambiente: int

    def __init__(self, RutEmpresa: str, TipoDTE: int, Ambiente: int):
        self.RutEmpresa = RutEmpresa
        self.TipoDTE = TipoDTE
        self.Ambiente = Ambiente