from dataclasses import dataclass, field
from typing import List

@dataclass
class SubTotal:
    NroSTI: int = 0
    __glosa: str = ''
    OrdenSTI: int = 0
    __neto: float = 0.0
    __iva: float = 0.0
    __impuestoAdicional: float = 0.0
    __montoExento: float = 0.0
    __total: float = 0.0
    LineasDeta: List[int] = field(default_factory=list)
    @property
    def GlosaSTI(self) -> str:
        return self.__glosa

    @GlosaSTI.setter
    def GlosaSTI(self, value: str):
        self.__glosa = value[:40]

    @property
    def SubTotNetoSTI(self) -> float:
        return round(self.__neto, 2)

    @SubTotNetoSTI.setter
    def SubTotNetoSTI(self, value: float):
        self.__neto = value

    @property
    def SubTotIVASTI(self) -> float:
        return round(self.__iva, 2)

    @SubTotIVASTI.setter
    def SubTotIVASTI(self, value: float):
        self.__iva = value

    @property
    def SubTotAdicSTI(self) -> float:
        return round(self.__impuestoAdicional, 2)

    @SubTotAdicSTI.setter
    def SubTotAdicSTI(self, value: float):
        self.__impuestoAdicional = value

    @property
    def SubTotExeSTI(self) -> float:
        return round(self.__montoExento, 2)

    @SubTotExeSTI.setter
    def SubTotExeSTI(self, value: float):
        self.__montoExento = value

    @property
    def ValSubtotSTI(self) -> float:
        return round(self.__total, 2)

    @ValSubtotSTI.setter
    def ValSubtotSTI(self, value: float):
        self.__total = value

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

    def to_dict(self):

        return {
            "NroSTI": self.NroSTI,
            "GlosaSTI": self.GlosaSTI,
            "OrdenSTI": self.OrdenSTI,
            "SubTotNetoSTI": self.SubTotNetoSTI,
            "SubTotIVASTI": self.SubTotIVASTI,
            "SubTotAdicSTI": self.SubTotAdicSTI,
            "SubTotExeSTI": self.SubTotExeSTI,
            "ValSubtotSTI": self.ValSubtotSTI,
            "LineasDeta": self.LineasDeta
        }