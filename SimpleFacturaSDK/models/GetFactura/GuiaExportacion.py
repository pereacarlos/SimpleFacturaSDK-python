from dataclasses import dataclass, field
from datetime import datetime
from SimpleFacturaSDK.enumeracion.CodigoTraslado import CodigoTrasladoEnum

@dataclass
class GuiaExportacion:
    CdgTraslado:CodigoTrasladoEnum.NotSet
    FolioAut: int 
    FechaAutorizacionString: str

    @property
    def FchAut(self) -> datetime:
        return datetime.strptime(self.FechaAutorizacionString, "%Y-%m-%d")

    @FchAut.setter
    def FchAut(self, value: datetime):
        self.FechaAutorizacionString = value.strftime("%Y-%m-%d")

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            CdgTraslado=CodigoTrasladoEnum(data.get('CdgTraslado')),
            FolioAut=data.get('FolioAut'),
            FechaAutorizacionString=data.get('FchAut')
        )


    def __init__(self):
        self.CdgTraslado = CodigoTrasladoEnum.NotSet
        self.FolioAut = 0
        self.FechaAutorizacionString = ''
