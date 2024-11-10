from typing import Optional
from dataclasses import dataclass, field

@dataclass
class CredencialExternaEnt:
    email_usuario: Optional[str] = field(default=None, repr=False)  # Equivalente a [JsonIgnore]
    rut_emisor: Optional[str] = None
    rut_contribuyente: Optional[str] = None
    nombre_sucursal: Optional[str] = None

    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            email_usuario=data.get('emailUsuario'),
            rut_emisor=data.get('rutEmisor'),
            rut_contribuyente=data.get('rutContribuyente'),
            nombre_sucursal=data.get('nombreSucursal')
        )