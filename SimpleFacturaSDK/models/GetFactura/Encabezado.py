from dataclasses import dataclass
from typing import Optional
from SimpleFacturaSDK.models.GetFactura.IdentificacionDTE import IdDoc
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.models.GetFactura.Transporte import Transporte
from SimpleFacturaSDK.models.GetFactura.Totales import Totales
from SimpleFacturaSDK.models.GetFactura.OtraMoneda import OtraMoneda

@dataclass
class Encabezado:
    IdDoc: IdDoc
    Emisor: Emisor
    Receptor: Receptor
    Totales: Totales
    Transporte: Optional[Transporte] = None
    OtraMoneda: Optional[OtraMoneda] = None
   