from typing import Optional
from dataclasses import dataclass
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType

@dataclass
class FolioRequest:
    credenciales: Credenciales
    Cantidad: Optional[int] = None
    CodigoTipoDte: Optional[DTEType] = None
    Ambiente: Optional[int] = None

