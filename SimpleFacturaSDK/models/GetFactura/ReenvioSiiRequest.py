from typing import Optional
from dataclasses import dataclass
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType

@dataclass
class ReenvioSiiRequest:
    Credenciales: Credenciales
    ambiente: Optional[AmbienteEnum] = None
    folio: Optional[float] = None
    codigoTipoDte: Optional[DTEType] = None

    def to_dict(self):
          return {
            "credenciales": self.Credenciales.to_dict(),
            "ambiente": self.ambiente.value if self.ambiente else None,
            "folio": self.folio,
            "codigoTipoDte": self.codigoTipoDte.value if self.codigoTipoDte else None
        }