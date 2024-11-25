from dataclasses import dataclass
from typing import Optional

@dataclass
class EmisorEnt:
    rutEmisor: Optional[str] = None
    direccion: Optional[str] = None
    razonSocial: Optional[str] = None

@dataclass
class ReceptorEnt:
    rut: Optional[str] = None
    comuna: Optional[str] = None
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    region: Optional[str] = None

@dataclass
class TotalesEnt:
    totalHonorarios: Optional[float] = None
    bruto: Optional[float] = None
    liquido: Optional[float] = None
    pagado: Optional[float] = None
    retenido: Optional[float] = None


@dataclass
class BHEEnt:
    folio: Optional[int] = None
    fechaEmision: Optional[str] = None
    codigoBarra: Optional[str] = None
    emisor: Optional[EmisorEnt] = None
    receptor: Optional[ReceptorEnt] = None
    totales: Optional[TotalesEnt] = None
    estado: Optional[str] = None
    descripcionAnulacion: Optional[str] = None