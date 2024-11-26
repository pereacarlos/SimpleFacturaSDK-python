from dataclasses import dataclass, field
from datetime import datetime
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType


@dataclass
class ReferenciaDte:
    fecha: str 
    FchRef: datetime
    motivo: str
    razon: str
    glosa: str 
    folio: int 
    tipo_doc: DTEType