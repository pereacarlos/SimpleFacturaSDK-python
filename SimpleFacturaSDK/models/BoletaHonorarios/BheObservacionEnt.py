from dataclasses import dataclass

from SimpleFacturaSDK.enumeracion.ObservacionBoletaHonorario import ObservacionBoletaHonorario


@dataclass
class BheObservacionEnt:
    RutEmpresa: str
    rutContribuyente: str
    Folio: int
    Observacion: ObservacionBoletaHonorario

    def to_dict(self):
        return {
            "RutEmpresa": self.RutEmpresa,
            "rutContribuyente": self.rutContribuyente,
            "folio": self.Folio,
            "Observacion": self.Observacion.value if isinstance(self.Observacion, ObservacionBoletaHonorario) else self.Observacion,
        }
