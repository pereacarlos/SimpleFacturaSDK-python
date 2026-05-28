from dataclasses import dataclass
from typing import Optional

@dataclass
class BasicData:
    RutUsuario : str = ""
    RutCertificado : str = ""
    Password : str = ""
    RutEmpresa : str = ""
    Ambiente : int = 0
    Detallado : bool = False
    CertificadoB64 : bytes = b""
    PasswordSII : Optional[str] = ""
    def to_dict(self):
          return {
            "rutUsuario": self.RutUsuario,
            "passwordSII": self.PasswordSII,
            "rutCertificado": self.RutCertificado,
            "password": self.Password,
            "rutEmpresa": self.RutEmpresa,
            "ambiente": self.Ambiente,
            "detallado": self.Detallado,
            "certificadoB64": self.CertificadoB64
        }
