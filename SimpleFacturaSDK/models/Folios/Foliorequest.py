from typing import Optional
from dataclasses import dataclass
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType

@dataclass
class FolioRequest:
    credenciales: Credenciales
    Cantidad: Optional[int] = None
    CodigoTipoDte: Optional[DTEType] = None
    ambiente: Optional[int] = None

    def to_dict(self):
        return {
            "Credenciales": self.credenciales.to_dict(),
            "Cantidad": self.Cantidad,
            "CodigoTipoDte": self.CodigoTipoDte.value if self.CodigoTipoDte else None,
            "Ambiente": self.ambiente
        }