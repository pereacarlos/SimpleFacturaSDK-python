from dataclasses import dataclass, field
from typing import List, Optional
from Extranjero import Extranjero

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Receptor:
    RUTRecep: str = ''
    RznSocRecep: str = ''
    Extranjero: Optional[Extranjero] = None
    CorreoRecep: Optional[str] = None
    CiudadRecep: str = ''
    CmnaPostal: str = ''
    CiudadPostal: str = ''

    __codigoInterno: str = field(default="", init=False)
    __giro: str = field(default="", init=False)
    __contacto: str = field(default="", init=False)
    __direccion: str = field(default="", init=False)
    __comuna: str = field(default="", init=False)
    __dirPostal: str = field(default="", init=False)

    @property
    def CdgIntRecep(self) -> str:
        return self.__codigoInterno

    @CdgIntRecep.setter
    def CdgIntRecep(self, value: str):
        self.__codigoInterno = truncate(value, 20)

    @property
    def GiroRecep(self) -> str:
        return self.__giro

    @GiroRecep.setter
    def GiroRecep(self, value: str):
        self.__giro = truncate(value, 40)

    @property
    def Contacto(self) -> Optional[str]:
        return self.__contacto

    @Contacto.setter
    def Contacto(self, value: Optional[str]):
        self.__contacto = truncate(value, 80) if value else None

    @property
    def DirRecep(self) -> Optional[str]:
        return self.__direccion

    @DirRecep.setter
    def DirRecep(self, value: Optional[str]):
        self.__direccion = truncate(value, 70) if value else None

    @property
    def CmnaRecep(self) -> str:
        return self.__comuna

    @CmnaRecep.setter
    def CmnaRecep(self, value: str):
        self.__comuna = truncate(value, 20)

    @property
    def DirPostal(self) -> str:
        return self.__dirPostal

    @DirPostal.setter
    def DirPostal(self, value: str):
        self.__dirPostal = truncate(value, 70)

    def __init__(self):
        self.RUTRecep = ''
        self.RznSocRecep = ''
        self.CdgIntRecep = ''
        self.Extranjero = null
        self.GiroRecep = ''
        self.Contacto = ''
        self.CorreoRecep = ''
        self.DirRecep = ''
        self.CmnaRecep = ''
        self.CiudadRecep = ''
        self.DirPostal = ''
        self.CmnaPostal = ''
        self.CiudadPostal = ''