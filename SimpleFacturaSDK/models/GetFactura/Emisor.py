from dataclasses import dataclass, field
from typing import List, Optional

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Emisor:
    RUTEmisor: str = ''
    Acteco: List[int] = field(default_factory=list)
    Telefono: List[str] = field(default_factory=list)
    CorreoEmisor: Optional[str] = None
    GuiaExport: Optional[GuiaExportacion] = None
    CdgSIISucur: int = 0
    CmnaOrigen: str = ''
    CiudadOrigen: str = ''

    _razonSocial: Optional[str] = field(default=None, init=False)
    _razonSocialBoleta: Optional[str] = field(default=None, init=False)
    _giro: Optional[str] = field(default=None, init=False)
    _giroEmisor: Optional[str] = field(default=None, init=False)
    _sucursal: Optional[str] = field(default=None, init=False)
    _dirOrigen: Optional[str] = field(default=None, init=False)
    _codigoVendedor: Optional[str] = field(default=None, init=False)
    _idAdicionalEmisor: Optional[str] = field(default=None, init=False)

    @property
    def RznSoc(self) -> Optional[str]:
        return self._razonSocial

    @RznSoc.setter
    def RznSoc(self, value: Optional[str]):
        self._razonSocial = truncate(value, 70)

    @property
    def RznSocEmisor(self) -> Optional[str]:
        return self._razonSocialBoleta

    @RznSocEmisor.setter
    def RznSocEmisor(self, value: Optional[str]):
        self._razonSocialBoleta = truncate(value, 100)

    @property
    def GiroEmis(self) -> Optional[str]:
        return self._giro

    @GiroEmis.setter
    def GiroEmis(self, value: Optional[str]):
        self._giro = truncate(value, 80)

    @property
    def GiroEmisor(self) -> Optional[str]:
        return self._giroEmisor

    @GiroEmisor.setter
    def GiroEmisor(self, value: Optional[str]):
        self._giroEmisor = truncate(value, 80)

    @property
    def Sucursal(self) -> Optional[str]:
        return self._sucursal

    @Sucursal.setter
    def Sucursal(self, value: Optional[str]):
        self._sucursal = truncate(value, 20)

    @property
    def DirOrigen(self) -> Optional[str]:
        return self._dirOrigen

    @DirOrigen.setter
    def DirOrigen(self, value: Optional[str]):
        self._dirOrigen = truncate(value, 70)

    @property
    def CdgVendedor(self) -> Optional[str]:
        return self._codigoVendedor

    @CdgVendedor.setter
    def CdgVendedor(self, value: Optional[str]):
        self._codigoVendedor = truncate(value, 60)

    @property
    def IdAdicEmisor(self) -> Optional[str]:
        return self._idAdicionalEmisor

    @IdAdicEmisor.setter
    def IdAdicEmisor(self, value: Optional[str]):
        self._idAdicionalEmisor = truncate(value, 20)

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