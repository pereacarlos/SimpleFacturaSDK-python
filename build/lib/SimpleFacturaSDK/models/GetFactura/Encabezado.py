from dataclasses import dataclass
from typing import Optional
from models.GetFactura.IdentificacionDTE import IdDoc
from models.GetFactura.Emisor import Emisor
from models.GetFactura.Receptor import Receptor
from models.GetFactura.Transporte import Transporte
from models.GetFactura.Totales import Totales
from models.GetFactura.OtraMoneda import OtraMoneda

@dataclass
class Encabezado:
    IdDoc: IdDoc
    Emisor: Emisor
    Receptor: Receptor
    Totales: Totales
    Transporte: Optional[Transporte] = None
    OtraMoneda: Optional[OtraMoneda] = None
   