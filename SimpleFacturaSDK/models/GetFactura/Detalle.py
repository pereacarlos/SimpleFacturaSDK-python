from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Detalle:
    """
    Clase que representa el detalle del documento.
    """

    NroLinDet: int = 0
    """Número secuencial de línea. De 1 a 60."""

    CdgItem: Optional[List[str]] = field(default_factory=list)
    """Codificación del item. Se pueden incluir 5 repeticiones de pares código-valor."""

    IndExe: Optional[str] = None
    """Indicador de exención/facturación."""

    Retenedor: Optional[str] = None
    """Sólo para transacciones realizadas por agentes retenedores. No aplica para facturas de exportación."""

    NmbItem: str = ''
    """Nombre del producto o servicio."""

    DscItem: Optional[str] = ''
    """Descripción del item."""

    QtyRef: float = 0.0
    """Cantidad para la unidad de medida de referencia."""

    UnmdRef: str = ''
    """Unidad de medida de referencia."""

    PrcRef: float = 0.0
    """Precio unitario de referencia para unidad de medida de referencia."""

    QtyItem: float = 0.0
    """Cantidad del ítem."""

    Subcantidad: Optional[List[str]] = field(default_factory=list)
    """Distribución de la cantidad."""

    FechaElaboracionString: str = ''
    """Fecha de elaboración del item. (AAAA-MM-DD)."""

    FchElabor: datetime = datetime.min
    """Fecha de elaboración del item. (AAAA-MM-DD)."""

    FechaVencimientoString: str = ''
    """Fecha de vencimiento del item. (AAAA-MM-DD)."""

    FchVencim: datetime = datetime.min
    """Fecha de vencimiento del item. (AAAA-MM-DD)."""

    UnmdItem: str = ''
    """Unidad de medida."""

    PrcItem: float = 0.0
    """Precio unitario del item en pesos."""

    OtrMnda: Optional[str] = None
    """Precio del item en otra moneda."""

    DescuentoPct: float = 0.0
    """Porcentaje de descuento."""

    DescuentoMonto: int = 0
    """Monto del descuento."""

    SubDscto: Optional[List[str]] = field(default_factory=list)
    """Desglose del descuento."""

    RecargoPct: float = 0.0
    """Porcentaje de recargo."""

    RecargoMonto: int = 0
    """Monto de recargo."""

    SubRecargo: Optional[List[str]] = field(default_factory=list)
    """Desglose del recargo."""

    CodImpAdic: Optional[List[str]] = field(default_factory=list)
    """Código de impuesto adicional o retención. No aplica para facturas de exportación."""

    MontoItem: int = 0
    """Monto por línea de detalle."""

    def __init__(self):
        self.NroLinDet = 0
        self.NmbItem = ''
        self.MontoItem = 0
        self.CdgItem = []
        self.IndExe = None
        self.Retenedor = None
        self.DscItem = ''
        self.QtyRef = 0.0
        self.UnmdRef = ''
        self.PrcRef = 0.0
        self.QtyItem = 0.0
        self.Subcantidad = []
        self.FchElabor = datetime.min
        self.FchVencim = datetime.min
        self.UnmdItem = ''
        self.PrcItem = 0.0
        self.OtrMnda = None
        self.DescuentoPct = 0.0
        self.DescuentoMonto = 0
        self.SubDscto = []
        self.RecargoPct = 0.0
        self.RecargoMonto = 0
        self.SubRecargo = []
        self.CodImpAdic = []