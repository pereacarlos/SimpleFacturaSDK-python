from dataclasses import dataclass, field
from typing import Optional

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

    

@dataclass
class Transporte:
    _patente: Optional[str] = field(default=None, init=False)
    RUTTrans: Optional[str] = None
    Chofer: Optional[Chofer] = None
    __dirDestino: Optional[str] = field(default=None, init=False)
    CmnaDest: Optional[str] = None
    CiudadDest: Optional[str] = None
    Aduana: Optional[Aduana] = None

    @property
    def Patente(self) -> Optional[str]:
        return self._patente

    @Patente.setter
    def Patente(self, value: Optional[str]):
        self._patente = truncate(value, 8)

    @property
    def DirDest(self) -> Optional[str]:
        return self.__dirDestino

    @DirDest.setter
    def DirDest(self, value: Optional[str]):
        self.__dirDestino = truncate(value, 70)