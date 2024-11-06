from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Definición de las enumeraciones
class IndicadorFacturacionExencionEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

class TipoImpuestoEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

@dataclass
class Detalle:
    """
    Clase que representa el detalle del documento.
    """

    NroLinDet: int = 0
    """Número secuencial de línea. De 1 a 60."""

    CdgItem: Optional[List[str]] = field(default_factory=list)
    """Codificación del item. Se pueden incluir 5 repeticiones de pares código-valor."""

    IndExe: Optional[IndicadorFacturacionExencionEnum] = IndicadorFacturacionExencionEnum.NOT_SET
    """Indicador de exención/facturación."""

    Retenedor: Optional[str] = None
    """Sólo para transacciones realizadas por agentes retenedores. No aplica para facturas de exportación."""

    _nombre: str = ''
    """Nombre del producto o servicio."""

    _descripcion: str = ''
    """Descripción del item."""

    _cantidadUnidadMedidaReferencia: float = 0.0
    """Cantidad para la unidad de medida de referencia."""

    _unidadMedidaReferencia: str = ''
    """Unidad de medida de referencia."""

    _precioUnitarioUnidadMedidaReferencia: float = 0.0
    """Precio unitario de referencia para unidad de medida de referencia."""

    _cantidad: float = 0.0
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

    _unidadMedida: str = ''
    """Unidad de medida."""

    _precio: float = 0.0
    """Precio unitario del item en pesos."""

    OtrMnda: Optional[str] = None
    """Precio del item en otra moneda."""

    _descuentoPorcentaje: float = 0.0
    """Porcentaje de descuento."""

    DescuentoMonto: int = 0
    """Monto del descuento."""

    SubDscto: Optional[List[str]] = field(default_factory=list)
    """Desglose del descuento."""

    _recargoPorcentaje: float = 0.0
    """Porcentaje de recargo."""

    RecargoMonto: int = 0
    """Monto de recargo."""

    SubRecargo: Optional[List[str]] = field(default_factory=list)
    """Desglose del recargo."""

    CodImpAdic: Optional[List[TipoImpuestoEnum]] = field(default_factory=list)
    """Código de impuesto adicional o retención. No aplica para facturas de exportación."""

    MontoItem: int = 0
    """Monto por línea de detalle."""

    @property
    def NmbItem(self) -> str:
        return self._nombre

    @NmbItem.setter
    def NmbItem(self, value: str):
        self._nombre = value[:80]  # Truncate to 80 characters

    @property
    def DscItem(self) -> str:
        return self._descripcion

    @DscItem.setter
    def DscItem(self, value: str):
        self._descripcion = value[:1000]  # Truncate to 1000 characters

    @property
    def QtyRef(self) -> float:
        return round(self._cantidadUnidadMedidaReferencia, 6)

    @QtyRef.setter
    def QtyRef(self, value: float):
        self._cantidadUnidadMedidaReferencia = value

    @property
    def UnmdRef(self) -> str:
        return self._unidadMedidaReferencia

    @UnmdRef.setter
    def UnmdRef(self, value: str):
        self._unidadMedidaReferencia = value[:4]  # Truncate to 4 characters

    @property
    def PrcRef(self) -> float:
        return round(self._precioUnitarioUnidadMedidaReferencia, 6)

    @PrcRef.setter
    def PrcRef(self, value: float):
        self._precioUnitarioUnidadMedidaReferencia = value

    @property
    def QtyItem(self) -> float:
        return round(self._cantidad, 6)

    @QtyItem.setter
    def QtyItem(self, value: float):
        self._cantidad = value

    @property
    def UnmdItem(self) -> str:
        return self._unidadMedida

    @UnmdItem.setter
    def UnmdItem(self, value: str):
        self._unidadMedida = value[:4]  # Truncate to 4 characters

    @property
    def PrcItem(self) -> float:
        return self._precio

    @PrcItem.setter
    def PrcItem(self, value: float):
        self._precio = value

    @property
    def DescuentoPct(self) -> float:
        return round(self._descuentoPorcentaje, 2)

    @DescuentoPct.setter
    def DescuentoPct(self, value: float):
        self._descuentoPorcentaje = value

    @property
    def RecargoPct(self) -> float:
        return round(self._recargoPorcentaje, 2)

    @RecargoPct.setter
    def RecargoPct(self, value: float):
        self._recargoPorcentaje = value

    def __init__(self):
        self.NroLinDet = 0
        self.NmbItem = ''
        self.MontoItem = 0
        self.CdgItem = []
        self.IndExe = IndicadorFacturacionExencionEnum.NOT_SET
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