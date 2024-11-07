from dataclasses import dataclass, field
from datetime import datetime
from SimpleFacturaSDK.enum.CodigoTraslado import CodigoTrasladoEnum

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
        self.CdgTraslado = CodigoTrasladoEnum.NotSet
        self.FolioAut = 0
        self.FechaAutorizacionString = ''
