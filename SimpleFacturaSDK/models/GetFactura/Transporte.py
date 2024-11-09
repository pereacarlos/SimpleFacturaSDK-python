from dataclasses import dataclass, field
from typing import Optional

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

    

@dataclass
class Transporte:
    Patente: Optional[str] = None
    RUTTrans: Optional[str] = None
    Chofer: Optional[Chofer] = None
    DirDest: Optional[str] = None
    CmnaDest: Optional[str] = None
    CiudadDest: Optional[str] = None
    Aduana: Optional[Aduana] = None

    __patente: Optional[str] = field(default=None, init=False, metadata={"max_length": 8})
    __dirDestino: Optional[str] = field(default=None, init=False, metadata={"max_length": 70})

    def __post_init__(self):
        self.__patente = truncate(self.Patente, 8)
        self.__dirDestino = truncate(self.DirDest, 70)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Patente=data.get('Patente'),
            RUTTrans=data.get('RUTTrans'),
            Chofer=Chofer.from_dict(data.get('Chofer')),
            DirDest=data.get('DirDest'),
            CmnaDest=data.get('CmnaDest'),
            CiudadDest=data.get('CiudadDest'),
            Aduana=Aduana.from_dict(data.get('Aduana'))
        )