from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID
from datetime import datetime
from SimpleFacturaSDK.Utilidades.Utilidades import Utilidades

@dataclass
class TimbrajeEnt:
    TimbrajeId: UUID
    TipoDteId: UUID
    SucursalId: UUID
    CodigoSii: int
    FechaIngreso: datetime
    FechaCaf: Optional[datetime] = None
    Desde: int = 0
    Hasta: int = 0
    Activo: bool = False
    EmisorId: UUID
    UsuarioId: UUID
    FechaVencimiento: datetime
    Xml: bytes = field(default_factory=bytes)
    NombreSucursal: str = ""
    TipoDte: str = ""
    FoliosDisponibless: int = 0
    FoliosSinUsar: int = 0
    UltimoFolioEmitido: int = 0
    RutEmisor: str = ""
    Ambiente: int = 0
    BorrarFolioBloqueado: bool = False
    Sincronizado: bool = False
    FechaUltimaSincronizacion: Optional[datetime] = None

@dataclass
class TimbrajeApiEnt:
    CodigoSii: int = 0
    FechaIngreso: Optional[datetime] = None
    FechaCaf: Optional[datetime] = None
    Desde: int = 0
    Hasta: int = 0
    FechaVencimiento: Optional[datetime] = None
    TipoDte: str = ""
    FoliosDisponibles: int = 0
    Ambiente: int = 0

    # Constructor alternativo para inicializar a partir de TimbrajeEnt
    @classmethod
    def from_timbraje_ent(cls, ent: Optional[TimbrajeEnt]) -> "TimbrajeApiEnt":
        if ent:
            return cls(
                CodigoSii=ent.CodigoSii,
                FechaIngreso=ent.FechaIngreso,
                FechaCaf=ent.FechaCaf,
                Desde=ent.Desde,
                Hasta=ent.Hasta,
                FechaVencimiento=ent.FechaVencimiento,
                TipoDte= Utilidades.ObtenerNombreTipoDTE(ent.CodigoSii),
                FoliosDisponibles=ent.FoliosDisponibles,
                Ambiente=ent.Ambiente
            )
        else:
            CodigoSii: int = 0
            TipoDte: str = ""
