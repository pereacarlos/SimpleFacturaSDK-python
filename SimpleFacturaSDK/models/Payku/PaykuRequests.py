from dataclasses import dataclass
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno


@dataclass
class PaykuTransaccionesRequest:
    credenciales: Credenciales
    desde: datetime
    hasta: datetime

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "desde": self.desde.strftime("%Y-%m-%d") if isinstance(self.desde, datetime) else self.desde,
            "hasta": self.hasta.strftime("%Y-%m-%d") if isinstance(self.hasta, datetime) else self.hasta,
        }


@dataclass
class PaykuToggleRequest:
    credenciales: Credenciales
    activo: bool

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "activo": self.activo,
        }


@dataclass
class PaykuReenviarLinkRequest:
    credenciales: Credenciales
    dte: DteReferenciadoExterno

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "dte": self.dte.to_dict(),
        }


@dataclass
class MarcarPagadoOPendienteRequest:
    credenciales: Credenciales
    dteReferenciadoExterno: DteReferenciadoExterno
    pagado: bool

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "dteReferenciadoExterno": self.dteReferenciadoExterno.to_dict(),
            "pagado": self.pagado,
        }
