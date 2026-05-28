from dataclasses import dataclass

from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales


@dataclass
class PartnerDteResumenRequest:
    Credenciales: Credenciales
    Anio: int
    Mes: int

    def to_dict(self):
        return {
            "credenciales": self.Credenciales.to_dict(),
            "anio": self.Anio,
            "mes": self.Mes,
        }


@dataclass
class PartnerDteResumenResponse:
    dtes: int = 0
    nombrePlan: str = ""
    dtesAdicionales: int = 0
