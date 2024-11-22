from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from enumeracion.TipoDTE import DTEType
from enumeracion.CodigosAduana import FormaPagoExportacionEnum
from enumeracion.IndicadorServicio import IndicadorServicioEnum
from enumeracion.TipoImpresion import TipoImpresionEnum
from enumeracion.MedioPago import MedioPagoEnum
from enumeracion.TipoCuentaPago import TipoCuentaPagoEnum
from enumeracion.TipoDespacho import TipoDespachoEnum
from enumeracion.TipoTraslado import TipoTrasladoEnum
from models.GetFactura.MontoPagoItem import MontoPagoItem

@dataclass
class IdDoc:
    TipoDTE: DTEType
    FchEmis: str
    FchVenc: str
    Folio: int = None
    MntBruto: int = None
    MntCancel: int = None
    SaldoInsol: int = None
    TipoTraslado: TipoTrasladoEnum = None
    TpoImpresion: TipoImpresionEnum = None
    TipoDespacho: TipoDespachoEnum = None
    FmaPagExp: FormaPagoExportacionEnum = None
    IdNorebaja: int = None
    FmaPago: int = None
    IndServicio: IndicadorServicioEnum = None
    MntPagos: List[MontoPagoItem] = field(default_factory=list)  # Usar una lista vacía como valor predeterminado
    PeriodoDesde: datetime = None
    PeriodoHasta: datetime = None
    MedioPago: MedioPagoEnum = None
    TpoCtaPago: TipoCuentaPagoEnum = None
    NumCtaPago: str = None
    BcoPago: str = None
    TermPagoCdg: str = None
    TermPagoGlosa: str = None
    TermPagoDias: int = None
    IndMntNeto: int = None
