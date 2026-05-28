from typing import Optional
from dataclasses import dataclass
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType

@dataclass
class AnularFoliosRequest:
    credenciales: Credenciales
    codigoTipoDte: DTEType
    ambiente: int
    folioInicio: int
    folioTermino: int
    motivoAnulacion: str

    def to_dict(self):
          return {
            "credenciales": self.credenciales.to_dict(),
            "codigoTipoDte" : self.codigoTipoDte.value if self.codigoTipoDte else None,
            "ambiente" : self.ambiente,
            "folioInicio" : self.folioInicio,
            "folioTermino" : self.folioTermino,
            "motivoAnulacion" : self.motivoAnulacion
        }

