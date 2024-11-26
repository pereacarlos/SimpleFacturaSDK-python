from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.enumeracion.CodigosAduana import FormaPagoExportacionEnum
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicioEnum
from SimpleFacturaSDK.enumeracion.TipoImpresion import TipoImpresionEnum
from SimpleFacturaSDK.enumeracion.MedioPago import MedioPagoEnum
from SimpleFacturaSDK.enumeracion.TipoCuentaPago import TipoCuentaPagoEnum
from SimpleFacturaSDK.enumeracion.TipoDespacho import TipoDespachoEnum
from SimpleFacturaSDK.enumeracion.TipoTraslado import TipoTrasladoEnum
from SimpleFacturaSDK.models.GetFactura.MontoPagoItem import MontoPagoItem

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
