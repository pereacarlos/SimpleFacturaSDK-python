from dataclasses import dataclass, field
from typing import Optional

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

    

@dataclass
class Transporte:
    Patente: Optional[str] 
    RUTTrans: Optional[str] 
    Chofer: Optional[Chofer]
    DirDest: Optional[str] 
    CmnaDest: Optional[str] 
    CiudadDest: Optional[str] 
    Aduana: Optional[Aduana] 

    __patente: Optional[str] 
    __dirDestino: Optional[str]

    def __post_init__(self):
        self.__patente = truncate(self.Patente, 8)
        self.__dirDestino = truncate(self.DirDest, 70)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Patente=data.get('Patente'),
            RUTTrans=data.get('RUTTrans'),
            Chofer=Chofer,
            DirDest=data.get('DirDest'),
            CmnaDest=data.get('CmnaDest'),
            CiudadDest=data.get('CiudadDest'),
            Aduana=Aduana
        )