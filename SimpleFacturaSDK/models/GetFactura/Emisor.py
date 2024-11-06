from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Emisor:
    RUTEmisor: str = ''
    _razonSocial: Optional[str] = ''
    _razonSocialBoleta: Optional[str] = ''
    _giro: Optional[str] = ''
    _giroEmisor: Optional[str] = ''
    _telefono: List[str] = field(default_factory=list)
    CorreoEmisor: Optional[str] = ''
    Acteco: List[int] = field(default_factory=list)
    GuiaExport: Optional[str] = None
    _sucursal: str = ''
    CdgSIISucur: int = 0
    _dirOrigen: str = ''
    CmnaOrigen: str = ''
    CiudadOrigen: str = ''
    _codigoVendedor: str = ''
    _idAdicionalEmisor: str = ''

    @property
    def RznSoc(self) -> Optional[str]:
        return self._razonSocial

    @RznSoc.setter
    def RznSoc(self, value: Optional[str]):
        self._razonSocial = value[:70] if value else ''

    @property
    def RznSocEmisor(self) -> Optional[str]:
        return self._razonSocialBoleta

    @RznSocEmisor.setter
    def RznSocEmisor(self, value: Optional[str]):
        self._razonSocialBoleta = value[:100] if value else ''

    @property
    def GiroEmis(self) -> Optional[str]:
        return self._giro

    @GiroEmis.setter
    def GiroEmis(self, value: Optional[str]):
        self._giro = value[:80] if value else ''

    @property
    def GiroEmisor(self) -> Optional[str]:
        return self._giroEmisor

    @GiroEmisor.setter
    def GiroEmisor(self, value: Optional[str]):
        self._giroEmisor = value[:80] if value else ''

    @property
    def Telefono(self) -> List[str]:
        return self._telefono

    @Telefono.setter
    def Telefono(self, value: List[str]):
        self._telefono = [x[:20] for x in value]

    @property
    def Sucursal(self) -> str:
        return self._sucursal

    @Sucursal.setter
    def Sucursal(self, value: str):
        self._sucursal = value[:20]

    @property
    def DirOrigen(self) -> str:
        return self._dirOrigen

    @DirOrigen.setter
    def DirOrigen(self, value: str):
        self._dirOrigen = value[:70]

    @property
    def CdgVendedor(self) -> str:
        return self._codigoVendedor

    @CdgVendedor.setter
    def CdgVendedor(self, value: str):
        self._codigoVendedor = value[:60]

    @property
    def IdAdicEmisor(self) -> str:
        return self._idAdicionalEmisor

    @IdAdicEmisor.setter
    def IdAdicEmisor(self, value: str):
        self._idAdicionalEmisor = value[:20]

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