from dataclasses import dataclass
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales


@dataclass
class CertificadoDigitalRequest:
    Credenciales: Credenciales
    RutCertificado: str
    Password: str


    def to_dict(self):
          return {
            "credenciales": self.Credenciales.to_dict(),
            "rutCertificado" : self.RutCertificado,
            "password" : self.Password
        }