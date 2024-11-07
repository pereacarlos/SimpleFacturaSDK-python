from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from SimpleFacturaSDK.enum.CodigoTraslado import CodigoTrasladoEnum

class CodigoTrasladoEnum(Enum):
    NotSet = 0
    Exportador = 1
    AgenteDeAduana = 2
    Vendedor = 3
    ContribuyenteAutorizado = 4
    # Agregar otros códigos si es necesario

@dataclass
class GuiaExportacion:
    CdgTraslado: CodigoTrasladoEnum = CodigoTrasladoEnum.NotSet
    FolioAut: int = 0
    FechaAutorizacionString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))

    @property
    def FchAut(self) -> datetime:
        return datetime.strptime(self.FechaAutorizacionString, "%Y-%m-%d")

    @FchAut.setter
    def FchAut(self, value: datetime):
        self.FechaAutorizacionString = value.strftime("%Y-%m-%d")


    def __init__(self):
        self.CdgTraslado = CodigoTrasladoEnum.NOT_SET
        self.FolioAut = 0
        self.FechaAutorizacionString = ''
