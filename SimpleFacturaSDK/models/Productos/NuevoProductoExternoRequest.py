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
    nombre: str
    codigoBarra: str
    unidadMedida: str
    precio: float
    exento: bool
    tieneImpuestos: bool
    impuestos: List[int]


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nombre=data.get('nombre'),
            codigoBarra=data.get('codigoBarra'),
            unidadMedida=data.get('unidadMedida'),
            precio=data.get('precio'),
            exento=data.get('exento'),
            tieneImpuestos=data.get('tieneImpuestos'),
            impuestos=data.get('impuestos')
        )

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'codigoBarra': self.codigoBarra,
            'unidadMedida': self.unidadMedida,
            'precio': self.precio,
            'exento': self.exento,
            'tieneImpuestos': self.tieneImpuestos,
            'impuestos': self.impuestos
        }