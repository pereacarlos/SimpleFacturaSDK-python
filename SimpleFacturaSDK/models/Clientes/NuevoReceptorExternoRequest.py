from dataclasses import dataclass, asdict
from uuid import UUID

@dataclass
class ReceptorExternoEnt:
    ReceptorId: UUID
    EmisorId: UUID
    Rut: int
    Dv: str
    RutFormateado: str
    RazonSocial: str
    NombreFantasia: str
    Giro: str
    DirPart: str
    DirFact: str
    CorreoPar: str
    CorreoFact: str
    Ciudad: str
    Comuna: str
    Activo: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            ReceptorId=UUID(data.get('ReceptorId')),
            EmisorId=UUID(data.get('EmisorId')),
            Rut=data.get('Rut'),
            Dv=data.get('Dv'),
            RutFormateado=data.get('RutFormateado'),
            RazonSocial=data.get('RazonSocial'),
            NombreFantasia=data.get('NombreFantasia'),
            Giro=data.get('Giro'),
            DirPart=data.get('DirPart'),
            DirFact=data.get('DirFact'),
            CorreoPar=data.get('CorreoPar'),
            CorreoFact=data.get('CorreoFact'),
            Ciudad=data.get('Ciudad'),
            Comuna=data.get('Comuna'),
            Activo=data.get('Activo')
        )

    def to_dict(self):
        return asdict(self)


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

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Rut=data.get('Rut'),
            RazonSocial=data.get('RazonSocial'),
            Giro=data.get('Giro'),
            DirPart=data.get('DirPart'),
            DirFact=data.get('DirFact'),
            CorreoPar=data.get('CorreoPar'),
            CorreoFact=data.get('CorreoFact'),
            Ciudad=data.get('Ciudad'),
            Comuna=data.get('Comuna')
        )

    def to_dict(self):
        return asdict(self)