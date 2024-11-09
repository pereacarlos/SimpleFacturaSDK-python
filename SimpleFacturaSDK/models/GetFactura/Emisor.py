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
    __razonSocial: Optional[str] = field(default=None, metadata={"max_length": 70})
    __razonSocialBoleta: Optional[str] = field(default=None, metadata={"max_length": 100})
    __giro: Optional[str] = field(default=None, metadata={"max_length": 80})
    __giroEmisor: Optional[str] = field(default=None, metadata={"max_length": 80})
    __telefono: List[str] = field(default_factory=list)
    __sucursal: str = field(default="", metadata={"max_length": 20})
    __dirOrigen: str = field(default="", metadata={"max_length": 70})
    __codigoVendedor: str = field(default="", metadata={"max_length": 60})
    __idAdicionalEmisor: str = field(default="", metadata={"max_length": 20})

    def __post_init__(self):
        self.__razonSocial = truncate(self.RznSoc, 70)
        self.__razonSocialBoleta = truncate(self.RznSocEmisor, 100)
        self.__giro = truncate(self.GiroEmis, 80)
        self.__giroEmisor = truncate(self.GiroEmisor, 80)
        self.__telefono = self.Telefono
        self.__sucursal = truncate(self.Sucursal, 20)
        self.__dirOrigen = truncate(self.DirOrigen, 70)
        self.__codigoVendedor = truncate(self.CdgVendedor, 60)
        self.__idAdicionalEmisor = truncate(self.IdAdicEmisor, 20)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            RUTEmisor=data.get('RUTEmisor'),
            RznSoc=data.get('RznSoc'),
            RznSocEmisor=data.get('RznSocEmisor'),
            GiroEmis=data.get('GiroEmis'),
            GiroEmisor=data.get('GiroEmisor'),
            Telefono=data.get('Telefono'),
            CorreoEmisor=data.get('CorreoEmisor'),
            Acteco=data.get('Acteco'),
            GuiaExport=GuiaExportacion.from_dict(data.get('GuiaExport')),
            Sucursal=data.get('Sucursal'),
            CdgSIISucur=data.get('CdgSIISucur'),
            DirOrigen=data.get('DirOrigen'),
            CmnaOrigen=data.get('CmnaOrigen'),
            CiudadOrigen=data.get('CiudadOrigen'),
            CdgVendedor=data.get('CdgVendedor'),
            IdAdicEmisor=data.get('IdAdicEmisor')
        )
