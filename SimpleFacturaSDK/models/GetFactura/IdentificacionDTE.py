from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Definición de las enumeraciones
class DTEType(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

class TipoDespachoEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

class TipoTrasladoEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

class TipoImpresionEnum(Enum):
    N = "N"
    # Agrega otros valores según sea necesario

class IndicadorServicioEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

class FormaPagoEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

class FormaPagoExportacionEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

class MedioPagoEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

class TipoCuentaPagoEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

@dataclass
class IdentificacionDTE:

    TipoDTE: DTEType = DTEType.NOT_SET

    Folio: int = 0

    FechaEmisionString: str = ''

    @property
    def FchEmis(self) -> datetime:
        return datetime.strptime(self.FechaEmisionString, "%Y-%m-%d")

    @FchEmis.setter
    def FchEmis(self, value: datetime):
        self.FechaEmisionString = value.strftime("%Y-%m-%d")

    IndNoRebaja: int = 0

    TipoDespacho: TipoDespachoEnum = TipoDespachoEnum.NOT_SET

    IndTraslado: TipoTrasladoEnum = TipoTrasladoEnum.NOT_SET

    TpoImpresion: TipoImpresionEnum = TipoImpresionEnum.N

    IndServicio: IndicadorServicioEnum = IndicadorServicioEnum.NOT_SET

    MntBruto: int = 0

    FmaPago: FormaPagoEnum = FormaPagoEnum.NOT_SET


    FmaPagExp: FormaPagoExportacionEnum = FormaPagoExportacionEnum.NOT_SET

    FechaCancelacionString: str = ''
    @property
    def FchCancel(self) -> datetime:
        return datetime.strptime(self.FechaCancelacionString, "%Y-%m-%d")

    @FchCancel.setter
    def FchCancel(self, value: datetime):
        self.FechaCancelacionString = value.strftime("%Y-%m-%d")

    MntCancel: int = 0

    SaldoInsol: int = 0

    MntPagos: List[int] = field(default_factory=list)

    PeriodoDesdeString: str = ''

    @property
    def PeriodoDesde(self) -> datetime:
        return datetime.strptime(self.PeriodoDesdeString, "%Y-%m-%d")

    @PeriodoDesde.setter
    def PeriodoDesde(self, value: datetime):
        self.PeriodoDesdeString = value.strftime("%Y-%m-%d")

    PeriodoHastaString: str = ''

    @property
    def PeriodoHasta(self) -> datetime:
        return datetime.strptime(self.PeriodoHastaString, "%Y-%m-%d")

    @PeriodoHasta.setter
    def PeriodoHasta(self, value: datetime):
        self.PeriodoHastaString = value.strftime("%Y-%m-%d")

    MedioPago: MedioPagoEnum = MedioPagoEnum.NOT_SET


    TpoCtaPago: TipoCuentaPagoEnum = TipoCuentaPagoEnum.NOT_SET

    _cuentaPago: str = ''

    @property
    def NumCtaPago(self) -> str:
        return self._cuentaPago

    @NumCtaPago.setter
    def NumCtaPago(self, value: str):
        self._cuentaPago = value[:20] 

    _bancoPago: str = ''

    @property
    def BcoPago(self) -> str:
        return self._bancoPago

    @BcoPago.setter
    def BcoPago(self, value: str):
        self._bancoPago = value[:40]  

    _terminoPagoCodigo: str = ''
 

    @property
    def TermPagoCdg(self) -> str:
        return self._terminoPagoCodigo

    @TermPagoCdg.setter
    def TermPagoCdg(self, value: str):
        self._terminoPagoCodigo = value[:4] 

    _terminoPagoGlosa: str = ''

    @property
    def TermPagoGlosa(self) -> str:
        return self._terminoPagoGlosa

    @TermPagoGlosa.setter
    def TermPagoGlosa(self, value: str):
        self._terminoPagoGlosa = value[:100]  

    TermPagoDias: int = 0

    FechaVencimientoString: str = ''

    @property
    def FchVenc(self) -> datetime:
        return datetime.strptime(self.FechaVencimientoString, "%Y-%m-%d")

    @FchVenc.setter
    def FchVenc(self, value: datetime):
        self.FechaVencimientoString = value.strftime("%Y-%m-%d")

    TipoTranCompra: Optional[str] = None

    TipoTranVenta: Optional[str] = None

    IndMntNeto: int = 0


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