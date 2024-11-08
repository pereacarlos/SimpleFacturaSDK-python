from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.enumeracion.TipoDespacho import TipoDespachoEnum
from SimpleFacturaSDK.enumeracion.TipoTraslado import TipoTrasladoEnum
from SimpleFacturaSDK.enumeracion.TipoImpresion import TipoImpresionEnum
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicioEnum
from SimpleFacturaSDK.enumeracion.FormaPago import FormaPagoEnum
from SimpleFacturaSDK.enumeracion.CodigosAduana import FormaPagoExportacionEnum
from SimpleFacturaSDK.enumeracion.MedioPago import MedioPagoEnum
from SimpleFacturaSDK.enumeracion.TipoCuentaPago import TipoCuentaPagoEnum
from SimpleFacturaSDK.models.GetFactura.MontoPagoItem import MontoPagoItem
from SimpleFacturaSDK.enumeracion.TipoTransCompra import TipoTransCompra, TipoTransVenta
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''


@dataclass
class IdentificacionDTE:
    TipoDTE: Optional[DTEType] = None
    Folio: Optional[int] = None
    FechaEmisionString: Optional[str] = None
    IndNoRebaja: int = 0
    TipoDespacho: Optional[TipoDespachoEnum] = None
    IndTraslado: Optional[TipoTrasladoEnum] = None
    TpoImpresion: Optional[TipoImpresionEnum] = None
    IndServicio: Optional[IndicadorServicioEnum] = None
    MntBruto: int = 0
    FmaPago: Optional[FormaPagoEnum] = None
    FmaPagExp: Optional[FormaPagoExportacionEnum] = None
    FechaCancelacionString: Optional[str] = None
    MntCancel: int = 0
    SaldoInsol: int = 0
    MntPagos: List[MontoPagoItem] = field(default_factory=list)
    PeriodoDesdeString: Optional[str] = None
    PeriodoHastaString: Optional[str] = None
    MedioPago: Optional[MedioPagoEnum] = None
    TpoCtaPago: Optional[TipoCuentaPagoEnum] = None
    TermPagoDias: int = 0
    FechaVencimientoString: Optional[str] = None
    IndMntNeto: Optional[int] = None

    # Private fields for internal use
    _cuentaPago: Optional[str] = field(init=False, default=None)
    _bancoPago: Optional[str] = field(init=False, default=None)
    _terminoPagoCodigo: Optional[str] = field(init=False, default=None)
    _terminoPagoGlosa: Optional[str] = field(init=False, default=None)

    # Date properties with parsing logic
    @property
    def FchEmis(self) -> Optional[datetime]:
        if self.FechaEmisionString:
            return datetime.strptime(self.FechaEmisionString, '%Y-%m-%d')
        return None

    @FchEmis.setter
    def FchEmis(self, value: datetime):
        self.FechaEmisionString = value.strftime('%Y-%m-%d') if value else None

    @property
    def FchCancel(self) -> Optional[datetime]:
        if self.FechaCancelacionString:
            return datetime.strptime(self.FechaCancelacionString, '%Y-%m-%d')
        return None

    @FchCancel.setter
    def FchCancel(self, value: datetime):
        self.FechaCancelacionString = value.strftime('%Y-%m-%d') if value else None

    @property
    def PeriodoDesde(self) -> Optional[datetime]:
        if self.PeriodoDesdeString:
            return datetime.strptime(self.PeriodoDesdeString, '%Y-%m-%d')
        return None

    @PeriodoDesde.setter
    def PeriodoDesde(self, value: datetime):
        self.PeriodoDesdeString = value.strftime('%Y-%m-%d') if value else None

    @property
    def PeriodoHasta(self) -> Optional[datetime]:
        if self.PeriodoHastaString:
            return datetime.strptime(self.PeriodoHastaString, '%Y-%m-%d')
        return None

    @PeriodoHasta.setter
    def PeriodoHasta(self, value: datetime):
        self.PeriodoHastaString = value.strftime('%Y-%m-%d') if value else None

    @property
    def FchVenc(self) -> Optional[datetime]:
        if self.FechaVencimientoString:
            return datetime.strptime(self.FechaVencimientoString, '%Y-%m-%d')
        return None

    @FchVenc.setter
    def FchVenc(self, value: datetime):
        self.FechaVencimientoString = value.strftime('%Y-%m-%d') if value else None

    # Properties with truncation logic
    @property
    def NumCtaPago(self) -> str:
        return truncate(self._cuentaPago, 20) if self._cuentaPago else ''

    @NumCtaPago.setter
    def NumCtaPago(self, value: str):
        self._cuentaPago = value

    @property
    def BcoPago(self) -> str:
        return truncate(self._bancoPago, 40) if self._bancoPago else ''

    @BcoPago.setter
    def BcoPago(self, value: str):
        self._bancoPago = value

    @property
    def TermPagoCdg(self) -> str:
        return truncate(self._terminoPagoCodigo, 4) if self._terminoPagoCodigo else ''

    @TermPagoCdg.setter
    def TermPagoCdg(self, value: str):
        self._terminoPagoCodigo = value

    @property
    def TermPagoGlosa(self) -> str:
        return truncate(self._terminoPagoGlosa, 100) if self._terminoPagoGlosa else ''

    @TermPagoGlosa.setter
    def TermPagoGlosa(self, value: str):
        self._terminoPagoGlosa = value

    def _post_init_(self):
        # Initialize default values if not set
        if self.TpoImpresion is None:
            self.TpoImpresion = TipoImpresionEnum()
        if self.FmaPagExp is None:
            self.FmaPagExp = FormaPagoExportacionEnum()
        if self.MedioPago is None:
            self.MedioPago = MedioPagoEnum()
        if self.TpoCtaPago is None:
            self.TpoCtaPago = TipoCuentaPagoEnum()
    def __init__(self, TipoDTE: Optional[DTEType] = None, Folio: Optional[int] = None, FechaEmisionString: Optional[str] = None, IndNoRebaja: int = 0, TipoDespacho: Optional[TipoDespachoEnum] = None, IndTraslado: Optional[TipoTrasladoEnum] = None, TpoImpresion: Optional[TipoImpresionEnum] = None, IndServicio: Optional[IndicadorServicioEnum] = None, MntBruto: int = 0, FmaPago: Optional[FormaPagoEnum] = None, FmaPagExp: Optional[FormaPagoExportacionEnum] = None, FechaCancelacionString: Optional[str] = None, MntCancel: int = 0, SaldoInsol: int = 0, MntPagos: List[MontoPagoItem] = field(default_factory=list), PeriodoDesdeString: Optional[str] = None, PeriodoHastaString: Optional[str] = None, MedioPago: Optional[MedioPagoEnum] = None, TpoCtaPago: Optional[TipoCuentaPagoEnum] = None, TermPagoDias: int = 0, FechaVencimientoString: Optional[str] = None, IndMntNeto: Optional[int] = None):
        self.TipoDTE = TipoDTE
        self.Folio = Folio
        self.FechaEmisionString = FechaEmisionString
        self.IndNoRebaja = IndNoRebaja
        self.TipoDespacho = TipoDespacho
        self.IndTraslado = IndTraslado
        self.TpoImpresion = TpoImpresion
        self.IndServicio = IndServicio
        self.MntBruto = MntBruto
        self.FmaPago = FmaPago
        self.FmaPagExp = FmaPagExp
        self.FechaCancelacionString = FechaCancelacionString
        self.MntCancel = MntCancel
        self.SaldoInsol = SaldoInsol
        self.MntPagos = MntPagos
        self.PeriodoDesdeString = PeriodoDesdeString
        self.PeriodoHastaString = PeriodoHastaString
        self.MedioPago = MedioPago
        self.TpoCtaPago = TpoCtaPago
        self.TermPagoDias = TermPagoDias
        self.FechaVencimientoString = FechaVencimientoString
        self.IndMntNeto = IndMntNeto
        self._cuentaPago = None
        self._bancoPago = None
        self._terminoPagoCodigo = None
        self._terminoPagoGlosa = None
    
    def to_dict(self):
        return {
            "TipoDTE": self.TipoDTE,
            "Folio": self.Folio,
            "FechaEmisionString": self.FechaEmisionString,
            "IndNoRebaja": self.IndNoRebaja,
            "TipoDespacho": self.TipoDespacho,
            "IndTraslado": self.IndTraslado,
            "TpoImpresion": self.TpoImpresion,
            "IndServicio": self.IndServicio,
            "MntBruto": self.MntBruto,
            "FmaPago": self.FmaPago,
            "FmaPagExp": self.FmaPagExp,
            "FechaCancelacionString": self.FechaCancelacionString,
            "MntCancel": self.MntCancel,
            "SaldoInsol": self.SaldoInsol,
            "MntPagos": [x.to_dict() for x in self.MntPagos],
            "PeriodoDesdeString": self.PeriodoDesdeString,
            "PeriodoHastaString": self.PeriodoHastaString,
            "MedioPago": self.MedioPago,
            "TpoCtaPago": self.TpoCtaPago,
            "TermPagoDias": self.TermPagoDias,
            "FechaVencimientoString": self.FechaVencimientoString,
            "IndMntNeto": self.IndMntNeto
        }