from dataclasses import dataclass, field
from typing import Optional, List
from SimpleFacturaSDK.enumeracion.CodigosAduana import Moneda
from SimpleFacturaSDK.models.GetFactura.ImpuestosRetencionesOtraMoneda import ImpuestosRetencionesOtraMoneda

@dataclass
class OtraMoneda:
    TpoCambio: float
    MntNetoOtrMnda: float
    MntExeOtrMnda: float
    TpoMoneda: Moneda
    IVANoRetOtrMnda: Optional[float] = None
    MntTotOtrMnda: Optional[float] = None
    IVAOtrMnda: Optional[float] = None
    MntFaeCarneOtrMnda: Optional[float] = None
    MntMargComOtrMnda: Optional[float] = None
    tipoCambio: Optional[float] = None
    montoNeto: Optional[float] = None
    montoExento: Optional[float] = None
    montoBaseFaenamientoCarne: Optional[float] = None
    montoBaseMargenComercial: Optional[float] = None
    iva: Optional[float] = None
    ivaNoRetenido: Optional[float] = None
    montoTotal: Optional[float] = None