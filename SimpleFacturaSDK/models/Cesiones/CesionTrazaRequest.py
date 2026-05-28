from dataclasses import dataclass
from typing import Union

from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales


@dataclass
class CesionTrazaRequest:
    credenciales: Credenciales
    folio: int
    ambiente: AmbienteEnum

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "folio": self.folio,
            "ambiente": self.ambiente.value if isinstance(self.ambiente, AmbienteEnum) else self.ambiente,
        }
