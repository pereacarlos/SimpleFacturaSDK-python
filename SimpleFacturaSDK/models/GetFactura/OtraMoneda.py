from dataclasses import dataclass, field
from typing import Optional, List
from SimpleFacturaSDK.enumeracion.CodigosAduana import Moneda
from SimpleFacturaSDK.models.GetFactura.ImpuestosRetencionesOtraMoneda import ImpuestosRetencionesOtraMoneda


@dataclass
class OtraMoneda:
    TpoCambio: float = 0.0
    MntNetoOtrMnda: float = 0.0
    MntExeOtrMnda: float = 0.0
    MntFaeCarneOtrMnda: float = 0.0
    MntMargComOtrMnda: float = 0.0
    IVAOtrMnda: float = 0.0
    IVANoRetOtrMnda: float = 0.0
    MntTotOtrMnda: float = 0.0
    ImpRetOtrMnda: Optional[List[ImpuestosRetencionesOtraMoneda]] = field(default_factory=list)

    TpoMoneda: Moneda = Moneda.NotSet

    __tipoCambio: float = field(default=0.0, init=False, metadata={"decimals": 4})
    __montoNeto: float = field(default=0.0, init=False, metadata={"decimals": 4})
    __montoExento: float = field(default=0.0, init=False, metadata={"decimals": 4})
    __montoBaseFaenamientoCarne: float = field(default=0.0, init=False, metadata={"decimals": 4})
    __montoBaseMargenComercial: float = field(default=0.0, init=False, metadata={"decimals": 4})
    __iva: float = field(default=0.0, init=False, metadata={"decimals": 4})
    __ivaNoRetenido: float = field(default=0.0, init=False, metadata={"decimals": 4})
    __montoTotal: float = field(default=0.0, init=False, metadata={"decimals": 4})

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
            ImpRetOtrMnda=[ImpuestosRetencionesOtraMoneda.from_dict(i) for i in data.get('ImpRetOtrMnda', [])]
        )