from typing import Optional
from dataclasses import dataclass
from models.GetFactura.Credenciales import Credenciales
from enumeracion.TipoDTE import DTEType

@dataclass
class FolioRequest:
    credenciales: Credenciales
    Cantidad: Optional[int] = None
    CodigoTipoDte: Optional[DTEType] = None
    Ambiente: Optional[int] = None

