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
    EmisorId: UUID
    UsuarioId: UUID
    FechaVencimiento: datetime

    # Campos opcionales o con valores predeterminados
    Desde: int = 0
    Hasta: int = 0
    Activo: bool = False
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
    FechaCaf: Optional[datetime] = None
    FechaUltimaSincronizacion: Optional[datetime] = None

@dataclass
class TimbrajeApiEnt:
    CodigoSii: int = 0
    Desde: int = 0
    Hasta: int = 0
    TipoDte: str = ""
    FoliosDisponibles: int = 0
    Ambiente: int = 0
    FechaCaf: Optional[datetime] = None
    FechaVencimiento: Optional[datetime] = None
    FechaIngreso: Optional[datetime] = None

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
