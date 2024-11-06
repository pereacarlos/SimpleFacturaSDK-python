from dataclasses import dataclass
from enum import Enum

# Definición de la enumeración
class ExpresionDineroEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

@dataclass
class SubDescuento:
    """
    Clase que representa el subdescuento del documento.
    """

    TipoDscto: ExpresionDineroEnum = ExpresionDineroEnum.NOT_SET
    """Indica en qué está expresado el descuento, en porcentaje (%) o pesos ($)."""

    _valorDescuento: float = 0.0
    """Valor de subdescuento."""

    @property
    def ValorDscto(self) -> float:
        return round(self._valorDescuento, 2)

    @ValorDscto.setter
    def ValorDscto(self, value: float):
        self._valorDescuento = value

    def __init__(self):
        self.TipoDscto = ExpresionDineroEnum.NOT_SET
        self.ValorDscto = 0.0