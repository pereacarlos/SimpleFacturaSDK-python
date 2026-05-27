from dataclasses import dataclass
from SimpleFacturaSDK.enumeracion.SyncTypeEnum import SyncTypeEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales


@dataclass
class UltimaSyncRequest:
    Credenciales: Credenciales
    Tipo: SyncTypeEnum


    def to_dict(self):
          return {
            "credenciales": self.Credenciales.to_dict(),
            "tipo" : self.Tipo.value if self.Tipo else None
        }