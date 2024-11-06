from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from enum import Enum

# Definir las enumeraciones correspondientes
class DTEType(Enum):
    NotSet = 0
    # Agregar otros tipos de DTE según sea necesario

class TipoDespachoEnum(Enum):
    NotSet = 0
    # Agregar otros tipos de despacho según sea necesario

class TipoTrasladoEnum(Enum):
    NotSet = 0
    # Agregar otros tipos de traslado según sea necesario

class TipoImpresionEnum(Enum):
    N = "N"
    # Agregar otros tipos de impresión según sea necesario

class IndicadorServicioEnum(Enum):
    NotSet = 0
    # Agregar otros indicadores de servicio según sea necesario

class FormaPagoEnum(Enum):
    NotSet = 0
    # Agregar otras formas de pago según sea necesario

class FormaPagoExportacionEnum(Enum):
    NotSet = 0
    # Agregar otras formas de pago para exportación según sea necesario

class MedioPagoEnum(Enum):
    NotSet = 0
    # Agregar otros medios de pago según sea necesario

class TipoCuentaPagoEnum(Enum):
    NotSet = 0
    # Agregar otros tipos de cuenta de pago según sea necesario

class TipoTransCompra(Enum):
    NotSet = 0
    # Agregar otros tipos de transacción de compra según sea necesario

class TipoTransVenta(Enum):
    NotSet = 0
    # Agregar otros tipos de transacción de venta según sea necesario


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

    _cuentaPago: str = field(default="", init=False)
    _bancoPago: str = field(default="", init=False)
    _terminoPagoCodigo: str = field(default="", init=False)
    _terminoPagoGlosa: str = field(default="", init=False)

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
        return self._cuentaPago

    @NumCtaPago.setter
    def NumCtaPago(self, value: str):
        self._cuentaPago = truncate(value, 20)

    @property
    def BcoPago(self) -> str:
        return self._bancoPago

    @BcoPago.setter
    def BcoPago(self, value: str):
        self._bancoPago = truncate(value, 40)

    @property
    def TermPagoCdg(self) -> str:
        return self._terminoPagoCodigo

    @TermPagoCdg.setter
    def TermPagoCdg(self, value: str):
        self._terminoPagoCodigo = truncate(value, 4)

    @property
    def TermPagoGlosa(self) -> str:
        return self._terminoPagoGlosa

    @TermPagoGlosa.setter
    def TermPagoGlosa(self, value: str):
        self._terminoPagoGlosa = truncate(value, 100)

    def __init__(self):
        self.TipoDTE = DTEType.NOT_SET
        self.Folio = 0
        self.FechaEmisionString = ''
        self.IndNoRebaja = 0
        self.TipoDespacho = TipoDespachoEnum.NOT_SET
        self.IndTraslado = TipoTrasladoEnum.NOT_SET
        self.TpoImpresion = TipoImpresionEnum.N
        self.IndServicio = IndicadorServicioEnum.NOT_SET
        self.MntBruto = 0
        self.FmaPago = FormaPagoEnum.NOT_SET
        self.FmaPagExp = FormaPagoExportacionEnum.NOT_SET
        self.FechaCancelacionString = ''
        self.MntCancel = 0
        self.SaldoInsol = 0
        self.MntPagos = []
        self.PeriodoDesdeString = ''
        self.PeriodoHastaString = ''
        self.MedioPago = MedioPagoEnum.NOT_SET
        self.TpoCtaPago = TipoCuentaPagoEnum.NOT_SET
        self.NumCtaPago = ''
        self.BcoPago = ''
        self.TermPagoCdg = ''
        self.TermPagoGlosa = ''
        self.TermPagoDias = 0
        self.FechaVencimientoString = ''
        self.TipoTranCompra = None
        self.TipoTranVenta = None
        self.IndMntNeto = 0