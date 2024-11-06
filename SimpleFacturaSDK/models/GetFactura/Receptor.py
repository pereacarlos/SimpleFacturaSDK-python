from dataclasses import dataclass, field
from typing import List, Optional

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Receptor:
    RUTRecep: str = ''
    __cdgIntRecep: str = ''
    razonSocial: str = ''
    Extranjero: Optional[str] = ''
    __giroRecep: str = ''
    __contacto: Optional[str] = ''
    CorreoRecep: Optional[str] = ''
    DirRecep: Optional[str] = field(default='', init=False)
    __ComunaRecep: str = ''
    CiudadRecep: str = ''
    DirPostal: str = ''
    CmnaPostal: str = ''
    CiudadPostal: str = ''
    



    @property
    def CodigoIntRecep(self) -> Optional[str]:
        return self.__cdgIntRecep

    @CodigoIntRecep.setter
    def CodigoIntRecep(self, value: Optional[str]):
        self.__cdgIntRecep =  truncate(value, 20)

    
    @property
    def GiroRecep(self) -> Optional[str]:
        return self.__giroRecep

    @GiroRecep.setter
    def GiroRecep(self, value: Optional[str]):
        self.__giroRecep =  truncate(value, 40)


    @property
    def Contacto(self) -> Optional[str]:
        return self.__contacto

    @Contacto.setter
    def Contacto(self, value: Optional[str]):
        self.__contacto =  truncate(value, 80)

    @property
    def DirRecep(self) -> str:
        return self._direccion

    @DirRecep.setter
    def DirRecep(self, value: str):
        self._direccion = truncate(value, 70)

    @property
    def ComunaRecep(self) -> str:
        return self.__ComunaRecep

    @ComunaRecep.setter
    def ComunaRecep(self, value: str):
        self.__ComunaRecep = truncate(value, 20)

    @property
    def DirPostal(self) -> str:
        return self._dir_postal

    @DirPostal.setter
    def DirPostal(self, value: str):
        self._dir_postal = truncate(value, 70)

   

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