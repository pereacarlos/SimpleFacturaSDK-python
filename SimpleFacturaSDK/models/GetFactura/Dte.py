from dataclasses import dataclass
from typing import List

@dataclass
class Dte:
    ambiente: str
    folioReutilizado: str
    folio: int
    importado: str
    codigoSii: int
    estadoAcuse: str
    estadoSii: str
    fechaDte: str 
    fechaCreacion: str 
    razonSocialReceptor: str
    rutReceptor: str
    trackId: int
    neto: float
    exento: float
    iva: float
    ivaTerceros: float
    ivaPropio: float
    totalImpuestosAdicionales: float
    total: float
    detalles: List[str] 
    referencias: List[str]  
