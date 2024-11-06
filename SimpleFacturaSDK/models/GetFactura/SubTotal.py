from dataclasses import dataclass, field
from typing import List

@dataclass
class SubTotal:
    """
    Clase que representa el subtotal del documento.
    """

    NroSTI: int = 0
    """Número de sub-total. Número secuencial de acuerdo al número de subtotales."""

    _glosa: str = ''
    """Glosa. Título del subtotal."""

    OrdenSTI: int = 0
    """Ubicación para impresión. De uso para el contribuyente como ayuda para indicar cómo se imprimirá los subtotales."""

    _neto: float = 0.0
    """Valor neto del subtotal."""

    _iva: float = 0.0
    """Valor del IVA del subtotal."""

    _impuestoAdicional: float = 0.0
    """Valor de los impuestos adicionales o específicos del subtotal."""

    _montoExento: float = 0.0
    """Valor no afecto o exento del subtotal."""

    _total: float = 0.0
    """Valor de la línea de subtotal."""

    LineasDeta: List[int] = field(default_factory=list)
    """Tabla de líneas de detalle que se agrupan en el subtotal."""

    @property
    def GlosaSTI(self) -> str:
        return self._glosa

    @GlosaSTI.setter
    def GlosaSTI(self, value: str):
        self._glosa = value[:40]  # Truncate to 40 characters

    @property
    def SubTotNetoSTI(self) -> float:
        return round(self._neto, 2)

    @SubTotNetoSTI.setter
    def SubTotNetoSTI(self, value: float):
        self._neto = value

    @property
    def SubTotIVASTI(self) -> float:
        return round(self._iva, 2)

    @SubTotIVASTI.setter
    def SubTotIVASTI(self, value: float):
        self._iva = value

    @property
    def SubTotAdicSTI(self) -> float:
        return round(self._impuestoAdicional, 2)

    @SubTotAdicSTI.setter
    def SubTotAdicSTI(self, value: float):
        self._impuestoAdicional = value

    @property
    def SubTotExeSTI(self) -> float:
        return round(self._montoExento, 2)

    @SubTotExeSTI.setter
    def SubTotExeSTI(self, value: float):
        self._montoExento = value

    @property
    def ValSubtotSTI(self) -> float:
        return round(self._total, 2)

    @ValSubtotSTI.setter
    def ValSubtotSTI(self, value: float):
        self._total = value

    def __init__(self):
        self.NroSTI = 0
        self.GlosaSTI = ''
        self.OrdenSTI = 0
        self.SubTotNetoSTI = 0.0
        self.SubTotIVASTI = 0.0
        self.SubTotAdicSTI = 0.0
        self.SubTotExeSTI = 0.0
        self.ValSubtotSTI = 0.0
        self.LineasDeta = []