from dataclasses import dataclass, field
from typing import List
from uuid import UUID

@dataclass
class ImpuestoProductoExternoEnt:
    codigoSii: int
    nombreImp: str
    tasa: float
@dataclass
class ProductoExternoEnt:
    productoId: UUID
    nombre: str
    precio: float
    exento: bool
    impuestos: List[ImpuestoProductoExternoEnt]

    @classmethod
    def from_dict(cls, data: dict):
        producto_id = data.get('productoId')
        try:
            producto_id = UUID(producto_id) if producto_id else None
        except ValueError:
            raise ValueError(f"productoId '{producto_id}' no es un UUID válido.")

        return cls(
            productoId=producto_id,
            nombre=data.get('nombre', ""),
            precio=data.get('precio', 0.0),
            exento=data.get('exento', False),
            impuestos=[
                ImpuestoProductoExternoEnt(**imp) for imp in data.get('impuestos', [])
            ]
        )

    def to_dict(self):
        return {
            'productoId': str(self.productoId) if self.productoId else None,
            'nombre': self.nombre,
            'precio': self.precio,
            'exento': self.exento,
            'impuestos': [imp.__dict__ for imp in self.impuestos]
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