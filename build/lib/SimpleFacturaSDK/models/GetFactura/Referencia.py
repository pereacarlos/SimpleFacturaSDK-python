from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from enumeracion.TipoReferencia import TipoReferenciaEnum

@dataclass
class Referencia:
    NroLinRef: int 
    TpoDocRef: str 
    FolioRef: str
    CodRef: TipoReferenciaEnum
    RazonRef: str 
    FchRef: datetime
    IndGlobal: Optional[int] = None
    FechaDocumentoReferenciaString: Optional[str] = None
    RUTOtr: Optional[str] = None

