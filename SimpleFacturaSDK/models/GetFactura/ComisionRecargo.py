from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

# Definición de las enumeraciones
class TipoRecargoComisionEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

@dataclass
class ComisionRecargo:
    """
    Clase que representa la comisión o recargo del documento.
    """

    NroLinCom: int = 0
    """Número secuencial de la línea."""

    TipoMovim: TipoRecargoComisionEnum = TipoRecargoComisionEnum.NOT_SET
    """C (Comisión) u O (Otros cargos)."""

    _glosa: str = ''
    """Especificación de la comisión u otro cargo."""

    _tasa: float = 0.0
    """Valor porcentual de la comisión u otro cargo."""

    ValComNeto: int = 0
    """Valor neto de la comisión u otro cargo."""

    ValComExe: int = 0
    """Valor no afecto o exento de la comisión u otros cargos."""

    ValComIVA: int = 0
    """Valor IVA de la comisión u otros cargos."""

    @property
    def Glosa(self) -> str:
        return self._glosa

    @Glosa.setter
    def Glosa(self, value: str):
        self._glosa = value[:60]  # Truncate to 60 characters

    @property
    def TasaComision(self) -> float:
        return round(self._tasa, 2)

    @TasaComision.setter
    def TasaComision(self, value: float):
        self._tasa = value

    def __init__(self):
        self.NroLinCom = 0
        self.TipoMovim = TipoRecargoComisionEnum.NOT_SET
        self.Glosa = ''
        self.TasaComision = 0.0
        self.ValComNeto = 0
        self.ValComExe = 0
        self.ValComIVA = 0