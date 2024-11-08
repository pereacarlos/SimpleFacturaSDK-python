from dataclasses import dataclass, field
from typing import List, Optional
from  SimpleFacturaSDK.enumeracion.CodigosAduana import Moneda
from SimpleFacturaSDK.models.GetFactura.ImpuestosRetenciones import ImpuestosRetenciones
from SimpleFacturaSDK.models.GetFactura.Comisiones import Comisiones



@dataclass
class Totales:
    TpoMoneda: Moneda = Moneda.NotSet
    MntNeto: float = 0.0
    MntExe: float = 0.0
    MntBase: int = 0
    MntMargenCom: int = 0
    TasaIVA: float = 0.0
    IVA: int = 0
    IVAProp: int = 0
    IVATerc: int = 0
    ImptoReten: Optional[List[ImpuestosRetenciones]] = field(default_factory=list)
    IVANoRet: int = 0
    CredEC: int = 0
    GrntDep: int = 0
    Comisiones: Optional[List[Comisiones]] = field(default_factory=list)
    MntTotal: float = 0.0
    MontoNF: int = 0
    MontoPeriodo: int = 0
    SaldoAnterior: int = 0
    VlrPagar: int = 0

    def __post_init__(self):
        self.TpoMoneda = Moneda.NotSet
        self.MntNeto = 0.0
        self.MntExe = 0.0
        self.MntBase = 0
        self.MntMargenCom = 0
        self.TasaIVA = 0.0
        self.IVA = 0
        self.IVAProp = 0
        self.IVATerc = 0
        self.ImptoReten = []
        self.IVANoRet = 0
        self.CredEC = 0
        self.GrntDep = 0
        self.Comisiones = []
        self.MntTotal = 0.0
        self.MontoNF = 0
        self.MontoPeriodo = 0
        self.SaldoAnterior = 0
        self.VlrPagar = 0


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TpoMoneda=data.get('TpoMoneda'),
            MntNeto=data.get('MntNeto'),
            MntExe=data.get('MntExe'),
            MntBase=data.get('MntBase'),
            MntMargenCom=data.get('MntMargenCom'),
            TasaIVA=data.get('TasaIVA'),
            IVA=data.get('IVA'),
            IVAProp=data.get('IVAProp'),
            IVATerc=data.get('IVATerc'),
            ImptoReten=[ImpuestosRetenciones.from_dict(d) for d in data.get('ImptoReten')],
            IVANoRet=data.get('IVANoRet'),
            CredEC=data.get('CredEC'),
            GrntDep=data.get('GrntDep'),
            Comisiones=[Comisiones.from_dict(d) for d in data.get('Comisiones')],
            MntTotal=data.get('MntTotal'),
            MontoNF=data.get('MontoNF'),
            MontoPeriodo=data.get('MontoPeriodo'),
            SaldoAnterior=data.get('SaldoAnterior'),
            VlrPagar=data.get('VlrPagar')
        )