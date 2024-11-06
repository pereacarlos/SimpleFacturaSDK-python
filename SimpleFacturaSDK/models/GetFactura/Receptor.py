from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Receptor:
    RUTRecep: str = ''
    __cdgIntRecep: str = ''
    razonSocial: str = ''
    Extranjero: Optional[str] = ''
    __giroRecep: str = ''
    __contacto: Optional[str] = ''
    CorreoRecep: Optional[str] = ''
    



    @property
    def CodigoIntRecep(self) -> Optional[str]:
        return self.__cdgIntRecep

    @CodigoIntRecep.setter
    def CodigoIntRecep(self, value: Optional[str]):
        self.__cdgIntRecep = value[:20] if value else ''

    
    @property
    def GiroRecep(self) -> Optional[str]:
        return self.__giroRecep

    @GiroRecep.setter
    def GiroRecep(self, value: Optional[str]):
        self.__giroRecep = value[:40] if value else ''


    @property
    def GiroRecep(self) -> Optional[str]:
        return self.__contacto

    @GiroRecep.setter
    def GiroRecep(self, value: Optional[str]):
        self.__contacto = value[:80] if value else ''

   

    def __init__(self):
        self.RUTRecep = ''
        self.RznSocRecep = ''
        self.CodigoIntRecep = ''
        self.Extranjero = ''
        self.GiroRecep = ''
        self.Contacto = ''
        self.CorreoRecep = ''