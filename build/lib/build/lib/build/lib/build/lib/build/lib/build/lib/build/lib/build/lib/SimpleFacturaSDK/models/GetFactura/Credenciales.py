from dataclasses import dataclass
from typing import Optional

@dataclass
class Credenciales:
    rut_emisor: str
    nombre_sucursal: Optional[str] = None
    email_usuario: Optional[str] = None
    rut_contribuyente: Optional[str] = None


    def to_dict(self):
        return {
            "rutEmisor": self.rut_emisor,
            "nombreSucursal": self.nombre_sucursal,
            "emailUsuario": self.email_usuario,
            "rutContribuyente": self.rut_contribuyente
        }
