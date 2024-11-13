from dataclasses import dataclass, field
from uuid import UUID, uuid4
from typing import List, Optional

@dataclass
class ReceptorExternoEnt:
    receptorId: UUID = field(default_factory=uuid4)
    emisorId: UUID = field(default_factory=uuid4)
    rut: int = 0
    dv: str = ""
    rutFormateado: str = ""
    razonSocial: str = ""
    nombreFantasia: str = ""
    giro: str = ""
    dirPart: str = ""
    dirFact: str = ""
    correoPar: str = ""
    correoFact: str = ""
    ciudad: str = ""
    comuna: str = ""
    activo: bool = False

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            receptorId=UUID(data.get('receptorId', str(uuid4()))),
            emisorId=UUID(data.get('emisorId', str(uuid4()))),
            rut=data.get('rut', 0),
            dv=data.get('dv', ""),
            rutFormateado=data.get('rutFormateado', ""),
            razonSocial=data.get('razonSocial', ""),
            nombreFantasia=data.get('nombreFantasia', ""),
            giro=data.get('giro', ""),
            dirPart=data.get('dirPart', ""),
            dirFact=data.get('dirFact', ""),
            correoPar=data.get('correoPar', ""),
            correoFact=data.get('correoFact', ""),
            ciudad=data.get('ciudad', ""),
            comuna=data.get('comuna', ""),
            activo=data.get('activo', False)
        )

    def to_dict(self):
        return {
            "receptorId": str(self.receptorId),
            "emisorId": str(self.emisorId),
            "rut": self.rut,
            "dv": self.dv,
            "rutFormateado": self.rutFormateado,
            "razonSocial": self.razonSocial,
            "nombreFantasia": self.nombreFantasia,
            "giro": self.giro,
            "dirPart": self.dirPart,
            "dirFact": self.dirFact,
            "correoPar": self.correoPar,
            "correoFact": self.correoFact,
            "ciudad": self.ciudad,
            "comuna": self.comuna,
            "activo": self.activo
        }

@dataclass
class NuevoReceptorExternoRequest:
    Rut: str
    RazonSocial: str
    Giro: str
    DirPart: str
    DirFact: str
    CorreoPar: str
    CorreoFact: str
    Ciudad: str
    Comuna: str

    def to_dict(self):
        return {
            "Rut": self.Rut,
            "RazonSocial": self.RazonSocial,
            "Giro": self.Giro,
            "DirPart": self.DirPart,
            "DirFact": self.DirFact,
            "CorreoPar": self.CorreoPar,
            "CorreoFact": self.CorreoFact,
            "Ciudad": self.Ciudad,
            "Comuna": self.Comuna
        }