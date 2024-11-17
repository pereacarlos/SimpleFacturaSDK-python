from dataclasses import dataclass
from models.GetFactura.Credenciales import Credenciales
from models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
@dataclass
class SolicitudPdfDte:
    credenciales: Credenciales
    dte_referenciado_externo: DteReferenciadoExterno

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "dteReferenciadoExterno": self.dte_referenciado_externo.to_dict()
        }