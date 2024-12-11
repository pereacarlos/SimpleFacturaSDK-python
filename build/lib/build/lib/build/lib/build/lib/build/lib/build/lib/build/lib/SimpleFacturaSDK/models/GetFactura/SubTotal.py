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
  