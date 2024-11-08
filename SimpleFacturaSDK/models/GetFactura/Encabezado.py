from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.models.GetFactura.IdentificacionDTE import IdentificacionDTE
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.models.GetFactura.Transporte import Transporte
from SimpleFacturaSDK.models.GetFactura.Totales import Totales
from SimpleFacturaSDK.models.GetFactura.OtraMoneda import OtraMoneda

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

    def __init__(self, IdDoc: IdentificacionDTE = None, Emisor: Emisor = None, RUTMandante: str = '', Receptor: Receptor = None, RUTSolicita: str = '', Transporte: Transporte = None, Totales: Totales = None, OtraMoneda: OtraMoneda = None):
        self.IdDoc = IdDoc
        self.Emisor = Emisor
        self.RUTMandante = RUTMandante
        self.Receptor = Receptor
        self.RUTSolicita = RUTSolicita
        self.Transporte = Transporte
        self.Totales = Totales
        self.OtraMoneda = OtraMoneda
        