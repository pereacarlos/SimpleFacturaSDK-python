from dataclasses import dataclass, field
from typing import List, Optional

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Emisor:
    RUTEmisor: str = ''
    Acteco: List[int] = field(default_factory=list)
    CorreoEmisor: Optional[str] = None
    GuiaExport: Optional[GuiaExportacion] = None
    CdgSIISucur: int = 0
    CmnaOrigen: str = ''
    CiudadOrigen: str = ''

    __razonSocial: Optional[str] = field(default=None, init=False)
    __razonSocialBoleta: Optional[str] = field(default=None, init=False)
    __giro: Optional[str] = field(default=None, init=False)
    __giroEmisor: Optional[str] = field(default=None, init=False)
    __Telefono: List[str] = field(default_factory=list)
    __sucursal: Optional[str] = field(default=None, init=False)
    __dirOrigen: Optional[str] = field(default=None, init=False)
    __codigoVendedor: Optional[str] = field(default=None, init=False)
    __idAdicionalEmisor: Optional[str] = field(default=None, init=False)

    @property
    def RznSoc(self) -> Optional[str]:
        return self.__razonSocial

    @RznSoc.setter
    def RznSoc(self, value: Optional[str]):
        self.__razonSocial = truncate(value, 70)

    @property
    def RznSocEmisor(self) -> Optional[str]:
        return self.__razonSocialBoleta

    @RznSocEmisor.setter
    def RznSocEmisor(self, value: Optional[str]):
        self.__razonSocialBoleta = truncate(value, 100)

    @property
    def GiroEmis(self) -> Optional[str]:
        return self.__giro

    @GiroEmis.setter
    def GiroEmis(self, value: Optional[str]):
        self.__giro = truncate(value, 80)

    @property
    def GiroEmisor(self) -> Optional[str]:
        return self.__giroEmisor

    @GiroEmisor.setter
    def GiroEmisor(self, value: Optional[str]):
        self.__giroEmisor = truncate(value, 80)

    @property
    def Telefono(self) -> Optional[str]:
        return self.__Telefono

    @Telefono.setter
    def Telefono(self, value: Optional[str]):
        self.__Telefono = truncate(value, 20)

    @property
    def Sucursal(self) -> Optional[str]:
        return self.__sucursal

    @Sucursal.setter
    def Sucursal(self, value: Optional[str]):
        self.__sucursal = truncate(value, 20)

    @property
    def DirOrigen(self) -> Optional[str]:
        return self.__dirOrigen

    @DirOrigen.setter
    def DirOrigen(self, value: Optional[str]):
        self.__dirOrigen = truncate(value, 70)

    @property
    def CdgVendedor(self) -> Optional[str]:
        return self.__codigoVendedor

    @CdgVendedor.setter
    def CdgVendedor(self, value: Optional[str]):
        self.__codigoVendedor = truncate(value, 60)

    @property
    def IdAdicEmisor(self) -> Optional[str]:
        return self.__idAdicionalEmisor

    @IdAdicEmisor.setter
    def IdAdicEmisor(self, value: Optional[str]):
        self.__idAdicionalEmisor = truncate(value, 20)

    def __init__(self):
        self.RUTEmisor = ''
        self.RznSoc = ''
        self.GiroEmis = ''
        self.Acteco = []
        self.Telefono = []
        self.CorreoEmisor = ''
        self.GuiaExport = None
        self.Sucursal = ''
        self.CdgSIISucur = 0
        self.DirOrigen = ''
        self.CmnaOrigen = ''
        self.CiudadOrigen = ''
        self.CdgVendedor = ''
        self.IdAdicEmisor = ''