from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales


@dataclass
class ListaCesionRequest:
    credenciales: Credenciales
    ambiente: AmbienteEnum
    desde: Optional[datetime] = None
    hasta: Optional[datetime] = None

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "ambiente": self.ambiente.value if isinstance(self.ambiente, AmbienteEnum) else self.ambiente,
            "desde": self.desde.isoformat() if isinstance(self.desde, datetime) else self.desde,
            "hasta": self.hasta.isoformat() if isinstance(self.hasta, datetime) else self.hasta,
        }
