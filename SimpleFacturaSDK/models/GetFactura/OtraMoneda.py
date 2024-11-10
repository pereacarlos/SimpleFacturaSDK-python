from dataclasses import dataclass, field
from typing import Optional, List
from SimpleFacturaSDK.enumeracion.CodigosAduana import Moneda
from SimpleFacturaSDK.models.GetFactura.ImpuestosRetencionesOtraMoneda import ImpuestosRetencionesOtraMoneda


@dataclass
class OtraMoneda:
    TpoCambio: float
    MntNetoOtrMnda: float
    MntExeOtrMnda: float
    MntFaeCarneOtrMnda: float 
    MntMargComOtrMnda: float
    IVAOtrMnda: float 
    IVANoRetOtrMnda: float
    MntTotOtrMnda: float 
    ImpRetOtrMnda: Optional[List[ImpuestosRetencionesOtraMoneda]]

    TpoMoneda: Moneda = Moneda.NotSet

    __tipoCambio: float
    __montoNeto: float
    __montoExento: float
    __montoBaseFaenamientoCarne: float
    __montoBaseMargenComercial: float
    __iva: float
    __ivaNoRetenido: float
    __montoTotal: float 

    def __post_init__(self):
        self.__tipoCambio = round(self.TpoCambio, 4)
        self.__montoNeto = round(self.MntNetoOtrMnda, 4)
        self.__montoExento = round(self.MntExeOtrMnda, 4)
        self.__montoBaseFaenamientoCarne = round(self.MntFaeCarneOtrMnda, 4)
        self.__montoBaseMargenComercial = round(self.MntMargComOtrMnda, 4)
        self.__iva = round(self.IVAOtrMnda, 4)
        self.__ivaNoRetenido = round(self.IVANoRetOtrMnda, 4)
        self.__montoTotal = round(self.MntTotOtrMnda, 4)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TpoCambio=data.get('TpoCambio'),
            MntNetoOtrMnda=data.get('MntNetoOtrMnda'),
            MntExeOtrMnda=data.get('MntExeOtrMnda'),
            MntFaeCarneOtrMnda=data.get('MntFaeCarneOtrMnda'),
            MntMargComOtrMnda=data.get('MntMargComOtrMnda'),
            IVAOtrMnda=data.get('IVAOtrMnda'),
            IVANoRetOtrMnda=data.get('IVANoRetOtrMnda'),
            MntTotOtrMnda=data.get('MntTotOtrMnda'),
            TpoMoneda=Moneda(data.get('TpoMoneda')),
            ImpRetOtrMnda=[ImpuestosRetencionesOtraMoneda]
        )