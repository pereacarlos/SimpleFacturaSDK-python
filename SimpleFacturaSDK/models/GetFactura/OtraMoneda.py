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
    TpoMoneda: Moneda.NotSet
    tipoCambio: float
    montoNeto: float
    montoExento: float
    montoBaseFaenamientoCarne: float
    montoBaseMargenComercial: float
    iva: float
    ivaNoRetenido: float
    montoTotal: float 