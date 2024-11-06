from dataclasses import dataclass, field
from typing import Optional

@dataclass
class DescuentosRecargos:
    """
    Clase que representa los descuentos y recargos del documento.
    """

    NroLinDR: int = 0
    """Número secuencial de línea."""

    TpoMov: Optional[str] = None
    """Tipo de movimiento."""

    _glosa: str = ''
    """Descripción del descuento o recargo."""

    TpoValor: Optional[str] = None
    """Unidad en que se expresa el valor."""

    _valor: float = 0.0
    """Valor del descuento o recargo."""

    _valorOtraMoneda: float = 0.0
    """Valor en otra moneda."""

    IndExeDR: Optional[str] = None
    """Indica si el descuento o recargo es No afecto o no facturable."""

    @property
    def GlosaDR(self) -> str:
        return self._glosa

    @GlosaDR.setter
    def GlosaDR(self, value: str):
        self._glosa = value[:45]  # Truncate to 45 characters

    @property
    def ValorDR(self) -> float:
        return round(self._valor, 2)

    @ValorDR.setter
    def ValorDR(self, value: float):
        self._valor = value

    @property
    def ValorDROtrMnda(self) -> float:
        return round(self._valorOtraMoneda, 4)

    @ValorDROtrMnda.setter
    def ValorDROtrMnda(self, value: float):
        self._valorOtraMoneda = value

    def __init__(self):
        self.NroLinDR = 0
        self.TpoMov = None
        self.GlosaDR = ''
        self.TpoValor = None
        self.ValorDR = 0.0
        self.ValorDROtrMnda = 0.0
        self.IndExeDR = None