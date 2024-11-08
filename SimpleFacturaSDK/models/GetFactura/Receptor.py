from dataclasses import dataclass, field
from typing import List, Optional
from SimpleFacturaSDK.models.GetFactura.Extranjero import Extranjero

def truncate(value: Optional[str], length: int) -> Optional[str]:
    return value[:length] if value else value

@dataclass
class Receptor:
    """
    Clase que representa al receptor del DTE (Documento Tributario Electrónico).
    """
    # Público
    RUTRecep: str
    RznSocRecep: str
    Extranjero: Optional[Extranjero] = None
    CorreoRecep: Optional[str] = None
    CiudadRecep: str = ''
    CmnaPostal: str = ''
    CiudadPostal: str = ''
    CdgIntRecep: str = ''
    GiroRecep: str = ''
    Contacto: Optional[str] = None
    DirRecep: Optional[str] = None
    CmnaRecep: str = ''
    DirPostal: str = ''

    # Privado
    __codigoInterno: str = ''
    __giro: str = ''
    __contacto: Optional[str] = None
    __direccion: Optional[str] = None
    __comuna: str = ''
    __dirPostal: str = ''

    def __post_init__(self):
        self.__codigoInterno = truncate(self.CdgIntRecep, 20)
        self.__giro = truncate(self.GiroRecep, 40)
        self.__contacto = truncate(self.Contacto, 80) if self.Contacto else None
        self.__direccion = truncate(self.DirRecep, 70) if self.DirRecep else None
        self.__comuna = truncate(self.CmnaRecep, 20)
        self.__dirPostal = truncate(self.DirPostal, 70)
        
    def to_dict(self):
        return {
            "RUTRecep": self.RUTRecep,
            "RznSocRecep": self.RznSocRecep,
            "Extranjero": self.Extranjero.to_dict() if self.Extranjero else None,
            "CorreoRecep": self.CorreoRecep,
            "CiudadRecep": self.CiudadRecep,
            "CmnaPostal": self.CmnaPostal,
            "CiudadPostal": self.CiudadPostal,
            "CdgIntRecep": self.__codigoInterno,
            "GiroRecep": self.__giro,
            "Contacto": self.__contacto,
            "DirRecep": self.__direccion,
            "CmnaRecep": self.__comuna,
            "DirPostal": self.__dirPostal
        }