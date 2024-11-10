from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.Documento import Documento
from SimpleFacturaSDK.models.GetFactura.Exportaciones import Exportaciones
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType, CustomJSONEncoder
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicioEnum


@dataclass
class RequestDTE:
    Documento: Optional[Documento] 
    Exportaciones: Optional[Exportaciones] 
    Observaciones: Optional[str]
    Cajero: Optional[str] 
    TipoPago: Optional[str] 
    Propina: Optional[int]   

    

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Documento=Documento,
            Exportaciones=Exportaciones,
            Observaciones=data.get('Observaciones'),
            Cajero=data.get('Cajero'),
            TipoPago=data.get('TipoPago'),
            Propina=data.get('Propina')
        )

    def to_dict(self):
        return asdict(self)
