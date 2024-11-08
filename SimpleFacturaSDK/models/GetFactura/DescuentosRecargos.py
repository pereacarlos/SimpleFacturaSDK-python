from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.enumeracion.TipoMovimiento import TipoMovimientoEnum
from SimpleFacturaSDK.enumeracion.ExpresionDinero import ExpresionDineroEnum
from SimpleFacturaSDK.enumeracion.IndicadorExento import IndicadorExentoEnum
def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class DescuentosRecargos:
    nro_lin_dr: int = 0
    tpo_mov: TipoMovimientoEnum = TipoMovimientoEnum.NotSet
    __glosa_dr: str = field(default="", metadata={"max_length": 45})
    tpo_valor: ExpresionDineroEnum = ExpresionDineroEnum.NotSet
    __valor_dr: float = 0.0
    __valorOtroMnda: float = 0.0
    ind_exe_dr: IndicadorExentoEnum = IndicadorExentoEnum.NotSet

    @property
    def glosa_dr(self) -> str:
        return self.__glosa_dr

    @glosa_dr.setter
    def glosa_dr(self, value: str):
        self.__glosa_dr = truncate(value, 45)

    @property
    def valor_dr(self) -> float:
        return round(self.__valor_dr, 2)

    @valor_dr.setter
    def valor_dr(self, value: float):
        self.__valor_dr = value

    @property
    def valorOtroMnda(self) -> float:
        return round(self.__valorOtroMnda, 4)

    @valorOtroMnda.setter
    def valor_dr_otr_mnda(self, value: float):
        self.__valorOtroMnda = value

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
