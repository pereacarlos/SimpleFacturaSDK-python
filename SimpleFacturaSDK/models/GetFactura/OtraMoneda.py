from dataclasses import dataclass, field
from typing import List, Optional
from SimpleFacturaSDK.enumeracion.CodigosAduana import Moneda
from SimpleFacturaSDK.models.GetFactura.ImpuestosRetencionesOtraMoneda import ImpuestosRetencionesOtraMoneda
@dataclass
class OtraMoneda:
    TpoMoneda: Moneda = Moneda.NotSet
    ImpRetOtrMnda: Optional[List[ImpuestosRetencionesOtraMoneda]] = field(default_factory=list)

    __tipoCambio: float = field(default=0.0, init=False)
    __montoNeto: float = field(default=0.0, init=False)
    __montoExento: float = field(default=0.0, init=False)
    __montoBaseFaenamientoCarne: float = field(default=0.0, init=False)
    __montoBaseMargenComercial: float = field(default=0.0, init=False)
    __IVA: float = field(default=0.0, init=False)
    __IVANoRetenido: float = field(default=0.0, init=False)
    __montoTotal: float = field(default=0.0, init=False)

    @property
    def TpoCambio(self) -> float:
        return round(self.__tipoCambio, 4)

    @TpoCambio.setter
    def TpoCambio(self, value: float):
        self.__tipoCambio = value

    @property
    def MntNetoOtrMnda(self) -> float:
        return round(self.__montoNeto, 4)

    @MntNetoOtrMnda.setter
    def MntNetoOtrMnda(self, value: float):
        self.__montoNeto = value

    @property
    def MntExeOtrMnda(self) -> float:
        return round(self.__montoExento, 4)

    @MntExeOtrMnda.setter
    def MntExeOtrMnda(self, value: float):
        self.__montoExento = value

    @property
    def MntFaeCarneOtrMnda(self) -> float:
        return round(self.__montoBaseFaenamientoCarne, 4)

    @MntFaeCarneOtrMnda.setter
    def MntFaeCarneOtrMnda(self, value: float):
        self.__montoBaseFaenamientoCarne = value

    @property
    def MntMargComOtrMnda(self) -> float:
        return round(self.__montoBaseMargenComercial, 4)

    @MntMargComOtrMnda.setter
    def MntMargComOtrMnda(self, value: float):
        self.__montoBaseMargenComercial = value

    @property
    def IVAOtrMnda(self) -> float:
        return round(self.__IVA, 4)

    @IVAOtrMnda.setter
    def IVAOtrMnda(self, value: float):
        self.__IVA = value

    @property
    def IVANoRetOtrMnda(self) -> float:
        return round(self.__IVANoRetenido, 4)

    @IVANoRetOtrMnda.setter
    def IVANoRetOtrMnda(self, value: float):
        self.__IVANoRetenido = value

    @property
    def MntTotOtrMnda(self) -> float:
        return round(self.__montoTotal, 4)

    @MntTotOtrMnda.setter
    def MntTotOtrMnda(self, value: float):
        self.__montoTotal = value

    def __init__(self):
        self.TpoMoneda = Moneda.NotSet
        self.TpoCambio = 0.0
        self.MntNetoOtrMnda = 0.0
        self.MntExeOtrMnda = 0.0
        self.MntFaeCarneOtrMnda = 0.0
        self.MntMargComOtrMnda = 0.0
        self.IVAOtrMnda = 0.0
        self.ImpRetOtrMnda = []
        self.IVANoRetOtrMnda = 0.0
        self.MntTotOtrMnda = 0.0