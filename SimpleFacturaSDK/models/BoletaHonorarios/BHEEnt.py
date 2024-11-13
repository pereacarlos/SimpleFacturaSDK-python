from dataclasses import dataclass
from typing import Optional

@dataclass
class EmisorEnt:
    rutEmisor: Optional[str] = None
    Direccion: Optional[str] = None
    RazonSocial: Optional[str] = None

@dataclass
class ReceptorEnt:
    Rut: Optional[str] = None
    Comuna: Optional[str] = None
    Nombre: Optional[str] = None
    Direccion: Optional[str] = None
    Region: Optional[str] = None

@dataclass
class TotalesEnt:
    TotalHonoraios: Optional[float] = None
    Bruto: Optional[float] = None
    Liquido: Optional[float] = None
    Pagado: Optional[float] = None
    Retenido: Optional[float] = None


@dataclass
class BHEEnt:
    Folio: Optional[int] = None
    FechaEmision: Optional[str] = None
    CodigoBarra: Optional[str] = None
    Emisor: Optional[EmisorEnt] = None
    Receptor: Optional[ReceptorEnt] = None
    Totales: Optional[TotalesEnt] = None
    Estado: Optional[str] = None
    DescriptionAnulacion: Optional[str] = None