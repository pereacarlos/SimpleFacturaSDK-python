from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from SimpleFacturaSDK.enum.TipoDTE import DTEType
from SimpleFacturaSDK.enum.TipoDespacho import TipoDespachoEnum
from SimpleFacturaSDK.enum.TipoTraslado import TipoTrasladoEnum
from SimpleFacturaSDK.enum.TipoImpresion import TipoImpresionEnum
from SimpleFacturaSDK.enum.IndicadorServicio import IndicadorServicioEnum
from SimpleFacturaSDK.enum.FormaPago import FormaPagoEnum
from SimpleFacturaSDK.enum.CodigosAduana import FormaPagoExportacionEnum
from SimpleFacturaSDK.enum.MedioPago import MedioPagoEnum
from SimpleFacturaSDK.enum.TipoCuentaPago import TipoCuentaPagoEnum

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class IdentificacionDTE:
    TipoDTE: DTEType = DTEType.NotSet
    Folio: int = 0
    FechaEmisionString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    IndNoRebaja: int = 0
    TipoDespacho: TipoDespachoEnum = TipoDespachoEnum.NotSet
    IndTraslado: TipoTrasladoEnum = TipoTrasladoEnum.NotSet
    TpoImpresion: TipoImpresionEnum = TipoImpresionEnum.N
    IndServicio: IndicadorServicioEnum = IndicadorServicioEnum.NotSet
    MntBruto: int = 0
    FmaPago: FormaPagoEnum = FormaPagoEnum.NotSet
    FmaPagExp: FormaPagoExportacionEnum = FormaPagoExportacionEnum.NotSet
    FechaCancelacionString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    MntCancel: int = 0
    SaldoInsol: int = 0
    MntPagos: List[MontoPagoItem] = field(default_factory=list)
    PeriodoDesdeString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    PeriodoHastaString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    MedioPago: MedioPagoEnum = MedioPagoEnum.NotSet
    TpoCtaPago: TipoCuentaPagoEnum = TipoCuentaPagoEnum.NotSet
    TermPagoDias: int = 0
    FechaVencimientoString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    TipoTranCompra: Optional[TipoTransCompra] = None
    TipoTranVenta: Optional[TipoTransVenta] = None
    IndMntNeto: int = 0

    __cuentaPago: str = field(default="", init=False)
    __bancoPago: str = field(default="", init=False)
    __terminoPagoCodigo: str = field(default="", init=False)
    __terminoPagoGlosa: str = field(default="", init=False)

    @property
    def FchEmis(self) -> datetime:
        return datetime.strptime(self.FechaEmisionString, "%Y-%m-%d")

    @FchEmis.setter
    def FchEmis(self, value: datetime):
        self.FechaEmisionString = value.strftime("%Y-%m-%d")

    @property
    def FchCancel(self) -> datetime:
        return datetime.strptime(self.FechaCancelacionString, "%Y-%m-%d")

    @FchCancel.setter
    def FchCancel(self, value: datetime):
        self.FechaCancelacionString = value.strftime("%Y-%m-%d")

    @property
    def PeriodoDesde(self) -> datetime:
        return datetime.strptime(self.PeriodoDesdeString, "%Y-%m-%d")

    @PeriodoDesde.setter
    def PeriodoDesde(self, value: datetime):
        self.PeriodoDesdeString = value.strftime("%Y-%m-%d")

    @property
    def PeriodoHasta(self) -> datetime:
        return datetime.strptime(self.PeriodoHastaString, "%Y-%m-%d")

    @PeriodoHasta.setter
    def PeriodoHasta(self, value: datetime):
        self.PeriodoHastaString = value.strftime("%Y-%m-%d")

    @property
    def FchVenc(self) -> datetime:
        return datetime.strptime(self.FechaVencimientoString, "%Y-%m-%d")

    @FchVenc.setter
    def FchVenc(self, value: datetime):
        self.FechaVencimientoString = value.strftime("%Y-%m-%d")

    @property
    def NumCtaPago(self) -> str:
        return self.__cuentaPago

    @NumCtaPago.setter
    def NumCtaPago(self, value: str):
        self.__cuentaPago = truncate(value, 20)

    @property
    def BcoPago(self) -> str:
        return self.__bancoPago

    @BcoPago.setter
    def BcoPago(self, value: str):
        self.__bancoPago = truncate(value, 40)

    @property
    def TermPagoCdg(self) -> str:
        return self.__terminoPagoCodigo

    @TermPagoCdg.setter
    def TermPagoCdg(self, value: str):
        self.__terminoPagoCodigo = truncate(value, 4)

    @property
    def TermPagoGlosa(self) -> str:
        return self.__terminoPagoGlosa

    @TermPagoGlosa.setter
    def TermPagoGlosa(self, value: str):
        self.__terminoPagoGlosa = truncate(value, 100)

    def __init__(self):
        self.TipoDTE = DTEType.NotSet
        self.Folio = 0
        self.FechaEmisionString = ''
        self.IndNoRebaja = 0
        self.TipoDespacho = TipoDespachoEnum.NotSet
        self.IndTraslado = TipoTrasladoEnum.NotSet
        self.TpoImpresion = TipoImpresionEnum.N
        self.IndServicio = IndicadorServicioEnum.NotSet
        self.MntBruto = 0
        self.FmaPago = FormaPagoEnum.NotSet
        self.FmaPagExp = FormaPagoExportacionEnum.NotSet
        self.FechaCancelacionString = ''
        self.MntCancel = 0
        self.SaldoInsol = 0
        self.MntPagos = []
        self.PeriodoDesdeString = ''
        self.PeriodoHastaString = ''
        self.MedioPago = MedioPagoEnum.NotSet
        self.TpoCtaPago = TipoCuentaPagoEnum.NotSet
        self.NumCtaPago = ''
        self.BcoPago = ''
        self.TermPagoCdg = ''
        self.TermPagoGlosa = ''
        self.TermPagoDias = 0
        self.FechaVencimientoString = ''
        self.TipoTranCompra = None
        self.TipoTranVenta = None
        self.IndMntNeto = 0