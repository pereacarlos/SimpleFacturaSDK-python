from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

# Definición de la enumeración
class Moneda(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

@dataclass
class OtraMoneda:
    TpoMoneda: Moneda = Moneda.NOT_SET
    __tipoCambio: float = 0.0
    __montoNeto: float = 0.0
    __montoExento: float = 0.0
    __montoBaseFaenamientoCarne: float = 0.0
    __montoBaseMargenComercial: float = 0.0
    __VAOtrMnda: float = 0.0
    ImpRetOtrMnda: Optional[List[ImpuestosRetencionesOtraMoneda]] = None
    _IVANoRetenido: float = 0.0
    _montoTotal: float = 0.0

    @property
    def TpoCambio(self) -> float:
        return round(self._tipoCambio, 4)

    @TpoCambio.setter
    def TpoCambio(self, value: float):
        self._tipoCambio = value

    @property
    def MntNetoOtrMnda(self) -> float:
        return round(self._montoNeto, 4)

    @MntNetoOtrMnda.setter
    def MntNetoOtrMnda(self, value: float):
        self._montoNeto = value

    @property
    def MntExeOtrMnda(self) -> float:
        return round(self._montoExento, 4)

    @MntExeOtrMnda.setter
    def MntExeOtrMnda(self, value: float):
        self._montoExento = value

    @property
    def MntFaeCarneOtrMnda(self) -> float:
        return round(self._montoBaseFaenamientoCarne, 4)

    @MntFaeCarneOtrMnda.setter
    def MntFaeCarneOtrMnda(self, value: float):
        self._montoBaseFaenamientoCarne = value

    @property
    def MntMargComOtrMnda(self) -> float:
        return round(self._montoBaseMargenComercial, 4)

    @MntMargComOtrMnda.setter
    def MntMargComOtrMnda(self, value: float):
        self._montoBaseMargenComercial = value

    @property
    def IVAOtrMnda(self) -> float:
        return round(self._IVA, 4)

    @IVAOtrMnda.setter
    def IVAOtrMnda(self, value: float):
        self._IVA = value

    @property
    def IVANoRetOtrMnda(self) -> float:
        return round(self._IVANoRetenido, 4)

    @IVANoRetOtrMnda.setter
    def IVANoRetOtrMnda(self, value: float):
        self._IVANoRetenido = value

    @property
    def MntTotOtrMnda(self) -> float:
        return round(self._montoTotal, 4)

    @MntTotOtrMnda.setter
    def MntTotOtrMnda(self, value: float):
        self._montoTotal = value

    def __init__(self):
        self.TpoMoneda = Moneda.NOT_SET
        self.TpoCambio = 0.0
        self.MntNetoOtrMnda = 0.0
        self.MntExeOtrMnda = 0.0
        self.MntFaeCarneOtrMnda = 0.0
        self.MntMargComOtrMnda = 0.0
        self.IVAOtrMnda = 0.0
        self.ImpRetOtrMnda = []
        self.IVANoRetOtrMnda = 0.0
        self.MntTotOtrMnda = 0.0