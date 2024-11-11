from dataclasses import dataclass
from datetime import datetime
from typing import Optional
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

@dataclass
class IdentificacionDTE:
    TipoDTE: DTEType 
    Folio: int
    FchEmis: str
    IndNoRebaja: int
    TipoDespacho: TipoDespachoEnum
    IndTraslado: TipoTrasladoEnum
    TpoImpresion: TipoImpresionEnum
    IndServicio: IndicadorServicioEnum
    MntBruto: int
    FmaPago: FormaPagoEnum
    FechaCancelacionString: str
    MntCancel: float
    SaldoInsol: float
    MntPagos: float
    PeriodoDesdeString: str
    PeriodoHastaString: str
    MedioPago: MedioPagoEnum
    TpoCtaPago: TipoCuentaPagoEnum
    NumCtaPago: str
    BcoPago: str
    TermPagoCdg: str
    TermPagoGlosa: str
    TermPagoDias: int
    FchVenc: str
    TipoTranCompra: TipoTransCompra
    TipoTransVenta: TipoTransVenta
    IndMntNeto: int
    FchCancel: datetime
    PeriodoDesde: datetime
    PeriodoHasta: datetime

'''
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TipoDTE=DTEType(data.get('TipoDTE')) if data.get('TipoDTE') else None,
            Folio=data.get('Folio'),
            FchEmis=data.get('FchEmis'),
            IndNoRebaja=data.get('IndNoRebaja'),
            TipoDespacho=TipoDespachoEnum(data.get('TipoDespacho')) if data.get('TipoDespacho') else None,
            IndTraslado=TipoTrasladoEnum(data.get('IndTraslado')) if data.get('IndTraslado') else None,
            TpoImpresion=TipoImpresionEnum(data.get('TpoImpresion')) if data.get('TpoImpresion') else None,
            IndServicio=IndicadorServicioEnum(data.get('IndServicio')) if data.get('IndServicio') else None,
            MntBruto=data.get('MntBruto'),
            FmaPago=FormaPagoEnum(data.get('FmaPago')) if data.get('FmaPago') else None,
            FechaCancelacionString=data.get('FechaCancelacionString'),
            MntCancel=data.get('MntCancel'),
            SaldoInsol=data.get('SaldoInsol'),
            MntPagos=data.get('MntPagos'),
            PeriodoDesdeString=data.get('PeriodoDesdeString'),
            PeriodoHastaString=data.get('PeriodoHastaString'),
            MedioPago=MedioPagoEnum(data.get('MedioPago')) if data.get('MedioPago') else None,
            TpoCtaPago=TipoCuentaPagoEnum(data.get('TpoCtaPago')) if data.get('TpoCtaPago') else None,
            NumCtaPago=data.get('NumCtaPago'),
            BcoPago=data.get('BcoPago'),
            TermPagoCdg=data.get('TermPagoCdg'),
            TermPagoGlosa=data.get('TermPagoGlosa'),
            TermPagoDias=data.get('TermPagoDias'),
            FchVenc=data.get('FchVenc'),
            TipoTranCompra=TipoTransCompra(data.get('TipoTranCompra')) if data.get('TipoTranCompra') else None,
            TipoTransVenta=TipoTransVenta(data.get('TipoTransVenta')) if data.get('TipoTransVenta') else None,
            IndMntNeto=data.get('IndMntNeto'),
            FchCancel=data.get('FchCancel'),
            PeriodoDesde=data.get('PeriodoDesde'),
            PeriodoHasta=data.get('PeriodoHasta')
        )

    def to_dict(self):
        return {
            'TipoDTE': self.TipoDTE.value if self.TipoDTE else None,
            'Folio': self.Folio,
            'FechaEmisionString': self.FechaEmisionString,
            'IndNoRebaja': self.IndNoRebaja,
            'TipoDespacho': self.TipoDespacho.value if self.TipoDespacho else None,
            'IndTraslado': self.IndTraslado.value if self.IndTraslado else None,
            'TpoImpresion': self.TpoImpresion.value if self.TpoImpresion else None,
            'IndServicio': self.IndServicio.value if self.IndServicio else None,
            'MntBruto': self.MntBruto,
            'FmaPagExp': self.FmaPagExp.value if self.FmaPagExp else None,
            'FechaCancelacionString': self.FechaCancelacionString,
            'MntCancel': self.MntCancel,
            'SaldoInsol': self.SaldoInsol,
            'MntPagos': self.MntPagos,
            'PeriodoDesdeString': self.PeriodoDesdeString,
            'PeriodoHastaString': self.PeriodoHastaString,
            'MedioPago': self.MedioPago.value if self.MedioPago else None,
            'TpoCtaPago': self.TpoCtaPago.value if self.TpoCtaPago else None,
            'NumCtaPago': self.NumCtaPago,
            'BcoPago': self.BcoPago,
            'TermPagoCdg': self.TermPagoCdg,
            'TermPagoGlosa': self.TermPagoGlosa,
            'TermPagoDias': self.TermPagoDias,
            'FechaVencimientoString': self.FechaVencimientoString,
            'TipoTranCompra': self.TipoTranCompra.value if self.TipoTranCompra else None,
            'TipoTransVenta': self.TipoTransVenta.value if self.TipoTransVenta else None,
            'IndMntNeto': self.IndMntNeto,
            'FchCancel': self.FchCancel,
            'PeriodoDesde': self.PeriodoDesde,
            'PeriodoHasta': self.PeriodoHasta
        }

'''