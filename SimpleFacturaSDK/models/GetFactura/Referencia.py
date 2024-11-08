from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from SimpleFacturaSDK.enumeracion.TipoReferencia import TipoReferenciaEnum

@dataclass
class Referencia:
    NroLinRef: int = 0
    TpoDocRef: str = ''
    IndGlobal: int = 0
    FolioRef: str = ''
    RUTOtr: str = ''
    FechaDocumentoReferenciaString: str = ''
    
    CodRef: TipoReferenciaEnum = TipoReferenciaEnum.NotSet
    _razonReferencia: str = ''
    @property
    def FchRef(self) -> datetime:
        return datetime.strptime(self.FechaDocumentoReferenciaString, "%Y-%m-%d")

    @FchRef.setter
    def FchRef(self, value: datetime):
        self.FechaDocumentoReferenciaString = value.strftime("%Y-%m-%d")


    @property
    def RazonRef(self) -> str:
        return self._razonReferencia

    @RazonRef.setter
    def RazonRef(self, value: str):
        self._razonReferencia = value[:90]

    def __init__(self):
        self.NroLinRef = 0
        self.TpoDocRef = ''
        self.FolioRef = ''
        self.FchRef = datetime.min
        self.IndGlobal = 0
        self.RUTOtr = ''
        self.CodRef = TipoReferenciaEnum.NotSet
        self.RazonRef = ''