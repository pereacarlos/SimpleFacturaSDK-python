from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from SimpleFacturaSDK.models.ActividadesEconomicaApiEnt import ActividadesEconomicaEnt

@dataclass
class EmisorAapiEnt:
    Rut: str
    RazonSocial: str
    Giro: str
    CorreoFact: str
    Comuna: str
    NroResol: int
    FechaResol: datetime
    Ambiente: int
    Telefono: float
    RutRepresentanteLegal: str
    ActividadesEconomicas: List[ActividadesEconomicaEnt]
    DirPart: Optional[str] = None
    DirFact: Optional[str] = None
    CorreoPart: Optional[str] = None
    Ciudad: Optional[str] = None
    UnidadSII: Optional[str] = None
