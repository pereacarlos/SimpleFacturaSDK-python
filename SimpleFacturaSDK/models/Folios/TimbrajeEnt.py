from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID
from datetime import datetime
from Utilidades.Utilidades import Utilidades
@dataclass
class TimbrajeEnt:
    TimbrajeId: UUID
    TipoDteId: UUID
    SucursalId: UUID
    codigoSii: int
    fechaIngreso: datetime
    EmisorId: UUID
    UsuarioId: UUID
    fechaVencimiento: datetime

    # Campos opcionales o con valores predeterminados
    desde: int = 0
    hasta: int = 0
    Activo: bool = False
    Xml: bytes = field(default_factory=bytes)
    NombreSucursal: str = ""
    tipoDte: str = ""
    foliosDisponibles: int = 0
    FoliosSinUsar: int = 0
    UltimoFolioEmitido: int = 0
    RutEmisor: str = ""
    ambiente: int = 0
    BorrarFolioBloqueado: bool = False
    Sincronizado: bool = False
    fechaCaf: Optional[datetime] = None
    FechaUltimaSincronizacion: Optional[datetime] = None

@dataclass
class TimbrajeApiEnt:
    codigoSii: int = 0
    desde: int = 0
    hasta: int = 0
    tipoDte: str = ""
    foliosDisponibles: int = 0
    ambiente: int = 0
    fechaCaf: Optional[datetime] = None
    fechaVencimiento: Optional[datetime] = None
    fechaIngreso: Optional[datetime] = None

    # Constructor alternativo para inicializar a partir de TimbrajeEnt
    @classmethod
    def from_timbraje_ent(cls, ent: Optional[TimbrajeEnt]) -> "TimbrajeApiEnt":
        if ent:
            return cls(
                codigoSii=ent.codigoSii,
                fechaIngreso=ent.fechaIngreso,
                fechaCaf=ent.fechaCaf,
                desde=ent.desde,
                hasta=ent.hasta,
                fechaVencimiento=ent.fechaVencimiento,
                tipoDte= Utilidades.ObtenerNombreTipoDTE(ent.codigoSii),
                foliosDisponibles=ent.foliosDisponibles,
                ambiente=ent.ambiente
            )
        else:
            codigoSii: int = 0
            tipoDte: str = ""
