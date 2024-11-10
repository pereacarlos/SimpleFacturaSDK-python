from dataclasses import dataclass, field
from typing import List
from uuid import UUID

@dataclass
class ImpuestoProductoExternoEnt:
    CodigoSii: int
    NombreImp: str
    Tasa: float

@dataclass
class ProductoExternoEnt:
    ProductoId: UUID
    Nombre: str
    Precio: float
    Exento: bool
    Impuestos: List[ImpuestoProductoExternoEnt]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            ProductoId=UUID(data.get('ProductoId')),
            Nombre=data.get('Nombre'),
            Precio=data.get('Precio'),
            Exento=data.get('Exento'),
            Impuestos=[ImpuestoProductoExternoEnt]
        )

    def to_dict(self):
        return {
            'ProductoId': str(self.ProductoId),
            'Nombre': self.Nombre,
            'Precio': self.Precio,
            'Exento': self.Exento,
            'Impuestos': [imp.__dict__ for imp in self.Impuestos]
        }


@dataclass
class NuevoProductoExternoRequest:
    Nombre: str
    CodigoBarra: str
    UnidadMedida: str
    Precio: float
    Exento: bool
    TieneImpuestos: bool
    Impuestos: List[int]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Nombre=data.get('Nombre'),
            CodigoBarra=data.get('CodigoBarra'),
            UnidadMedida=data.get('UnidadMedida'),
            Precio=data.get('Precio'),
            Exento=data.get('Exento'),
            TieneImpuestos=data.get('TieneImpuestos'),
            Impuestos=data.get('Impuestos')
        )

    def to_dict(self):
        return {
            'Nombre': self.Nombre,
            'CodigoBarra': self.CodigoBarra,
            'UnidadMedida': self.UnidadMedida,
            'Precio': self.Precio,
            'Exento': self.Exento,
            'TieneImpuestos': self.TieneImpuestos,
            'Impuestos': self.Impuestos
        }