from dataclasses import dataclass, field
from typing import List, Optional
from uuid import UUID
from SimpleFacturaSDK.models.Productos.ImpuestoEnt import ImpuestoEnt

@dataclass
class ProductoEnt:
    ProductoId: UUID
    CodigoBarra: Optional[str]
    Nombre: str 
    Precio: float 
    Exento: bool 
    Activo: bool 
    EmisorId: UUID
    SucursalId: UUID
    UnidadMedida: Optional[str]
    Impuestos: List[ImpuestoEnt] 

    @property
    def NombreCategoria(self) -> str:
        return "Sin Categoría"

    @property
    def NombreMarca(self) -> str:
        return "Sin Marca"

    @property
    def Stock(self) -> int:
        return 50

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            ProductoId=UUID(data.get('ProductoId')),
            CodigoBarra=data.get('CodigoBarra'),
            Nombre=data.get('Nombre'),
            Precio=data.get('Precio'),
            Exento=data.get('Exento'),
            Activo=data.get('Activo'),
            EmisorId=UUID(data.get('EmisorId')),
            SucursalId=UUID(data.get('SucursalId')),
            UnidadMedida=data.get('UnidadMedida'),
            Impuestos=[ImpuestoEnt]
        )

    def to_dict(self):
        return {
            'ProductoId': str(self.ProductoId),
            'CodigoBarra': self.CodigoBarra,
            'Nombre': self.Nombre,
            'Precio': self.Precio,
            'Exento': self.Exento,
            'Activo': self.Activo,
            'EmisorId': str(self.EmisorId),
            'SucursalId': str(self.SucursalId),
            'UnidadMedida': self.UnidadMedida,
            'Impuestos': [imp.to_dict() for imp in self.Impuestos],
            'NombreCategoria': self.NombreCategoria,
            'NombreMarca': self.NombreMarca,
            'Stock': self.Stock
        }