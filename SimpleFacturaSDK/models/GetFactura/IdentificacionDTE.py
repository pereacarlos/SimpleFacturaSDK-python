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
    TipoDTE: DTEType = None
    Folio: int = None
    FechaEmisionString: str = None
    IndNoRebaja: int = 0
    TipoDespacho: TipoDespachoEnum.NotSet = None
    IndTraslado: TipoTrasladoEnum.NotSet = None
    TpoImpresion: TipoImpresionEnum.N = None
    IndServicio: IndicadorServicioEnum.NotSet = None
    MntBruto: int = 0
    FmaPago: FormaPagoEnum = None
    FmaPagExp: FormaPagoExportacionEnum.NotSet= None
    FechaCancelacionString: str = None
    MntCancel: int = 0
    SaldoInsol: int = 0
    MntPagos: List[MontoPagoItem] = field(default_factory=list)
    PeriodoDesdeString: str = None
    PeriodoHastaString: str = None
    MedioPago: MedioPagoEnum.NotSet = None
    TpoCtaPago: TipoCuentaPagoEnum.NotSet = None
    NumCtaPago: str = ''
    BcoPago: str = ''
    TermPagoCdg: str = ''
    TermPagoGlosa: str = ''
    TermPagoDias: int = 0
    FechaVencimientoString: str= None
    TipoTranCompra: TipoTransCompra = None
    TipoTransVenta: TipoTransVenta = None
    IndMntNeto: int = None
    FchEmis: datetime = None
    FchVenc: datetime = None
    FchCancel: datetime= None
    PeriodoDesde:datetime = None
    PeriodoHasta: datetime = None

    # Private fields for internal use
    __cuentaPago: str = field(init=False, default=None, metadata={"max_length": 20})
    __bancoPago: str = field(init=False, default=None, metadata={"max_length": 40})
    __terminoPagoCodigo: str = field(init=False, default=None, metadata={"max_length": 4})
    __terminoPagoGlosa: str = field(init=False, default=None, metadata={"max_length": 100})

   

    def __post_init__(self):
        self.FchEmis = datetime.strptime(self.FechaEmisionString, '%Y-%m-%d') if self.FechaEmisionString else None
        self.FchVenc = datetime.strptime(self.FechaVencimientoString, '%Y-%m-%d') if self.FechaVencimientoString else None
        self.FchCancel = datetime.strptime(self.FechaCancelacionString, '%Y-%m-%d') if self.FechaCancelacionString else None
        self.PeriodoDesde = datetime.strptime(self.PeriodoDesdeString, '%Y-%m-%d') if self.PeriodoDesdeString else None
        self.PeriodoHasta = datetime.strptime(self.PeriodoHastaString, '%Y-%m-%d') if self.PeriodoHastaString else None
        self.__cuentaPago = truncate(self.NumCtaPago, 20)
        self.__bancoPago = truncate(self.BcoPago, 40)
        self.__terminoPagoCodigo = truncate(self.TermPagoCdg, 4)
        self.__terminoPagoGlosa = truncate(self.TermPagoGlosa, 100)
        self.TipoDespacho = TipoDespachoEnum(self.TipoDespacho) if self.TipoDespacho else None
   

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TipoDTE=data.get('TipoDTE'),
            Folio=data.get('Folio'),
            FechaEmisionString=data.get('FchEmis'),
            IndNoRebaja=data.get('IndNoRebaja'),
            TipoDespacho=data.get('TipoDespacho'),
            IndTraslado=data.get('IndTraslado'),
            TpoImpresion=data.get('TpoImpresion'),
            IndServicio=data.get('IndServicio'),
            MntBruto=data.get('MntBruto'),
            FmaPago=data.get('FmaPago'),
            FmaPagExp=data.get('FmaPagExp'),
            FechaCancelacionString=data.get('FechaCancelacionString'),
            MntCancel=data.get('MntCancel'),
            SaldoInsol=data.get('SaldoInsol'),
            MntPagos=[MontoPagoItem.from_dict(d) for d in data.get('MntPagos', [])],
            PeriodoDesdeString=data.get('PeriodoDesdeString'),
            PeriodoHastaString=data.get('PeriodoHastaString'),
            MedioPago=data.get('MedioPago'),
            TpoCtaPago=data.get('TpoCtaPago'),
            TermPagoDias=data.get('TermPagoDias'),
            FechaVencimientoString=data.get('FchVenc'),
            IndMntNeto=data.get('IndMntNeto')
        )
    
 