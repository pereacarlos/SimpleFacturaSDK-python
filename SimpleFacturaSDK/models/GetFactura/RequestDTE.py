from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.Documento import Documento
from SimpleFacturaSDK.models.GetFactura.Exportaciones import Exportaciones
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.enumeracion.TipoDTE import DOCType, DTEType, DTEFacturasType
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicioEnum, IndicadorServicioDetalleLibroEnum


@dataclass
class RequestDTE:
    Documento: Optional[Documento] = field(default_factory=Documento)
    Exportaciones: Optional[Exportaciones] = None
    Observaciones: Optional[str] = None
    Cajero: Optional[str] = None
    TipoPago: Optional[str] = None
    Propina: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Documento=Documento.from_dict(data.get('Documento')) if data.get('Documento') else None,
            Exportaciones=Exportaciones.from_dict(data.get('Exportaciones')) if data.get('Exportaciones') else None,
            Observaciones=data.get('Observaciones'),
            Cajero=data.get('Cajero'),
            TipoPago=data.get('TipoPago'),
            Propina=data.get('Propina')
        )

    def to_dict(self):
        return asdict(self)