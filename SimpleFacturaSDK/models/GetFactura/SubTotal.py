from dataclasses import dataclass, field
from typing import List

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class SubTotal:
    NroSTI: int = 0
    GlosaSTI: str = ''
    OrdenSTI: int = 0
    SubTotNetoSTI: float = 0.0
    SubTotIVASTI: float = 0.0
    SubTotAdicSTI: float = 0.0
    SubTotExeSTI: float = 0.0
    ValSubtotSTI: float = 0.0
    
    
    __glosa: str = field(default="", metadata={"max_length": 40})
    __neto: float = field(default=0.0, metadata={"decimals": 2})
    __iva: float = field(default=0.0, metadata={"decimals": 2})
    __impuestoAdicional: float = field(default=0.0, metadata={"decimals": 2})
    __montoExento: float = field(default=0.0, metadata={"decimals": 2})
    __total: float = field(default=0.0, metadata={"decimals": 2})
    LineasDeta: List[int] = field(default_factory=list)

    def __post_init__(self):
        self.__glosa = truncate(self.GlosaSTI, 40)
        self.__neto = round(self.SubTotNetoSTI, 2)
        self.__iva = round(self.SubTotIVASTI, 2)
        self.__impuestoAdicional = round(self.SubTotAdicSTI, 2)
        self.__montoExento = round(self.SubTotExeSTI, 2)
        self.__total = round(self.ValSubtotSTI, 2)
   

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            NroSTI=data.get('NroSTI'),
            GlosaSTI=data.get('GlosaSTI'),
            OrdenSTI=data.get('OrdenSTI'),
            SubTotNetoSTI=data.get('SubTotNetoSTI'),
            SubTotIVASTI=data.get('SubTotIVASTI'),
            SubTotAdicSTI=data.get('SubTotAdicSTI'),
            SubTotExeSTI=data.get('SubTotExeSTI'),
            ValSubtotSTI=data.get('ValSubtotSTI'),
            LineasDeta=data.get('LineasDeta')
        )