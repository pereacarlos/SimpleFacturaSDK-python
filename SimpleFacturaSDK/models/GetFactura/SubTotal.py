from dataclasses import dataclass, field
from typing import List

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class SubTotal:
    NroSTI: int 
    GlosaSTI: str 
    OrdenSTI: int 
    SubTotNetoSTI: float 
    SubTotIVASTI: float 
    SubTotAdicSTI: float 
    SubTotExeSTI: float 
    ValSubtotSTI: float 
    
    
    __glosa: str 
    __neto: float 
    __iva: float 
    __impuestoAdicional: float 
    __montoExento: float 
    __total: float
    LineasDeta: List[int] 

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

    def to_dict(self):
        return asdict(self)