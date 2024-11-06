from dataclasses import dataclass
from enum import Enum

# Definición de la enumeración
class ExpresionDineroEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

@dataclass
class SubRecargo:
    """
    Clase que representa el subrecargo del documento.
    """

    TipoRecargo: ExpresionDineroEnum = ExpresionDineroEnum.NOT_SET
    """Tipo de subdescuento."""

    _valorRecargo: float = 0.0
    """Valor de subdescuento."""

    @property
    def ValorRecargo(self) -> float:
        return round(self._valorRecargo, 2)

    @ValorRecargo.setter
    def ValorRecargo(self, value: float):
        self._valorRecargo = value

    def __init__(self):
        self.TipoRecargo = ExpresionDineroEnum.NOT_SET
        self.ValorRecargo = 0.0