from dataclasses import dataclass, field
from typing import Optional
from IdentificacionDTE import IdentificacionDTE
from Emisor import Emisor
from Receptor import Receptor
from Transporte import Transporte
from Totales import Totales
from OtraMoneda import OtraMoneda

@dataclass
class Encabezado:
    IdDoc: IdentificacionDTE = field(default_factory=IdentificacionDTE)
    Emisor: Emisor = field(default_factory=Emisor)
    RUTMandante: Optional[str] = field(default='')
    Receptor: Receptor = field(default_factory=Receptor)
    RUTSolicita: Optional[str] = field(default='')
    Transporte: Optional[Transporte] = None
    Totales: Totales = field(default_factory=Totales)
    OtraMoneda: Optional[OtraMoneda] = None

    def __init__(self):
        self.RUTMandante = ''
        self.RUTSolicita = ''
        self.IdDoc = IdentificacionDTE()
        self.Emisor = Emisor()
        self.Receptor = Receptor()
        self.Transporte = None
        self.Totales = Totales()
        self.OtraMoneda = None