from dataclasses import dataclass, field
from typing import List, Optional
from uuid import UUID
from SimpleFacturaSDK.models.Productos.ImpuestoEnt import ImpuestoEnt

@dataclass
class ProductoEnt:
    productoId: UUID
    nombre: Optional[str] = None
    precio: Optional[float] = None
    exento: Optional[bool] = None
    activo: Optional[bool] = None
    emisorId: Optional[UUID] = None
    sucursalId: Optional[UUID] = None
    impuestos: Optional[List[ImpuestoEnt]] = None
    codigoBarra: Optional[str] = None
    unidadMedida: Optional[str] = None
    @property
    def NombreCategoria(self) -> str:
        return "Sin Categoría"

    @property
    def NombreMarca(self) -> str:
        return "Sin Marca"

    @property
    def Stock(self) -> int:
        return 50

