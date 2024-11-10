from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from SimpleFacturaSDK.enumeracion.TipoReferencia import TipoReferenciaEnum

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Referencia:
    NroLinRef: int 
    TpoDocRef: str 
    IndGlobal: int 
    FolioRef: str
    RUTOtr: str 
    FechaDocumentoReferenciaString: str 
    FchRef = datetime
    CodRef: TipoReferenciaEnum.NotSet
    RazonRef: str 

    _razonReferencia: str

    def __post_init__(self):
        self.FchRef = datetime.strptime(self.FechaDocumentoReferenciaString, '%Y-%m-%d')
        self._razonReferencia = truncate(self.RazonRef, 90)
  
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            NroLinRef=data.get('NroLinRef'),
            TpoDocRef=data.get('TpoDocRef'),
            IndGlobal=data.get('IndGlobal'),
            FolioRef=data.get('FolioRef'),
            RUTOtr=data.get('RUTOtr'),
            FechaDocumentoReferenciaString=data.get('FchRef'),
            CodRef=TipoReferenciaEnum(data.get('CodRef')),
            RazonRef=data.get('RazonRef')
        )