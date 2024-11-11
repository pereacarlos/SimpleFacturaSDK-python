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

