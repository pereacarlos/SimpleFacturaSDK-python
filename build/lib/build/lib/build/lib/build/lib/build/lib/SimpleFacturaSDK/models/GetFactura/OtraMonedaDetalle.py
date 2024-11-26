from dataclasses import dataclass, field

@dataclass
class OtraMonedaDetalle:
    PrcOtrMon: float 
    Moneda: str 
    FctConv: float 
    DctoOtrMnda: float 
    RecargoOtrMnda: float 
    MontoItemOtrMnda: float
