from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.enumeracion.TipoMovimiento import TipoMovimientoEnum
from SimpleFacturaSDK.enumeracion.ExpresionDinero import ExpresionDineroEnum
from SimpleFacturaSDK.enumeracion.IndicadorExento import IndicadorExentoEnum
def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class DescuentosRecargos:
    NroLinDR: int = 0
    TpoMov: TipoMovimientoEnum = TipoMovimientoEnum.NotSet
    GlosaDR: str = ""
    tpo_valor: ExpresionDineroEnum = ExpresionDineroEnum.NotSet
    ValorDR: float = 0.0
    ValorDROtrMnda: float = 0.0

    __glosa: str = field(default="", metadata={"max_length": 45})
    __valor: float = field(default=0.0, metadata={"decimals": 2})
    __valorOtraMoneda: float = field(default=0.0, metadata={"decimals": 4})
    ind_exe_dr: IndicadorExentoEnum = IndicadorExentoEnum.NotSet

    def __post_init__(self):
        self.__glosa = truncate(self.GlosaDR, 45)
        self.__valor = round(self.ValorDR, 2)
        self.__valorOtraMoneda = round(self.ValorDROtrMnda, 4)

        

   
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nro_lin_dr=data.get('nroLinDR'),
            tpo_mov=TipoMovimientoEnum(data.get('tpoMov')),
            glosa_dr=data.get('glosaDR'),
            tpo_valor=ExpresionDineroEnum(data.get('tpoValor')),
            valor_dr=data.get('valorDR'),
            valorOtroMnda=data.get('valorOtroMnda'),
            ind_exe_dr=IndicadorExentoEnum(data.get('indExeDR'))
        )
