from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.enumeracion.TipoRecargoComision import TipoRecargoComisionEnum

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class ComisionRecargo:
    NroLinCom: int = 0
    TipoMovim: TipoRecargoComisionEnum = TipoRecargoComisionEnum.NotSet
    Glosa: str = ''
    TasaComision: float = 0.0

    __glosa: str = field(default="", metadata={"max_length": 60})
    __tasa: float = field(default=0.0, metadata={"decimals": 2})
    ValComNeto: int = 0
    ValComExe: int = 0
    ValComIVA: int = 0

    def __post_init__(self):
        self.__glosa = truncate(self.Glosa, 60)
        self.__tasa = round(self.TasaComision, 2)


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            NroLinCom=data.get('NroLinCom'),
            TipoMovim=TipoRecargoComisionEnum(data.get('TipoMovim')),
            Glosa=data.get('Glosa'),
            TasaComision=data.get('TasaComision'),
            ValComNeto=data.get('ValComNeto'),
            ValComExe=data.get('ValComExe'),
            ValComIVA=data.get('ValComIVA')
        )