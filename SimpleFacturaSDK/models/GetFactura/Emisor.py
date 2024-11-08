from dataclasses import dataclass, field
from typing import List, Optional
from SimpleFacturaSDK.models.GetFactura.GuiaExportacion import GuiaExportacion

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Emisor:
    RUTEmisor: str
    RznSoc: str
    RznSocEmisor: Optional[str] = None
    GiroEmis: Optional[str] = None
    GiroEmisor: Optional[str] = None
    Telefono: List[str] = field(default_factory=list)
    CorreoEmisor: Optional[str] = None
    Acteco: List[int] = field(default_factory=list)
    GuiaExport: Optional['GuiaExportacion'] = None
    Sucursal: str = ""
    CdgSIISucur: int = 0
    DirOrigen: str = ""
    CmnaOrigen: str = ""
    CiudadOrigen: str = ""
    CdgVendedor: str = ""
    IdAdicEmisor: str = ""

    # Privado
    _razonSocial: Optional[str] = None
    _razonSocialBoleta: Optional[str] = None
    _giro: Optional[str] = None
    _giroEmisor: Optional[str] = None
    _telefono: List[str] = field(default_factory=list)
    _codigoVendedor: str = ""
    _idAdicionalEmisor: str = ""

    def __post_init__(self):
        self._razonSocial = self.RznSoc
        self._razonSocialBoleta = self.RznSocEmisor
        self._giro = self.GiroEmis
        self._giroEmisor = self.GiroEmisor
        self._telefono = self.Telefono
        self._codigoVendedor = self.CdgVendedor
        self._idAdicionalEmisor = self.IdAdicEmisor
