from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.enum.TipoRecargoComisionEnum import TipoRecargoComisionEnum
@dataclass
class ComisionRecargo:
    NroLinCom: int = 0
    TipoMovim: TipoRecargoComisionEnum = TipoRecargoComisionEnum.NotSet
    _glosa: str = ''
    _tasa: float = 0.0
    ValComNeto: int = 0
    ValComExe: int = 0
    ValComIVA: int = 0

    @property
    def Glosa(self) -> str:
        return self._glosa

    @Glosa.setter
    def Glosa(self, value: str):
        self._glosa = value[:60]

    @property
    def TasaComision(self) -> float:
        return round(self._tasa, 2)

    @TasaComision.setter
    def TasaComision(self, value: float):
        self._tasa = value

    def __init__(self):
        self.NroLinCom = 0
        self.TipoMovim = TipoRecargoComisionEnum.NotSet
        self.Glosa = ''
        self.TasaComision = 0.0
        self.ValComNeto = 0
        self.ValComExe = 0
        self.ValComIVA = 0