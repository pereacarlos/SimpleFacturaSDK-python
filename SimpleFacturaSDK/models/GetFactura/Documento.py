from dataclasses import dataclass, field
from typing import List
from datetime import datetime

# Import or define the classes used by Documento
class Encabezado:
    """Class definition for Encabezado"""
    pass

class Detalle:
    """Class definition for Detalle"""
    pass

class SubTotal:
    """Class definition for SubTotal"""
    pass

class DescuentosRecargos:
    """Class definition for DescuentosRecargos"""
    pass

class Referencia:
    """Class definition for Referencia"""
    pass

class ComisionRecargo:
    """Class definition for ComisionRecargo"""
    pass

@dataclass
class Documento:
    """
    Información tributaria del DTE
    """
    Id: str = field(default_factory=lambda: f"T_{int(datetime.now().timestamp() * 1e6)}")

    Encabezado: Encabezado = field(default_factory=Encabezado)

    Detalles: List[Detalle] = field(default_factory=list)

    SubTotales: List[SubTotal] = field(default_factory=list)
    def ShouldSerializeSubTotales(self) -> bool:
        return bool(self.SubTotales)

    DescuentosRecargos: List[DescuentosRecargos] = field(default_factory=list)
    def ShouldSerializeDescuentosRecargos(self) -> bool:
        return bool(self.DescuentosRecargos)

    Referencias: List[Referencia] = field(default_factory=list)
    def ShouldSerializeReferencias(self) -> bool:
        return bool(self.Referencias)

    Comisiones: List[ComisionRecargo] = field(default_factory=list)
    def ShouldSerializeComisiones(self) -> bool:
        return bool(self.Comisiones)

    def __post_init__(self):
        # Initialize with default values similar to the C# constructor
        self.Id = self.Id or f"T_{int(datetime.now().timestamp() * 1e6)}"
        self.Encabezado = self.Encabezado or Encabezado()
        self.Detalles = self.Detalles or []
        self.SubTotales = self.SubTotales or []
        self.DescuentosRecargos = self.DescuentosRecargos or []
        self.Referencias = self.Referencias or []
        self.Comisiones = self.Comisiones or []
